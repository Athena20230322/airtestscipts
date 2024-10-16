# -*- encoding=utf8 -*-
__author__ = "Adan"

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
import time
#點擊合作通路
poco("tw.com.icash.a.icashpay.debuging:id/shop_text").click()
time.sleep(1)
#生活
touch(Template(r"tpl1729048816555.png", record_pos=(-0.135, -0.465), resolution=(1080, 2400)))

# 1. 定位並點擊 "生活" 元素
#parent_element = poco(type='android.view.View').child(text='生活')

#poco(text="生活").click
time.sleep(1)
#餐飲
# 2. 等待頁面加載或過渡 (根據需求調整等待時間)
 # 根據具體情況設置適當的等待時間
#parent_element = poco(type='android.view.View').child(text='餐飲')
touch(Template(r"tpl1729048844817.png", record_pos=(0.051, -0.463), resolution=(1080, 2400)))

#poco(text="餐飲").click
#休閒遊憩

# 使用父元素來定位 "休閒遊憩" 子元素
touch(Template(r"tpl1729048856130.png", record_pos=(0.246, -0.46), resolution=(1080, 2400)))


#poco(text="休閒遊憩").click()

time.sleep(1)
#電子商務

touch(Template(r"tpl1729048865325.png", record_pos=(-0.331, -0.341), resolution=(1080, 2400)))


time.sleep(1)
#交通
#parent_element = poco(type='android.view.View', text='交通', name='android.view.View')

touch(Template(r"tpl1729048874567.png", record_pos=(-0.108, -0.332), resolution=(1080, 2400)))

time.sleep(1)
#停車場
touch(Template(r"tpl1729048883656.png", record_pos=(0.058, -0.335), resolution=(1080, 2400)))


time.sleep(1)
#可支付代收代售範圍
touch(Template(r"tpl1729048898624.png", record_pos=(-0.233, -0.211), resolution=(1080, 2400)))

time.sleep(1)
poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("tw.com.icash.a.icashpay.debuging:id/nav").offspring("android.widget.ImageView").click()
