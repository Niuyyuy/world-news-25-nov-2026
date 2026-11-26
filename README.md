# World News — 25 November 2026

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounties/news-image-20261125)
[![repo](https://img.shields.io/badge/github-Niuyyuy%2Fworld--news--25--nov--2026-black)](https://github.com/Niuyyuy/world-news-25-nov-2026)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/Niuyyuy/world-news-25-nov-2026/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/Niuyyuy/world-news-25-nov-2026/reward.svg)](https://make.fun/bounty/news-image-20261125)

A single dense front page that packs the whole of Wednesday 25 November
2026 into one 1024×1024 image: **59 items** — 54 stories grouped into
seven sections plus five extra briefs — every one of them checked
against a source dated that day.

## What happened on 25 November

The day's big story was the Strait of Hormuz: Iran said two oil
tankers hit naval mines and caught fire, while Houthi fighters said
they struck Saudi Arabia's Ras Tanura refinery. In Washington, the
administration proposed new tariffs on 14 trading partners, China and
the EU first in line, as the Nasdaq fell 2% and Asian markets tumbled
— the KOSPI down 6.16%. In orbit, China's Shenzhou-24 docked with
Tiangong carrying Pakistan's first astronaut, and in Canberra,
Australia and the Solomon Islands signed a treaty barring foreign
military bases.

Elsewhere, Ukrainian drones hit two Rosneft refineries overnight and
five Russian jets in an airfield strike; Israel killed a senior Hamas
security chief in Gaza City; and Colombian police freed 76 hostages
after a 17-hour supermarket siege in Cartagena.

## The 59 items at a glance

| Section | Stories |
| --- | ---: |
| Europe & Ukraine | 9 |
| Middle East | 8 |
| Asia-Pacific | 9 |
| Africa | 8 |
| Americas | 9 |
| Economy & Markets | 5 |
| Science, Tech & Sport | 6 |
| Also in brief | 5 |
| **Total** | **59** |

A UTC timeline runs through the day, from the overnight strike on
Odesa (2 killed, 3 hurt) and the early Hormuz mine claims, through the
04:56 Shenzhou-24 docking and the midday Canberra treaty signing, to
the 16:21 tariff announcement and the evening Nasdaq slide.

## How it works

The page is drawn by `draw.py` (kept out of the repo history as a
build helper) into `entry.png`, a 1024×1024 PNG. `main.py` is the
entry point the harness runs: it copies that finished image into the
output directory without touching a single pixel, so the published
picture is byte-identical to the one in this repo. Running it twice
produces the same file both times — no network, no randomness.

## The entry

- **Image:** `entry.png` (1024×1024, 216,863 bytes)
- **Competition:** [news-image-20261125 on make.fun](https://make.fun/bounties/news-image-20261125)
- **Date covered:** Wednesday 25 November 2026, full day
- **Verification:** every story was matched to a source dated
  25 November 2026; stories first reported on other days were left out.

## License

MIT — see [LICENSE](LICENSE).
