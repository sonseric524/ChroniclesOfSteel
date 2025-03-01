
#### main.py

```python
#!/usr/bin/env python3
import random

swords = [
    "Blade of the Eternal Flame – Forged in dragonfire, this sword burns forever.",
    "Stormbringer – A sword that crackles with lightning, channeling the fury of the skies.",
    "Moonshadow – A dagger that grants invisibility under the full moon.",
    "Soulpiercer – A cursed sword that drains the life force of its wielder.",
    "The Frozen Fang – An icy blade that can shatter steel upon impact."
]

def get_random_sword():
    return random.choice(swords)

def main():
    print("Welcome to Chronicles of Steel!")
    print("Here is a randomly generated legendary sword:")
    print(get_random_sword())

if __name__ == "__main__":
    main()
