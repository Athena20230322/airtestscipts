# -*- encoding=utf8 -*-
__author__ = "P10381190"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from poco.exceptions import PocoTargetTimeout

# 1. 初始化環境與 Poco
# 指定 log 保存路徑，這是產生報告的基礎
auto_setup(__file__, logdir=True)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def close_popup():
    """ 通用彈窗關閉函式 """
    print("正在檢查是否有彈窗廣告...")
    close_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/label", text="關閉")
    if close_btn.wait(7).exists():
        print("發現關閉按鈕，執行點擊")
        close_btn.click()
        sleep(1.0)
    else:
        print("未發現關閉按鈕，跳過")

def click_payment_code():
    print("準備點擊付款碼...")
    pay_code_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/nav_home_or_scan")
    if pay_code_btn.wait(5).exists():
        pay_code_btn.click()
        sleep(2.0) 

def click_login_register():
    print("準備點擊 登入/註冊 按鈕...")
    login_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/text", text="登入/註冊")
    if login_btn.wait(5).exists():
        login_btn.click()
        sleep(2.0)

def login_account_info(user_id, user_pwd):
    print(f"開始執行登入流程...")
    # 定位帳號輸入框
    account_input = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/input_text")[0]
    if account_input.wait(5).exists():
        account_input.click()
        text(user_id, enter=True)
    
    # 定位密碼輸入框
    password_input = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/input_text")[1]
    if password_input.exists():
        password_input.click()
        text(user_pwd, enter=True)
    
    # 點擊最終登入按鈕
    final_login_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/login")
    if final_login_btn.exists():
        final_login_btn.click()
        sleep(5.0)

def logout_flow():
    """ 執行登出流程 """
    print("開始執行登出流程...")
    # 點擊我的 (使用 personal_text ID)
    mine_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/personal_text", text="我的")
    if mine_btn.wait(5).exists():
        mine_btn.click()
        sleep(2.0)

    # 點擊設定 (使用 item_name ID)
    setting_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/item_name", text="設定")
    if setting_btn.wait(5).exists():
        setting_btn.click()
        sleep(2.0)

    # 點擊登出
    logout_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/item_name", text="登出")
    if logout_btn.wait(5).exists():
        logout_btn.click()
        sleep(1.0)

    # 點擊確定 (使用 right_text ID)
    confirm_btn = poco(resourceId="tw.com.icash.a.icashpay.debuging:id/right_text", text="確定")
    if confirm_btn.wait(5).exists():
        confirm_btn.click()
        sleep(3.0)

# --- 主執行流程：循環 3 次並加入閃退監控 ---

try:
    for i in range(3):
        print(f"==== 開始第 {i+1} 次測試循環 ====")
        
        # 流程步驟
        close_popup()
        click_payment_code()
        click_login_register()
        login_account_info("tester182", "Aa123456")
        close_popup()
        logout_flow()
        close_popup()
        
        print(f"==== 第 {i+1} 次測試循環成功 ====\n")

except PocoTargetTimeout:
    # 偵測到元件超時，可能是 APP 閃退導致元件消失
    msg = "偵測到異常：元件加載超時，可能發生閃退！"
    print(msg)
    snapshot(msg=msg) # 立即截圖並標註錯誤原因
    raise # 拋出異常讓測試報告顯示失敗

except Exception as e:
    # 捕捉其他未知錯誤
    msg = f"發生非預期錯誤: {e}"
    print(msg)
    snapshot(msg=msg)
    raise

finally:
    # 不論測試成功或失敗，最後自動產生測試報告
    # output 參數指定報告存放的檔案名稱
    print("測試結束，正在產生測試報告...")
    simple_report(__file__, logpath=True, output='icashpay_test_report.html')