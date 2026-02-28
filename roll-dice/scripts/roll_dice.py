import argparse
import random
import sys

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls)
    return rolls, total

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Roll some dice.")
    parser.add_argument("-d", "--dice", type=int, default=1, help="Number of dice to roll (default: 1)")
    parser.add_argument("-s", "--sides", type=int, default=6, help="Number of sides per die (default: 6)")

    args = parser.parse_args()

    if args.dice < 1:
        print("Error: Number of dice must be at least 1.", file=sys.stderr)
        sys.exit(1)
    if args.sides < 2:
        print("Error: Number of sides must be at least 2.", file=sys.stderr)
        sys.exit(1)

    rolls, total = roll_dice(args.dice, args.sides)

    print(f"Rolling {args.dice}d{args.sides}...")
    print(f"Result: {rolls}")
    print(f"Total: {total}")