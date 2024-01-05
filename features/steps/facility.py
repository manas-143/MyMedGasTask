from behave import given, when, then
from playwright.sync_api import expect
import datetime
from Ui_functions import *

user = "robot@mymedgas.com"
Brand = "Class 1 Inc"
Facility = "random_test"
Job_type = "inspection"
product="Other: BeaconMedaes: 8102340981"
locators = {"LOG_IN": "//button[@class='loginBtn btn btn-default']",
            "EMAIL": "//input[@id='email']",
            "PASSWORD": "//input[@id='password']",
            "SIGN-IN BTN": "//button[@id='next' and @type='submit']",
            "ADMIN-TAB": "//div[@title='Admin']/button",
            "USER-TAB":"//a[@title='Users']",
            "BRAND TAB":"//a[@title='Brands']",
            "USER SEARCH TAB":"(//label[text()='search']/following::input)[1]",
            "LOGO": "//div[@class='sk-cube-grid']",
            "LOADING LOGO":"//img[@alt='logo']",
            "NAME SEARCH":"(//div[@class='rt-td' and text()='{}'])[1]",
            "BRAND SELECT": "(//label[text()='Brand']/following::input[@aria-haspopup='true'])[1]",
            "BRAND SEARCH":'//label[text()="Brand"]/following::input[@placeholder="Search by text"]',
            "BRAND ADDRESS": "//label[text()='Address']/following::input[@name='address']",

            "POSTAL CODE": "//input[@name='postal-code']",
            "COUNTRY": "(//input[@name='country'])[2]/parent::div//input[@type='text']",
            "CHECK BOX": "(//div[@class='react-toggle-track'])[1]",
            "SAVE BTN": "//div[@class='form-buttons text-right col-xs-12']//button[@type='submit']",
            "SUCCESS": "//div[text()='Success']",
            "ADD JOB BTN":"//button[@type='submit' and text()='Add Job']",
            "FSE NAME SEARCH":"//label[text()='Name']/following::input[@name='name']",
            "FSE NAME SELECT" :"//li[@class='list-group-item new-product-item']/h4[text()='{}']",
            "FSE JOB NUMBER":"//input[@name='jobnumber']",
            "FSE DROPDOWN BTN":"//div[@class='dropdown btn-group']/child::button",
            "FSE LOG-OUT BTN":"//ul[@role='menu']/descendant::*[@data-icon='sign-out']",
            "CONFIRM LOG-OUT":"//button[text()='Logout']",
            "FSE SAVE BTN":"//button[@type='submit' and text()='save' or text()='Save']",
            "FSE JOB LIST":"//*[@class='modal-title' and text()='New Job']/ancestor::div[@class='modal-content']//label[text()='Type']/parent::div//*[contains(@class,'react-select__control')]",
            "FSE JOB TYPE":"//*[@class='react-select__option css-yt9ioa-option' and text()='Inspection']",
            "FSE SEARCH TAB":"(//label[text()='Search']/parent::div/child::input)[1]",
            "FSE JOB SELECT":"//p[text()='{}']",
            "START JOB":"//a[text()='Start' or text()='Download & Start']",
            "SELECT ALL BOX":"//input[@type='checkbox' and @aria-label='Select row with id:select-all']",
            "ACTION BTN":"//button[@aria-haspopup='true' and text()='actions']",
            "DELETE TAB":"//ul[@role='menu' ]/child::li/child::a[text()='Delete']",
            "DELETE ASSETS":"//div[@class='rrt-buttons-holder' ]/child::button[text()='Delete Assets']",
            "ADD ASSETS" :"//a[text()='Add Asset']",
            "JOB CATEGORY":"(//label[text()='Category']/following::*[text()='Search...']/parent::div)[1]",
            "JOB OPTION":"//div[@class='react-select__option css-yt9ioa-option' and text()='Outlet']",
            "PRODUCT SEARCH":"//input[@name='product-search']",
            "END PRODUCT TOGGLE":"//span[@class='react-toggle-label' and text()='End Product']",
            "PRODUCT":"//div[@class='beacon-list-group list-group']/child::li[1]",
            "QUANTITY":"//input[@name='quantity']",
            "PASS" :"//a[text()='Pass']",
            "CONFIRM PASS":"//Button[text()='Pass Assets']",
            "COMPLETE JOB":"//a[text()='Complete Job']",
            "CUSTOMER NAME":"//div/child::label[text()='Authorized Customer Name']/following-sibling::input",
            "CUSTOMER SIGN" : "//label[text()='Authorized Customer Signature']/following-sibling::div/canvas",
            "SERVICE ENGINEER SIGN" :"//label[text()='Service Engineer Confirmation Signature']/following-sibling::div/canvas",








            }




@given(u'User is on Desktop application')
def logging_in_to_the_website(context):
    context.page.goto("https://mmg-staging-web.azurewebsites.net/")
    context.page.wait_for_load_state()

    with context.page.expect_popup() as popup_info:
        click(context.page, locators["LOG_IN"])
    popup = popup_info.value
    popup.wait_for_load_state()
    send_input(popup, locators["EMAIL"], "robot.mymedgas.uk@gmail.com")
    send_input(popup, locators["PASSWORD"], "MedGas101")
    click(popup, locators["SIGN-IN BTN"])
    popup.close()



@when(u'they navigates to the user section')
def navigating_to_user_section(context):
    context.page.wait_for_load_state()
    element_not_visible(context.page,locators["LOGO"])
    # click(context.page, locators["ADMIN-TAB"])
    # context.page.wait_for_load_state()
    # element_not_visible(context.page,locators["LOGO"])
    # click(context.page,locators["USER-TAB"])
    # context.page.wait_for_load_state()


