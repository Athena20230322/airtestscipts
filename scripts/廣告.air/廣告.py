# -*- encoding=utf8 -*-
__author__ = "aijinka"

from airtest.core.api import *

auto_setup(__file__)
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
#優惠專區
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/banner_more").child("android.widget.TextView").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_left").click()
#金融服務
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_more").child("android.widget.TextView").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
#金融服務保險
poco("tw.com.icash.a.icashpay.debuging:id/insurance").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_container").child("android.widget.HorizontalScrollView")[1].offspring("tw.com.icash.a.icashpay.debuging:id/financial_item_container").child("android.view.ViewGroup")[0].child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/image").click()
poco(text="立即前往").click()
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
#富邦產險
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_container").child("android.widget.HorizontalScrollView")[1].offspring("tw.com.icash.a.icashpay.debuging:id/financial_item_container").child("android.view.ViewGroup")[1].child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/image").click()
sleep(1.0)
poco(text="立即前往").click()
poco(text="確定前往").click()
poco("com.android.systemui:id/back").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_left").click()
#基金
poco("tw.com.icash.a.icashpay.debuging:id/fund").click()
#信貸
poco("tw.com.icash.a.icashpay.debuging:id/loan").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_container").child("android.widget.HorizontalScrollView")[1].offspring("tw.com.icash.a.icashpay.debuging:id/financial_item_container").child("android.view.ViewGroup")[0].child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/image").click()
poco(text="確定前往").click()
poco("com.android.systemui:id/back").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/financial_container").child("android.widget.HorizontalScrollView")[1].offspring("tw.com.icash.a.icashpay.debuging:id/financial_item_container").child("android.view.ViewGroup")[1].child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/image").click()
poco(text="立即前往").click()
poco("com.android.systemui:id/back").click()
sleep(1.0)

poco(text="確定前往").click()
poco("com.android.systemui:id/back").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_left").click()
#付款點擊
poco("tw.com.icash.a.icashpay.debuging:id/home_text").click()
poco(text="2").click()
poco(text="4").click()
poco(text="6").click()
poco(text="7").click()
poco(text="9").click()
poco(text="0").click()
sleep(2.0)
poco("tw.com.icash.a.icashpay.debuging:id/close").click()
swipe(Template(r"tpl1728371882749.png", record_pos=(0.069, 0.347), resolution=(1080, 2400)), vector=[-0.0483, -0.3676])

#生活優惠
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/coop_more").child("android.widget.TextView").click()
poco("tw.com.icash.a.icashpay.debuging:id/title_left").click()
swipe(Template(r"tpl1728372138324.png", record_pos=(-0.007, 0.364), resolution=(1080, 2400)), vector=[0.0, -0.2389])

#銀行優惠
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/fragment_container").offspring("tw.com.icash.a.icashpay.debuging:id/scroll_view").offspring("tw.com.icash.a.icashpay.debuging:id/home_container").offspring("tw.com.icash.a.icashpay.debuging:id/cash_bank_container").offspring("tw.com.icash.a.icashpay.debuging:id/cashback_more").child("android.widget.TextView").click()
sleep(1.0)
poco("tw.com.icash.a.icashpay.debuging:id/toolbarLeftArrow").click()
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/base_container").offspring("tw.com.icash.a.icashpay.debuging:id/nav").offspring("android.widget.ImageView").click()
poco(text="2").click()
poco(text="4").click()
poco(text="6").click()
poco(text="7").click()
poco(text="9").click()
poco(text="0").click()
poco("tw.com.icash.a.icashpay.debuging:id/close").click()