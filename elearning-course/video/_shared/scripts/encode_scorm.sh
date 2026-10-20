#!/usr/bin/env bash
# Encode the 1080p master into the SCORM deliverable: 720p H.264, capped bitrate, mono AAC 96k,
# loudness normalised to -16 LUFS / -1 dBTP, faststart. Then run delivery_check.py on the result.
#   bash encode_scorm.sh renders/<clip-id>_master_1080p.mp4 renders/<clip-id>.mp4
set -euo pipefail
in="$1"; out="$2"
ffmpeg -y -hide_banner -i "$in" \
  -vf "scale=1280:720:flags=lanczos,format=yuv420p" -r 30 \
  -c:v libx264 -preset slow -crf 26 -maxrate 1200k -bufsize 2400k -profile:v high \
  -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ac 1 -ar 48000 -c:a aac -b:a 96k \
  -movflags +faststart "$out"
echo "encoded $out"
