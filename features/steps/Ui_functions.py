from playwright.sync_api import expect


def send_input(page, selector, search_item):  # function for sending input to  search box
    page.locator(selector).fill(search_item)


def click(page, selector):  # click function to perform click
    page.locator(selector).click()


def title(page):  # function for getting the title of webpage
    return page.title


def get_url(page):  # function for getting the url of  current webpage
    return page.url


def scroll(page):  # function for getting to the end
    page.keyboard.press('End')


def get_text(page, selector):  # function for getting the text content
    text = page.locator(selector).text_content()
    return text


def count(page, selector):
    value = page.locator(selector).count()
    return value


def clear_input(page, selector):
    page.locator(selector).clear()


def get_value(page, selector):
    value=page.locator(selector)
    return value.input_value()

def element_not_visible(page,selector,max_iterations=5):
    for iteration in range(max_iterations):
        try:
            expect(page.locator(selector)).not_to_be_visible(timeout=50000)
            # If the element is visible, break out of the loop
            break
        except TimeoutError:
            pass
        except Exception as e:
            pass

        # Optional: You can add a delay between iterations if needed
        page.wait_for_timeout(2000)  # 2 seconds delay (adjust as needed)
    else:
        pass
