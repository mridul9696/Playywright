from playwright.sync_api import sync_playwright
import os

# On Windows, Chrome's profile lives here by default.
# os.path.expandvars automatically fills in your actual username for you —
# no need to type "Acer" manually, this grabs it from your system.
user_data_dir = os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data")

with sync_playwright() as p:
    # launch_persistent_context = opens a browser that REMEMBERS your real
    # Chrome profile — cookies, logins, extensions, everything.
    # This is the ONLY browser launch we need. (No separate p.chromium.launch()
    # — that was creating a second, pointless browser before.)
    context = p.chromium.launch_persistent_context(
        user_data_dir,      # path to YOUR Chrome profile folder
        headless=False,     # False = show the window so you can watch it
        channel="chrome"    # use real installed Chrome, not bundled Chromium
    )

    # A persistent context usually opens with one blank tab already.
    # This line says: "use that existing tab if there is one,
    # otherwise create a new one" — just a safety check.
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://google.com")  # navigate to a page

    page.pause()  # opens Playwright Inspector — click around, watch code generate

    context.close()  # ALWAYS close — otherwise a hidden Chrome process can linger in Task Manager