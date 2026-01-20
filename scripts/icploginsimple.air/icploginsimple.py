# -*- encoding=utf8 -*-
__author__ = "Adan"
from airtest.core.android.android import Android
device = Android()
device.use_adb_screen_capture(True)


from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 初始化Airtest和Poco
auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


# 封装常用操作
def click_element(element=None, text=None, sleep_time=1.0):
    """点击元素并等待"""
    if text:  # 如果提供了text參數，嘗試通過文字定位
        poco(text=text).click()
    elif element:  # 如果提供了element參數，通過Poco ID定位
        if isinstance(element, str):
            poco(element).click()
        else:
            element.click()  # 支持直接传入Poco对象
    else:
        raise ValueError("Either 'element' or 'text' must be provided.")
    sleep(sleep_time)



def swipe_screen(start_pos, end_pos, sleep_time=1.0):
    """滑动屏幕"""
    swipe(start_pos, end_pos)
    sleep(sleep_time)


def navigate_back():
    """返回上一页"""
    poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
    sleep(1.0)


# 封装页面操作
class HomePage:
    def __init__(self, poco):
        self.poco = poco

    def click_recharge(self):
        """点击儲值"""
        click_element(text="儲值")

    def click_cash_recharge(self):
        """点击現金儲值"""
        click_element(text="現金儲值")

    def click_add_100(self):
        """点击加100元"""
        click_element("tw.com.icash.a.icashpay.debuging:id/add_100")

    def click_close(self):
        """点击关闭按钮"""
        click_element("tw.com.icash.a.icashpay.debuging:id/close")


class SettingsPage:
    def __init__(self, poco):
        self.poco = poco

    def click_transaction_limit(self):
        """点击交易限額"""
        click_element(text="交易限額")

    def click_authorization_management(self):
        """点击授權扣款管理"""
        click_element(text="授權扣款管理")

    def click_usage_tutorial(self):
        """点击使用教學"""
        click_element(text="使用教學")

    def click_version_history(self):
        """点击版本與登入紀錄"""
        click_element(text="版本與登入紀錄")

    def click_faq(self):
        """点击常見問題"""
        click_element(text="常見問題")

    def click_terms_of_service(self):
        """点击服務條款"""
        click_element(text="服務條款")

    def click_contact_us(self):
        """点击聯絡我們"""
        click_element(text="聯絡我們")


# 初始化页面对象
home_page = HomePage(poco)
settings_page = SettingsPage(poco)

# 主测试流程
def main_test_flow():
    # 儲值相关操作
    home_page.click_recharge()
    home_page.click_cash_recharge()
    home_page.click_add_100()
    home_page.click_close()

    # 设置页面操作
    settings_page.click_transaction_limit()
    navigate_back()
    settings_page.click_authorization_management()
    navigate_back()
    settings_page.click_usage_tutorial()
    navigate_back()
    settings_page.click_version_history()
    navigate_back()
    settings_page.click_faq()
    navigate_back()
    settings_page.click_terms_of_service()
    navigate_back()
    settings_page.click_contact_us()
    navigate_back()

    # 滑动操作
    swipe_screen(
        (500, 1500),  # 起始坐标
        (500, 500)    # 结束坐标
    )

    # 其他操作
    click_element("tw.com.icash.a.icashpay.debuging:id/nav")
    click_element("tw.com.icash.a.icashpay.debuging:id/home_text")
    for number in ["2", "4", "6", "7", "9", "0"]:
        click_element(text=number, sleep_time=0.5)


# 执行测试
if __name__ == "__main__":
    main_test_flow()