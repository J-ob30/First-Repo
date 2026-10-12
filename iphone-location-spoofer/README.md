# iPhone Location Spoofer

Makes your iPhone 16 Pro think it's somewhere else (for example, Paris).
It uses a feature Apple built in for app makers, so **no jailbreak** (no hacking your phone) is needed.

**You need:** a Windows PC or Mac, your iPhone, and its USB cable.
This must run on *your own computer* — it can't run from the cloud.

---

## One-time setup

1. **Install Python** (a free programming language) from <https://www.python.org/downloads/>.
   On Windows, tick the box **"Add Python to PATH"** during install.
   - Windows only: also install **iTunes** or **Apple Devices** from the Microsoft Store (this lets your PC talk to the iPhone).
2. **Install the helper tool.** Open *Terminal* (Mac) or *Command Prompt* (Windows) and type:
   ```
   python3 -m pip install -U pymobiledevice3
   ```
   (On Windows, use `python` instead of `python3`.)
3. **Plug in your iPhone**, unlock it, and tap **Trust** when it asks.
4. **Turn on Developer Mode** on the iPhone:
   - If you don't see it in Settings yet, run: `pymobiledevice3 amfi reveal-developer-mode`
   - Then on the iPhone: **Settings → Privacy & Security → Developer Mode → On**. The phone restarts; tap **Turn On** afterwards.
5. **Load Apple's developer tools onto the phone** (one command, it downloads them for you):
   ```
   pymobiledevice3 mounter auto-mount
   ```

## Every time you want to use it

1. Plug in and unlock your iPhone.
2. Open a terminal window and start the "connection bridge" (newer iPhones need this). **Leave this window open.**
   - Mac: `sudo pymobiledevice3 remote tunneld` (it asks for your computer password)
   - Windows: open Command Prompt **as Administrator**, then `pymobiledevice3 remote tunneld`
3. Open a **second** terminal window, go to this folder, and run:
   ```
   python3 spoof.py
   ```
4. Pick a place from the menu. Open Apple Maps on your phone to check it worked!
5. To go back to your real location, choose **r** in the menu (restarting the phone also resets it).

## On the go with an iPad (your iPhone stays free)

The idea: your **iPad stays at home** with a fake location, and it becomes the device
that shares your location. Your iPhone goes anywhere and works normally.

**Setting it up (once):**
1. Make sure your iPad is signed into the **same Apple Account** as your iPhone.
2. Do the "One-time setup" steps above, but with the **iPad** plugged in instead of the iPhone
   (tap Trust, turn on Developer Mode on the iPad, run `pymobiledevice3 mounter auto-mount`).
3. On the iPad, open the **Find My** app → **Me** tab → tap **Use this iPad as My Location**.
   Now Messages and Find My show the iPad's location instead of the iPhone's.

**Each day:**
1. Plug the iPad into your computer and **unplug your iPhone** (so the program picks the iPad).
2. Start the bridge window and run `python3 spoof.py` as usual, then pick your place.
3. Leave the iPad plugged in, switched on, and connected to Wi-Fi. Leave the bridge window open too.
4. Take your iPhone and go.

**Important things to know:**
- **Test it first.** Check your location from another device or ask a friend before relying on it.
- If the **iPad restarts, runs out of battery, or loses Wi-Fi**, it may show its real location
  (your home) or "No location found". Keep it charging.
- If you ever tap **Use this iPhone as My Location** on your iPhone, sharing switches back to the iPhone.
- If you want to change the fake place while you're out, you'd need to be at the computer,
  so pick your place before you leave.

## If something goes wrong

- **Windows: "Microsoft Visual C++ 14.0 or greater is required"** → your Python is too new for the tool.
  Install **Python 3.13** from python.org as well, then use `py -3.13` in place of `python` in every command,
  e.g. `py -3.13 -m pip install -U pymobiledevice3` and `py -3.13 spoof.py`.

- **"No device connected"** → unplug and replug, unlock the phone, tap Trust.
- **Errors about "tunnel" or "RSD"** → make sure step 2 (the bridge window) is still running.
- **"Developer disk image" errors** → run `pymobiledevice3 mounter auto-mount` again.
- **Brand-new iOS version** → iOS updates sometimes break this tool until it's updated. Run
  `python3 -m pip install -U pymobiledevice3` to get the newest version.

## Backup option: Mac with Xcode

If you have a Mac, Apple's free **Xcode** app can do this too:
make any small app project, run it on your iPhone, then go to **Debug → Simulate Location → Add GPX File** and pick `paris.gpx` from this folder.
Change the numbers inside `paris.gpx` to go anywhere.

---

**Please use this responsibly.** It's great for testing apps or privacy. Using it to cheat in games
(like Pokémon GO) can get your account banned, and some apps (banking, dating) may stop working properly while it's on.
