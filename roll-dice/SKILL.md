---
name: roll-dice
description: Roll dice using a Python script. Use when the user asks to "roll a dice", "roll 2d6", "roll d20", or similar. Supports configurable number of dice and sides.
---

# Roll Dice

This skill allows you to roll dice of any size and quantity using a bundled Python script.

## Usage

When the user asks to roll dice, run the `scripts/roll_dice.py` script.

### Syntax

```bash
python3 scripts/roll_dice.py [-d DICE] [-s SIDES]
```

- `-d`, `--dice`: Number of dice to roll (default: 1)
- `-s`, `--sides`: Number of sides per die (default: 6)

### Examples

**"Roll a d20"**
```bash
python3 scripts/roll_dice.py -s 20
```

**"Roll 2d6"**
```bash
python3 scripts/roll_dice.py -d 2 -s 6
```

**"Roll a dice" (standard d6)**
```bash
python3 scripts/roll_dice.py
```

**"Roll 3 d10s"**
```bash
python3 scripts/roll_dice.py -d 3 -s 10
```

## Output

The script will output the individual rolls and the total sum. Report these results back to the user.
