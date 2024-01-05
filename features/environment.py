from playwright.sync_api import sync_playwright



def before_scenario(context, scenario):
    context.p = sync_playwright().start()
    context.browser = context.p.firefox.launch(headless=False, slow_mo=5000)
    context.tab = context.browser.new_context()
    context.page = context.tab.new_page()


def after_scenario(context, scenario):
    context.page.close()
    context.tab.close()
    context.browser.close()
