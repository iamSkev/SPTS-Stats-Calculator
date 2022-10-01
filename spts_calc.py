import datetime
import re
from datetime import timedelta

STATS = {"fs": 1, "bt": 1.25, "psy": 1.5}


def _converter(stat) -> int | None:
    suffix_converter = {
        "k": 1_000,
        "m": 1_000_000,
        "b": 1_000_000_000,
        "t": 1_000_000_000_000,
        "qa": 1_000_000_000_000_000
    }
    if re.search("[a-zA-Z]+", stat):
        digit = float((re.sub("[a-zA-Z]+", "", stat)))
        letter = (re.sub("[^a-zA-Z]", "", stat)).lower()
        return (
            float(digit * (suffix_converter.get(letter)))
            if suffix_converter.get(letter) is not None
            else None
        )
    return float(stat)


def _net(message=None, suffix=True) -> int:
    while True:
        if suffix is True:
            print(
                "i'm sorry but you'd have to type that out again since that doesn't look right."
            )
            print(
                "You can either add a suffix to your stat or type it out manually. e.g 69m or 69000000 "
            )
            print(
            """ Here are the suffixes:
                K (Thousand)
                M (Million)
                B (Billion)
                T (Trillion)
                Qa (Quadrillion)
            """
            )
            stat = _converter((input(message)))
            if stat is not None:
                return stat
                break
        else:
            print(
            """ I'm sorry but you'll have to specify which stat you're training between: 
                fs (Fist Strength)
                bt (Body Toughness) 
                psy (Psychic Power)
            """ 
            )
            stat = str(input("What stat are you training? (fs, bt, psy): ")).lower()
            if STATS.get(stat) is not None:
                return stat
                break

print("You can add suffixes to your stats e.g 69m will be the same as 69000000")
goal = _converter((input("How much is your goal?: ")))
if goal is None:
    goal = _net("How much is your goal?: ")
current = _converter(input("How much do you currently have?: "))
if current is None:
    current = _net("How much do you currently have?: ")

per_tick = _converter(input("How much do you get per tick?: "))
if per_tick is None:
    per_tick = _net("How much do you get per tick?: ")
tick_time = str(input("What stat are you training?(fs, bt, psy): ")).lower()
if tick_time not in ('fs', 'bt', 'psy'):
    tick_time = _net(suffix=False)
optimal_time = ((((goal - current) / per_tick) * (STATS.get(tick_time))) / 60) / 60
time = datetime.timedelta(
    hours=optimal_time)
days, hours, minutes = time.days, time.seconds // 3600, (time.seconds % 3600) // 60
print(time.microseconds)
print(
    f"It would take roughly around {time.days} days {hours} hours {minutes} minutes {time.seconds - ((hours*3600)+(minutes*60))} seconds and {time.microseconds/10000} microseconds"
)
input("Press the Enter button to exit. And as always. Quack.")
