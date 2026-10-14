import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prepare_asset_approval_handoff import FIELDS, request_rows, write_handoff


class ApprovalHandoffTests(unittest.TestCase):
    def test_all_44_rows_are_unapproved_and_not_submitted(self):
        rows = request_rows()
        self.assertEqual(len(rows), 44)
        self.assertEqual(len({r['asset_id'] for r in rows}), 44)
        self.assertEqual(sum(r['asset_id'].startswith('hs2-img-drill-') for r in rows), 6)
        self.assertEqual(sum(r['asset_id'].startswith('ehr-shot-') for r in rows), 31)
        for row in rows:
            self.assertEqual(row['status'], 'Pending — not submitted')
            for field in ['reviewer_name', 'review_date', 'signed_decision', 'approved_file_or_record']:
                self.assertEqual(row[field], '')
            self.assertIn('PENDING', row['production_gate'])
            self.assertTrue(row['draft_alt'])

    def test_deterministic_packet(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            request = write_handoff(out)
            before = {p.name: p.read_bytes() for p in out.iterdir()}
            write_handoff(out)
            self.assertEqual(before, {p.name: p.read_bytes() for p in out.iterdir()})
            self.assertFalse(request['production_authorised'])
            self.assertEqual(request['required_video_count'], 0)
            self.assertEqual(json.loads((out / 'request.json').read_text())['asset_count'], 44)

    def test_human_responses_are_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp)
            write_handoff(out)
            path = out / 'response-template.csv'
            rows = request_rows()
            rows[0]['comments'] = 'Reviewer clarification: keep this evidence.'
            with path.open('w', newline='') as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader(); writer.writerows(rows)
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'human updates'):
                write_handoff(out)
            self.assertEqual(path.read_bytes(), before)


if __name__ == '__main__':
    unittest.main()
