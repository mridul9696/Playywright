from playwright.sync_api import sync_playwright

# your Chrome profile lives in a folder on your computer.
# this is the DEFAULT location on most systems — you may need to adjust it:
# Windows: C:\Users\<YourName>\AppData\Local\Google\Chrome\User Data
# Mac:     /Users/<YourName>/Library/Application Support/Google/Chrome
# Linux:   /home/<YourName>/.config/google-chrome
user_data_dir = "/Users/Acer/Library/Application Support/Google/Chrome"

with sync_playwright() as p:
    # launch_persistent_context = launch a browser THAT REMEMBERS STATE
    # (cookies, logins, extensions) tied to a real profile folder
    context = p.chromium.launch_persistent_context(
        user_data_dir,        # path to the profile folder above
        headless=False,       # show the window
        channel="chrome"      # use real Chrome, not bundled Chromium
    )

    # note: persistent context already comes with one page open,
    # so we grab it instead of creating a new one
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")

    page.pause()  # inspect / record actions here

    context.close()  # closes the browser