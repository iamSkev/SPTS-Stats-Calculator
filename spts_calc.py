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
        "qa": 1_000_000_000_000_000,
        "qi": 1_000_000_000_000_000_000
    }
    try:
        if re.search("[a-zA-Z]+", stat):
            digit = float((re.sub("[a-zA-Z]+", "", stat)))
            letter = (re.sub("[^a-zA-Z]", "", stat)).lower()
            return (
                float(digit * (suffix_converter.get(letter)))
                if suffix_converter.get(letter) is not None
                else None
            )
    except ValueError:
        return None
    return float(stat)


def _net(message=None, suffix=True, wrong_type=False) -> int | None:
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
            Qi (Quintillion)
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

def _time_checker(time, msg) -> 0:
    return f"{time} {msg+'s' if time > 1 else msg} " if time != 0 else ""

while True:
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
    seconds = time.seconds - ((hours*3600)+(minutes*60))
    print(seconds)
    milliseconds, microseconds = int((time.microseconds/10000)*10), int((((time.microseconds/10000)*10)-(int((time.microseconds/10000)*10)))*1000)
    print(
        f"It would take roughly around {_time_checker(time.days, 'day')}{'and ' if minutes == 0 and hours != 0 else ''}{_time_checker(hours, 'hour')}{'and ' if seconds == 0 and minutes != 0 else ''}{_time_checker(minutes, 'minute')}{'and ' if milliseconds == 0 and seconds != 0 else ''}{_time_checker(seconds, 'second')}{'and ' if microseconds == 0 and milliseconds != 0 else ''}{_time_checker(milliseconds, 'millisecond')}{'and' if microseconds != 0 else ''} {_time_checker(microseconds, 'microsecond')}"
    )
    print("Good Luck. And as always. Quack.")
