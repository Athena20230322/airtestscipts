# -*- encoding=utf8 -*-
__author__ = "Adan"
icashPay_Android_version = "3.0.1.471049"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time

poco("tw.com.icash.a.icashpay.debuging:id/personal_text").click()
poco(text="設定").click()
poco(text="變更登入密碼").click()
poco("tw.com.icash.a.icashpay.debuging:id/oldPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/oldPwdText").set_text("Aa123456")
poco("tw.com.icash.a.icashpay.debuging:id/newPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/newPwdText").set_text("Aa567890")
poco("tw.com.icash.a.icashpay.debuging:id/doubleNewPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/doubleNewPwdText").set_text("Aa567890")
poco("com.android.systemui:id/back").click()
poco("tw.com.icash.a.icashpay.debuging:id/leftButton").click()
poco("tw.com.icash.a.icashpay.debuging:id/txt_right").click()
poco(text="變更登入密碼").click()
poco("tw.com.icash.a.icashpay.debuging:id/oldPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/oldPwdText").set_text("Aa567890")
poco("tw.com.icash.a.icashpay.debuging:id/newPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/newPwdText").set_text("Aa123456")
poco("tw.com.icash.a.icashpay.debuging:id/doubleNewPwdText").click()
poco("tw.com.icash.a.icashpay.debuging:id/doubleNewPwdText").set_text("Aa123456")
poco("com.android.systemui:id/back").click()
poco("tw.com.icash.a.icashpay.debuging:id/leftButton").click()
poco("tw.com.icash.a.icashpay.debuging:id/txt_right").click()
