# -*- encoding=utf8 -*-
__author__ = "Adan"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
poco(text="繳費稅").click()
poco(text="停車費").click()
#基隆路邊臨時停車費
poco(text="基隆市路邊臨時停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="臺北市路邊臨時停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="新北市路邊臨時停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="桃園市路邊臨時停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="宜蘭縣路邊停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/constraintLayout").click()
poco(text="汽車").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="宜蘭縣路邊停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/dropdown_text").click()
poco(text="機車(含重機)").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="宜蘭縣路邊停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/constraintLayout").click()
poco(text="拖車").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="臺中市停車費").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco("com.android.systemui:id/back").click()
