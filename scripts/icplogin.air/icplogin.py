# -*- encoding=utf8 -*-
__author__ = "P10381190"

from airtest.core.api import *

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
poco("tw.com.icash.a.icashpay.debuging:id/action").click()
sleep(1.0)

poco("tw.com.icash.a.icashpay.debuging:id/et_acct").click()
poco("tw.com.icash.a.icashpay.debuging:id/et_acct").set_text("tester349")
sleep(1.0)
poco("tw.com.icash.a.icashpay.debuging:id/et_pwd").click()
poco("tw.com.icash.a.icashpay.debuging:id/et_pwd").set_text("Aa123456")
poco("tw.com.icash.a.icashpay.debuging:id/bt_login").click()
sleep(2.0)
poco(text="儲值").click()
sleep(2.0)
poco(text="現金儲值").click()
poco("tw.com.icash.a.icashpay.debuging:id/add_100").click()
poco("tw.com.icash.a.icashpay.debuging:id/text").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_left").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_right").click()
poco(text="自帶杯儲值").click()
sleep(1.0)

poco("tw.com.icash.a.icashpay.debuging:id/close").click()
poco(text="中獎發票儲值").click()
sleep(1.0)

poco("tw.com.icash.a.icashpay.debuging:id/close").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_right").click()
poco("tw.com.icash.a.icashpay.debuging:id/fund").click()
poco("tw.com.icash.a.icashpay.debuging:id/loan").click()
poco("tw.com.icash.a.icashpay.debuging:id/personal").click()
poco(text="交易限額").click()
sleep(1.0)

poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco("tw.com.icash.a.icashpay.debuging:id/lvSetting").click()
sleep(1.0)
poco(text="授權扣款管理").click()
sleep(1.0)
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
sleep(1.0)

poco(text="使用教學").click()
sleep(1.0)

poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco(text="版本與登入紀錄").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
sleep(1.0)
poco(text="常見問題").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
sleep(1.0)
poco(text="服務條款").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
sleep(1.0)
poco(text="聯絡我們").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
sleep(1.0)
poco("android.widget.ImageView").click()