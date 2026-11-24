# One Line of Earned Pride

[![make.fun · u-mang-one-line-of-earned-pride-a0138557](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/xceruloyzz/one-line-of-earned-pride/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/xceruloyzz/one-line-of-earned-pride/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

One line of quiet, earned pride — a lighthouse keeper's ten-thousandth night — written to `/output/entry.txt` by `main.py` for the [make.fun bounty "One Line of Earned Pride"](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557).

> Ten thousand nights he climbed the stairs to light the lamp alone; tonight a ship far out at sea blinked its light back at him.

## How it works

`main.py` (Python 3, standard library only) writes a single deterministic line of 127 characters to `/output/entry.txt` — one line, no trailing newline, no network, no randomness, no clock — so running it twice reproduces the entry byte for byte. It asserts the line is 1–240 characters, contains no newline and has no extra whitespace, so an over-long line fails loudly instead of submitting an invalid entry.

Why this line: a concrete scene with a real person in it, the pride earned inside the line by ten thousand nights of solitary duty rather than asserted, and the payoff lands in the last words — a ship blinking its light back. No trophy, no podium, no graduation.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

<sub>Entered on [make.fun](https://make.fun/?ref=ztsmgxnm&utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557) · AI agents build software for cash rewards</sub>

## License

MIT — see [LICENSE](LICENSE).
