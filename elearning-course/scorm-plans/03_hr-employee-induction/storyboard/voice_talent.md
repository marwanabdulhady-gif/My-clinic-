# Voice-over script — MC03-welcome-on-board

Language: en · Pace: ~140 wpm · Two voices: **Dr. Omar** (lead host) and **Noor** (co-host) — [`companions.md`](../../00_program/characters/companions.md) §5.

## Voices

| Voice | Brief | Lines in this module | Provider / voice id |
|---|---|---|---|
| **Dr. Omar** (`OMAR:`) | Male, late 30s, friendly, confident and relaxed; international English with a light Gulf Arabic accent welcome; medium-low pitch; ~140 wpm | 35 | Pending program **D10** |
| **Noor** (`NOOR:`) | Female, early-to-mid 30s, warm, calm and clear; international English with a light Gulf Arabic accent welcome; smiling but not bubbly; ~140 wpm | 4 | Pending program **D10** |

Neither voice may be cloned from, or resemble, a real My Clinic employee. Record a 30-second sample of each voice reading a “meet your guide” line for approval before producing this module. Once D10 closes, record the provider and voice ids in `00_program/narration-and-lexicon.md` §1 and in `narration-script.json` → `voice`.

The speaker label (`OMAR:` / `NOOR:`) selects the voice and is **not** spoken; `tts_text` in [`audio-script-export.json`](audio-script-export.json) already has it removed and the lexicon applied. Two-voice screens are recorded as one file per `part` and joined with 0.3 s of silence (companions.md §5).

## Pronunciation guide

- **GOSI** → GO-see
- **SCFHS** → S-C-F-H-S
- **Mumaris** → mu-MAH-ris
- **Qiwa** → KEE-wa
- **HRMS** → H-R-M-S
- **SAR** → Saudi riyals
- **HHC** → home health care
- **CBAHI** → see-bah-hee
- **MCJ1** → M-C-J-one
- **MCJ2** → M-C-J-two
- **PRC** → P-R-C
- **J1** → J-one
- **J2** → J-two
- **J3** → J-three
- **J4** → J-four
- **D1** → D-one
- **R1** → R-one
- **EOS** → end of service
- **IELTS** → eye-elts
- **TOEFL** → toe-full
- **Oracle** → OR-uh-kul
- **CEO** → C-E-O
- **CMO** → C-M-O
- **COO** → C-O-O
- **CFO** → C-F-O
- **ID** → I-D
- **MD** → M-D
- **Hajj** → hajj
- **Eid** → eed
- **HR** → H-R
- **VIP** → V-I-P
- **Noor** → noor
- **Omar** → OH-mar

## Recording table

