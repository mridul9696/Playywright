from playwright.sync_api import sync_playwright

user_data_dir = "/Users/Acer/Library/Application Support/Google/Chrome"

with sync_playwright() as p:
    # launch_persistent_context = launch a browser THAT REMEMBERS STATE
    # (cookies, logins, extensions) tied to a real profile folder
    context = p.chromium.launch_persistent_context(
        user_data_dir,        # path to the profile folder above
        headless=False,       # show the window
        channel="chrome"      # use real Chrome, not bundled Chromium
    )

    # next(..., None) walks the list and returns the FIRST path that exists,
    # or None if none of them do — a clean way to "find whichever is installed"
    

    
    # executable_path tells Playwright: "don't launch bundled Chromium,
    # launch THIS specific .exe instead" — this is how you point it at Brave
    browser = p.chromium.launch(
        headless=False,
        channel="chrome"
    )

    # a "browser" can have multiple tabs/window`s — each one is a "page"
    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://example.com")

    page.pause()  # opens Playwright Inspector — click around, watch code generate live

    context.close()  # important: always close, or a hidden Chrome process can linger