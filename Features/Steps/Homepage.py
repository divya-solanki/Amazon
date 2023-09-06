from behave import *
from Pages.TodaysDeal import TodaysDeal
from Pages.MobileTab import MobileTab
from time import sleep



@given(u'I open Amazon HomePage')
def step_impl(context):
    context.driver.get('https://www.amazon.in/')




@then(u'Navigate to todays deal tab')
def step_impl(context):
    context.todaysDeal = TodaysDeal(context.driver)
    context.todaysDeal.navigate_to_todays_deal_tab()



@then(u'I select the item')
def step_impl(context):
    context.todaysDeal.select_item_from_the_list()


@then(u'Add it to the cart')
def step_impl(context):
    context.todaysDeal.add_item_to_cart()
    context.todaysDeal.verify_item_added_to_cart()
    sleep(5)

@then(u'Navigate to Mobiles Tab')
def step_impl(context):
    context.mobileTab = MobileTab(context.driver)
    context.mobileTab.navigate_to_mobile_tab()


@then(u'Select a mobile')
def step_impl(context):
    context.mobileTab.select_mobile_from_list()


@then(u'hover the cursor to to show enlarged image of it')
def step_impl(context):
    context.mobileTab.mouse_over_image()
    sleep(3)


@then(u'verify the zoomed image.')
def step_impl(context):
    context.mobileTab.verify_image()