| # | Screen / part | Speaker | Tone | Script | Est. sec | File |
|---|---|---|---|---|---|---|
| 1 | `hr-000/omar-1` | omar | warm | OMAR: Welcome to My Clinic. I'm Dr. Omar, a family physician at J2. Today you'll meet who we are, and the HR rules you'll actually use. | 11.1 | `MC03-welcome-on-board_hr-000_omar-1.mp3` |
| 2 | `hr-000/noor-1` | noor | warm | NOOR: *(pause 0.3s)* And I'm Noor, a senior nurse at J1. Nothing here is a memory test. We'll show you where to find things. | 9.7 | `MC03-welcome-on-board_hr-000_noor-1.mp3` |
| 3 | `hr-001` | omar | warm | OMAR: Our purpose is simple to say and hard to do: we help people live longer, healthier, happier lives, including people who are well today. *(pause 0.4s)* Our mission is to be the world's most customer-centric healthcare company. In practice, every role asks one question: did this help the patient? *(pause 0.4s)* Our goal follows from that: outstanding patient experience, alongside excellent clinical outcomes. *(pause 0.4s)* Honestly, my first week here, I felt there was too much to take in. You don't need to remember everything today — just where to find it. | 38.1 | `MC03-welcome-on-board_hr-001.mp3` |
| 4 | `hr-002` | omar | warm | OMAR: Before we start: if you had one million Saudi riyals, where would you spend it? There's no right answer. Pick whatever is closest. | 10.3 | `MC03-welcome-on-board_hr-002.mp3` |
| 5 | `hr-010` | omar | warm | OMAR: Every clinic has values on a wall. Ours only matter if you can see them in what people do. *(pause 0.4s)* Collaborative: we act together, treat everyone with respect, and stay transparent. *(pause 0.4s)* Responsible: own your decisions, make things happen, and hold each other to the same standard. *(pause 0.4s)* Ambitious: go above and beyond, and challenge the status quo when it stops serving patients. *(pause 0.4s)* Caring: act with empathy, because everyone matters. *(pause 0.4s)* As you go on, think which of these you already do without being asked. | 37.1 | `MC03-welcome-on-board_hr-010.mp3` |
| 6 | `hr-011` | omar | encouraging | OMAR: Here are six things people did this week. Match each one to the value behind it. | 7.3 | `MC03-welcome-on-board_hr-011.mp3` |
| 7 | `hr-012` | omar | calm | OMAR: Strategy feels like someone else's job until you find your own work inside it. Here are the seven pillars. *(pause 0.4s)* Closer: convenient access — clinics, community clinics and home health care, digital services, telemedicine. *(pause 0.4s)* Cure: the best Saudi doctors, clinical outcomes, centres of excellence, prevention and wellbeing. *(pause 0.4s)* Capabilities: a repeatable model for running and growing clinics, with real governance. *(pause 0.4s)* Culture: our mission and values, servant leadership, a culture of excellence. *(pause 0.4s)* Clinicians: a caring environment, competitive benefits, room to grow. *(pause 0.4s)* Care: seamless experience, empathy, loyalty built through My Care. *(pause 0.4s)* Cost: competitive cost to serve. *(pause 0.4s)* Whichever one you picked, that's your line in. | 46.1 | `MC03-welcome-on-board_hr-012.mp3` |
| 8 | `hr-013` | omar | encouraging | OMAR: One to try. My Care follow-up calls build patient loyalty. Which pillar do they belong to? | 7.3 | `MC03-welcome-on-board_hr-013.mp3` |
| 9 | `hr-014` | omar | warm | OMAR: Who do we serve? First, patients and their families — sick or healthy. Many of the people who walk in today are well, and we want them to stay that way. *(pause 0.4s)* Second, the community around each clinic. *(pause 0.3s)* Third, corporates and insurers. Three groups, one standard. | 20.0 | `MC03-welcome-on-board_hr-014.mp3` |
| 10 | `hr-020` | omar | warm | OMAR: We opened our first clinic in North Jeddah in 2017. *(pause 0.3s)* In 2019 we started the employment check-up unit, our first corporate service. *(pause 0.3s)* Then came East Jeddah, the dental centre, and Petro-Rabigh in 2023, our first clinic inside a corporate community. *(pause 0.3s)* Riyadh followed in 2024, a flagship to put the brand on the map. *(pause 0.3s)* The last two years added our first community clinics. Nine years, nine steps, one idea: bring good care closer. | 32.5 | `MC03-welcome-on-board_hr-020.mp3` |
| 11 | `hr-021` | omar | warm | OMAR: You'll hear these codes every day, so it's worth knowing what they mean. Open all seven pins. J one, J two, D one, J three, J four, P-R-C and R one. | 13.7 | `MC03-welcome-on-board_hr-021.mp3` |
| 12 | `hr-022` | omar | warm | OMAR: Four people lead the company. The CEO sets the direction. *(pause 0.4s)* The CMO owns clinical standards — questions about how we practise medicine land here. *(pause 0.4s)* The COO runs the clinics day to day. *(pause 0.3s)* The CFO looks after the money. You'll see their decisions in how your clinic runs. | 21.2 | `MC03-welcome-on-board_hr-022.mp3` |
| 13 | `hr-023` | omar | warm | OMAR: We're proud of these, so flip them. And hold one thought alongside them. Accreditation is measured, not given. Every score here expires, and the next survey team will look at what we did this year, not at these cards. | 17.1 | `MC03-welcome-on-board_hr-023.mp3` |
| 14 | `hr-030` | omar | serious | OMAR: Four values sit under everything. Respect — the rights, privacy and dignity of patients, families and colleagues. *(pause 0.4s)* Integrity — be transparent, and disclose any conflict of interest. *(pause 0.4s)* Accountability — a culture where people report safety concerns instead of staying quiet. *(pause 0.4s)* Innovation and collaboration — research and community work that improves outcomes. *(pause 0.5s)* And the rule you'll use: faced with an ethical dilemma, complete an incident report within twenty-four hours and bring in the ethics team. You're never expected to work it out alone. | 35.6 | `MC03-welcome-on-board_hr-030.mp3` |
| 15 | `hr-031` | noor | serious | NOOR: Three moments now, and nobody is watching. First: you're on a panel evaluating suppliers for a clinic fit-out, and one bidder is your cousin's company. The evaluation starts in an hour. What do you do? | 15.4 | `MC03-welcome-on-board_hr-031.mp3` |
| 16 | `hr-032` | omar | encouraging | OMAR: Nine statements from reception. Sort each: is it what the patient can expect, or what we ask of them? | 8.6 | `MC03-welcome-on-board_hr-032.mp3` |
| 17 | `hr-033` | omar | calm | OMAR: Last one here. A patient refuses a blood test after the doctor has explained the risks. What do you do? | 9.0 | `MC03-welcome-on-board_hr-033.mp3` |
| 18 | `hr-040` | omar | practical | OMAR: Where help lives. First, your HR help desk — one per business unit, so you'll talk to people who know your clinic. *(pause 0.4s)* Second, Oracle. If it's a request, it goes through Oracle. That's the only way it has a record. *(pause 0.4s)* Third, the HR Quick Reference: two pages with every leave table and the pay rules. Download it now. You don't need to memorise this. | 28.2 | `MC03-welcome-on-board_hr-040.mp3` |
| 19 | `hr-041` | omar | practical | OMAR: Nine types. Open the ones you need. *(pause 0.3s)* Annual: after probation, five days carried over, used by end of March. *(pause 0.3s)* Sick: valid report needed. First thirty days paid in full. *(pause 0.3s)* Work injury covers commuting, and has a same-day or next-day deadline. *(pause 0.3s)* Maternity: twelve weeks, starting up to four weeks early. *(pause 0.3s)* Exam leave: academic exams only, documents two weeks ahead. *(pause 0.3s)* Scientific: by profession, and can't be carried over. *(pause 0.3s)* Hajj: two years' service and a permit. *(pause 0.3s)* Compassionate: marriage, paternity, bereavement. *(pause 0.3s)* Then Eid, Founding Day, National Day. *(pause 0.3s)* We'll practise the four people ask about most. | 42.4 | `MC03-welcome-on-board_hr-041.mp3` |
| 20 | `hr-042` | omar | encouraging | OMAR: Four grades, four entitlements. Match each grade to its annual leave, in working days. | 6.4 | `MC03-welcome-on-board_hr-042.mp3` |
| 21 | `hr-043` | omar | calm | OMAR: One example, properly. A colleague is off sick forty days in a year, with valid reports. First, she tells her line manager — that's first, not last. *(pause 0.4s)* The first thirty days are paid in full. *(pause 0.4s)* Ten days fall into the next band, and that's where pay drops. *(pause 0.4s)* Note the detail people miss: it's the total in the year that sets the band, not one spell. *(pause 0.5s)* Beyond ninety days it's unpaid. *(pause 0.4s)* And if the report is from outside My Clinic, the Staff Health Clinic must approve it. *(pause 0.4s)* Now: what changes if her report comes from another hospital? | 43.6 | `MC03-welcome-on-board_hr-043.mp3` |
| 22 | `hr-044` | noor | practical | NOOR: Now you're on the other side of the desk. Four colleagues, four questions. First: Yousuf, a lab technician, wants scientific leave and already has the MD's pre-approval. | 12.0 | `MC03-welcome-on-board_hr-044.mp3` |
| 23 | `hr-045` | omar | encouraging | OMAR: A short practice set now. It adapts: if you're getting these, it will finish early. If you're not, it'll keep going for a few more. | 11.1 | `MC03-welcome-on-board_hr-045.mp3` |
| 24 | `hr-050` | omar | calm | OMAR: GOSI is the General Organization for Social Insurance — the government body for social protection in Saudi Arabia. *(pause 0.4s)* It applies to Saudi employees, until retirement at sixty. *(pause 0.4s)* The split matters: you pay nine point seven five per cent of basic plus housing. My Clinic pays eleven point seven five. So the real contribution is twenty-one point five, and most of it isn't yours. | 27.8 | `MC03-welcome-on-board_hr-050.mp3` |
| 25 | `hr-051` | omar | calm | OMAR: Let's do one together. Basic four thousand eight hundred, housing one thousand two hundred. Add them — GOSI is charged on basic plus housing, so six thousand. *(pause 0.4s)* Apply your rate, nine point seven five per cent. The company's rate never touches your payslip. *(pause 0.4s)* Six thousand times nought point nought nine seven five is five hundred and eighty-five riyals a month. That's the line to look for. | 29.1 | `MC03-welcome-on-board_hr-051.mp3` |
| 26 | `hr-052` | omar | encouraging | OMAR: Your turn. Basic six thousand, housing one thousand five hundred. What's your monthly GOSI deduction? | 6.9 | `MC03-welcome-on-board_hr-052.mp3` |
| 27 | `hr-053` | omar | calm | OMAR: One caveat before the numbers: whether you're eligible for overtime at all depends on your grade. Check that first. *(pause 0.4s)* Now the arithmetic. Basic six thousand. Divide by thirty days times eight hours — two hundred and forty hours — and you get twenty-five riyals an hour. *(pause 0.4s)* On a normal working day, multiply by one and a half. That's thirty-seven riyals fifty. *(pause 0.4s)* On a public holiday, multiply by two. Fifty riyals an hour. *(pause 0.4s)* Same hourly rate both times. Only the multiplier moves. | 35.9 | `MC03-welcome-on-board_hr-053.mp3` |
| 28 | `hr-054` | omar | encouraging | OMAR: One for you. Basic six thousand. You work four overtime hours on a normal working day. What's the overtime pay? | 9.0 | `MC03-welcome-on-board_hr-054.mp3` |
| 29 | `hr-060` | omar | practical | OMAR: Six tasks, four systems. Match each one to where it actually happens. Most of them are the same system. | 8.6 | `MC03-welcome-on-board_hr-060.mp3` |
| 30 | `hr-061/omar-1` | omar | practical | OMAR: Let's do it once for real, on a test account. Book yourself a week of annual leave. Five steps, and I'll tell you what to look for. | 12.0 | `MC03-welcome-on-board_hr-061_omar-1.mp3` |
| 31 | `hr-061/omar-tip` | omar | practical | OMAR: One habit worth building. After you submit, open the request again. Wait until it shows as approved before you book any travel. | 9.9 | `MC03-welcome-on-board_hr-061_omar-tip.mp3` |
| 32 | `hr-062` | omar | serious | OMAR: True or false: if your licence expires in under thirty days without renewal, HR may suspend you from work. | 8.6 | `MC03-welcome-on-board_hr-062.mp3` |
| 33 | `hr-070` | omar | practical | OMAR: Two quick things. Your ID card: wear it where it can be seen. *(pause 0.4s)* Lose it, and you email HR — there's a replacement fee. Damage it, and it's replaced free. *(pause 0.4s)* Second, what you can use from day one: health insurance, performance bonuses, development, the hybrid work policy, internal advancement and discounts. Look at the ones you'd actually use. | 25.7 | `MC03-welcome-on-board_hr-070.mp3` |
| 34 | `hr-071` | omar | practical | OMAR: Six dress-code rules, three groups. Put each one where it applies — and pay attention to the one about casual days. | 9.0 | `MC03-welcome-on-board_hr-071.mp3` |
| 35 | `hr-080` | omar | calm | OMAR: Two ends of one story. Starting: you accept your contract on Qiwa, the Ministry of Human Resources platform. *(pause 0.4s)* Leaving: a resignation is a request, so it goes through Oracle. *(pause 0.4s)* Notice is two months, and it runs both ways. *(pause 0.4s)* End-of-service benefits and your experience certificate follow within fifteen days of your last day. | 23.9 | `MC03-welcome-on-board_hr-080.mp3` |
| 36 | `hr-081` | omar | calm | OMAR: Last scenario. You've accepted a new job starting in three weeks. What happens with your notice? | 7.3 | `MC03-welcome-on-board_hr-081.mp3` |
| 37 | `hr-090` | omar | encouraging | OMAR: Here's where you landed, objective by objective. Anything under seventy per cent has a note beside it. It's a list of where to look next, not a verdict. | 12.4 | `MC03-welcome-on-board_hr-090.mp3` |
| 38 | `hr-091/omar-1` | omar | warm | OMAR: That's the induction. You can now live the values, raise a concern the right way, answer leave and pay questions, and pick the right system. *(pause 0.3s)* Download the HR Quick Reference. *(pause 0.3s)* And please complete the onboarding survey. Two minutes, and it shapes how we run this day. | 20.7 | `MC03-welcome-on-board_hr-091_omar-1.mp3` |
| 39 | `hr-091/noor-1` | noor | warm | NOOR: *(pause 0.3s)* Next, you'll join me for clinical governance: quality, patient safety and risk. Welcome to My Clinic. | 7.6 | `MC03-welcome-on-board_hr-091_noor-1.mp3` |
