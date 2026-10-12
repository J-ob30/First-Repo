"""
iPhone location spoofer.

Makes your iPhone think it is somewhere else, using Apple's built-in
"simulate location" feature for app developers. Runs on your computer
while the iPhone is plugged in with a cable.

How to use: read README.md first, then run:  python3 spoof.py
"""

import subprocess
import sys

# A few ready-made places so you don't have to look up numbers.
FAVORITES = {
    "1": ("Eiffel Tower, Paris", 48.8584, 2.2945),
    "2": ("Times Square, New York", 40.7580, -73.9855),
    "3": ("Shibuya Crossing, Tokyo", 35.6595, 139.7005),
    "4": ("Sydney Opera House", -33.8568, 151.2153),
}


def run(args):
    """Run a pymobiledevice3 command and say whether it worked."""
    print("\nRunning: pymobiledevice3 " + " ".join(args))
    # Use the same Python that started this program, so the right copy of the tool is found.
    result = subprocess.run([sys.executable, "-m", "pymobiledevice3", *args])
    if result.returncode == 0:
        print("Done!")
    else:
        print("That didn't work. Check the 'If something goes wrong' part of README.md.")


def set_location(lat, lon):
    # The "--" stops negative numbers (like -73.9) being read as options.
    run(["developer", "dvt", "simulate-location", "set", "--", str(lat), str(lon)])


def clear_location():
    run(["developer", "dvt", "simulate-location", "clear"])


def ask_number(prompt, low, high):
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
            if low <= value <= high:
                return value
        except ValueError:
            pass
        print(f"Please type a number between {low} and {high}.")


def main():
    try:
        import pymobiledevice3  # noqa: F401  (just checking it's installed)
    except ImportError:
        print("pymobiledevice3 isn't installed for this Python yet. Run:")
        print(f'  "{sys.executable}" -m pip install -U pymobiledevice3')
        sys.exit(1)

    while True:
        print("\n=== iPhone Location Spoofer ===")
        for key, (name, _, _) in FAVORITES.items():
            print(f"  {key}. Go to {name}")
        print("  c. Type in my own place (latitude and longitude)")
        print("  r. Reset - go back to my real location")
        print("  q. Quit")
        choice = input("Pick one: ").strip().lower()

        if choice in FAVORITES:
            name, lat, lon = FAVORITES[choice]
            print(f"Moving your iPhone to {name}...")
            set_location(lat, lon)
        elif choice == "c":
            lat = ask_number("Latitude (between -90 and 90): ", -90, 90)
            lon = ask_number("Longitude (between -180 and 180): ", -180, 180)
            set_location(lat, lon)
        elif choice == "r":
            clear_location()
        elif choice == "q":
            print("Bye! Tip: pick 'r' before quitting if you want your real location back.")
            break
        else:
            print("I didn't understand that - try again.")


if __name__ == "__main__":
    main()