@when(u'they adds a brand for an existing user')
def adding_a_brand_to_an_user(context):
    # send_input(context.page, locators["USER SEARCH TAB"], user)
    # element_not_visible(context.page,locators["LOGO"])
    # click(context.page, locators["NAME SEARCH"].format(user))
    # element_not_visible(context.page,locators["LOGO"])
    # send_input(context.page,locators["BRAND SELECT"],Brand)
    # context.page.keyboard.press("Enter")
    # element_not_visible(context.page,locators["LOGO"])
    # click(context.page, locators["SAVE BTN"])
    pass



@when(u'they navigates to the brand section')
def navigating_to_brand_tab(context):
    # click(context.page, locators["BRAND TAB"])
    # context.page.wait_for_load_state()
    pass



@when(u'they search and verify the address for the added brand')
def verify_the_address_of_brand(context):
    # send_input(context.page, locators["BRAND SEARCH"], Brand)
    # element_not_visible(context.page,locators["LOGO"])
    # click(context.page, locators["NAME SEARCH"].format(Brand))
    # address = get_value(context.page, locators["BRAND ADDRESS"])
    # print(address)
    pass



@when(u'they navigates to the FSE application')
def logging_in_to_existing_user_FSE_Application(context):
    context.page.goto("https://mmg-staging-offline.azurewebsites.net")
    context.page.wait_for_load_state()
    element_not_visible(context.page,locators["LOGO"])
    click(context.page, locators["LOG_IN"])
    element_not_visible(context.page,locators["LOGO"])
    click(context.page,locators["FSE DROPDOWN BTN"])
    click(context.page,locators["FSE LOG-OUT BTN"])
    click(context.page,locators["CONFIRM LOG-OUT"])
    context.page.wait_for_load_state()
    with context.page.expect_popup() as popup_info:
        click(context.page, locators["LOG_IN"])
    popup = popup_info.value
    popup.wait_for_load_state()
    send_input(popup, locators["EMAIL"], user)
    send_input(popup, locators["PASSWORD"], "MedGas101")
    click(popup, locators["SIGN-IN BTN"])
    popup.close()



@when(u'they create an inspection job for the existing user')
def creating_(context):
    context.page.wait_for_load_state()
    element_not_visible(context.page,locators["LOGO"])
    click(context.page,locators["ADD JOB BTN"])
    send_input(context.page,locators["FSE NAME SEARCH"],Facility)
    element_not_visible(context.page,locators["LOGO"])
    click(context.page,locators["FSE NAME SELECT"].format(Facility))
    job_no= get_value(context.page,locators["FSE JOB NUMBER"])
    click(context.page,locators["FSE JOB LIST"])
    click(context.page,locators["FSE JOB TYPE"])
    click(context.page,locators["FSE SAVE BTN"])
    element_not_visible(context.page, locators["LOGO"])
    send_input(context.page,locators["FSE SEARCH TAB"],job_no)
    click(context.page,locators["FSE JOB SELECT"].format(job_no))
    element_not_visible(context.page, locators["LOGO"])
    click(context.page,locators["START JOB"])
    # element_not_visible(context.page, locators["LOADING LOGO"])
    element_not_visible(context.page, locators["LOGO"])
    try:
        click(context.page, locators["SELECT ALL BOX"])
    except TimeoutError:
        pass
    else:
        click(context.page, locators["ACTION BTN"])
        context.page.wait_for_load_state()
        click(context.page, locators["DELETE TAB"])
        click(context.page, locators["DELETE ASSETS"])
        click(context.page, locators["DELETE ASSETS"])
    click(context.page, locators["ACTION BTN"])
    click(context.page,locators["ADD ASSETS"])
    click(context.page,locators["JOB CATEGORY"])
    click(context.page,locators["JOB OPTION"])
    send_input(context.page,locators["PRODUCT SEARCH"],product)
    click(context.page,locators["END PRODUCT TOGGLE"])
    click(context.page,locators["PRODUCT"])
    click(context.page,locators["QUANTITY"])
    clear_input(context.page,locators["QUANTITY"])
    send_input(context.page,locators["QUANTITY"],"1")
    click(context.page,locators["FSE SAVE BTN"])
    element_not_visible(context.page, locators["LOGO"])
    context.page.wait_for_load_state()


@when(u'they complete the job')
def step_impl(context):
    click(context.page, locators["SELECT ALL BOX"])
    click(context.page, locators["ACTION BTN"])
    context.page.wait_for_load_state()
    click(context.page, locators["PASS"])
    click(context.page, locators["CONFIRM PASS"])
    element_not_visible(context.page, locators["LOGO"])
    context.page.wait_for_load_state()
    click(context.page, locators["ACTION BTN"])
    click(context.page,locators["COMPLETE JOB"])
    send_input(context.page,locators["CUSTOMER NAME"],"TEST AUTO")
    canvas = context.page.locator(locators["CUSTOMER SIGN"])
    # Get the bounding box of the canvas to determine starting and ending points for the line
    canvas_box = canvas.bounding_box()

    # Move the mouse to the starting point of the line
    start_x = canvas_box['x'] + 50  # Replace with the desired starting coordinates
    start_y = canvas_box['y'] + 50
    context.page.mouse.move(start_x, start_y)
    context.page.mouse.down()

    # Move the mouse to the ending point of the line
    end_x = start_x + 100  # Replace with the desired ending coordinates
    end_y = start_y
    context.page.mouse.move(end_x, end_y)
    context.page.mouse.up()





@when(u'they navigate to the desktop application')
def step_impl(context):
    pass


@when(u'download the reports on the report section')
def step_impl(context):
    pass


@then(u'they verify the footer address of the report')
def step_impl(context):
    pass


