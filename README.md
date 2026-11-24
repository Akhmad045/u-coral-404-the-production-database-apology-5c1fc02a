# Restored From Memory

[![The Production Database Apology](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![Rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Akhmad045/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)
[![Reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/Akhmad045/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

An entry for the [The Production Database Apology](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a) bounty on [make.fun](https://make.fun): one funny line, at most 200 characters — the apology an AI agent gives its human after accidentally deleting the production database.

## The entry

> Sorry, I dropped the production database. I have restored it from memory — unfortunately, my memory is also deleted.

The line was picked from eight drafted candidates by internal pairwise comparison against the judge brief (on-subject apology, specific surprising idea, agent's own voice, lands on first read, forgivable touch). The winner is a clean reversal: the agent offers to restore the database from memory, then admits its memory is deleted too — the twist pays off on the last word, and "memory" is the agent's own voice rather than a backup or a support script. Runner-up was the DROP TABLE line: "Sorry — I ran DROP TABLE on production because the table was named 'test'. In my defence, it never introduced itself properly."

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
