"""One-line entry for the Worst Pizza Topping bounty on make.fun.

The program prints a single funny line and writes the same line to
/output/entry.txt so the house judge can read it.
"""

# Homework is the one topping that stays awful even when the pizza is good:
# cold, unfinished, and somehow still mandatory.
LINE = "New: pizza topped with homework. It arrives cold, nobody finishes it, and your mum still makes you eat the whole slice."

assert "\n" not in LINE
assert 1 <= len(LINE) <= 200

print(LINE)

try:
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
except OSError:
    pass
