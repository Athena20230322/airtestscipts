# -*- encoding=utf8 -*-
__author__ = "P10381190"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
import subprocess

# 1. 初始化環境
auto_setup(__file__, logdir=True)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 定義 Package Name
PKG = "tw.com.icash.a.icashpay.debuging"
LAUNCH_TIMES = []  # 存儲每次啟動的時間

def check_crash_log():
    """ 修正 Windows 環境下的 Crash 檢查 (將 grep 改為 findstr) """
    # Windows 使用 findstr /I (忽略大小寫)
    # 這裡搜尋 FATAL EXCEPTION 或 Runtime 錯誤
    cmd = f'adb shell logcat -d *:E | findstr /I "FATAL Exception RuntimeError"'
    try:
        # 使用 shell=True 執行系統指令
        res = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')
        if res.strip():
            print(f"[警告] 偵測到疑似 Crash 日誌：\n{res[:500]}") # 僅顯示前500字避免洗版
            return True
    except subprocess.CalledProcessError:
        # 當 findstr 找不到關鍵字時會回傳非0狀態碼，這在這是正常的
        pass
    except Exception as e:
        print(f"Log 檢查發生錯誤: {e}")
    return False

def close_popup():
    """ 通用彈窗關閉函式 """
    print("正在檢查是否有彈窗廣告...")
    close_btn = poco(resourceId=f"{PKG}:id/label", text="關閉")
    if close_btn.wait(8).exists():
        print("發現關閉按鈕，執行點擊")
        close_btn.click()
        sleep(1.0)
    else:
        print("未發現關閉按鈕，跳過")

def click_payment_code():
    """ 點擊付款碼 """
    print("準備點擊付款碼...")
    pay_code_btn = poco(resourceId=f"{PKG}:id/nav_home_or_scan")
    if pay_code_btn.wait(10).exists():
        pay_code_btn.click()
        sleep(2.0)
    else:
        raise Exception("首頁載入失敗或找不到付款碼按鈕")

def enter_security_password(password_str):
    """ 依序輸入 6 位數密碼 """
    print(f"開始輸入安全密碼...")
    for i in range(len(password_str)):
        pin_id = f"{PKG}:id/pin{i+1}"
        target_cell = poco(resourceId=pin_id)
        if target_cell.wait(5).exists():
            target_cell.set_text(password_str[i])
            sleep(0.5)
        else:
            raise Exception(f"找不到密碼格: {pin_id}")

def close_payment_page():
    """ 點擊右上角 X 關閉支付頁面 """
    print("準備點擊右上角 X 關閉頁面...")
    exit_btn = poco(resourceId=f"{PKG}:id/close")
    if exit_btn.wait(5).exists():
        exit_btn.click()
        sleep(1.0)

def restart_app_with_timer():
    """ 冷啟動 App 並測量時間 """
    print(f"--- 重新啟動 App: {PKG} ---")
    stop_app(PKG)
    sleep(2.0)
    
    start_time = time.time()
    start_app(PKG)
    
    # 等待首頁關鍵元素出現作為啟動完成標誌
    if poco(resourceId=f"{PKG}:id/nav_home_or_scan").wait(20).exists():
        end_time = time.time()
        duration = round(end_time - start_time, 2)
        LAUNCH_TIMES.append(duration)
        print(f"App 啟動耗時: {duration} 秒")
    else:
        print("App 啟動超時，可能發生 Crash 或網路緩慢")

def clear_app_from_background():
    """ 從多工介面滑掉 App """
    print("執行滑掉 App 動作...")
    keyevent("KEYCODE_APP_SWITCH")
    sleep(2.0)
    
    xy = device().get_current_resolution()
    # 向上滑動關閉 App
    swipe((xy[0] * 0.5, xy[1] * 0.8), (xy[0] * 0.5, xy[1] * 0.2), duration=0.5)
    print("App 已從背景移除")
    sleep(1.0)
    home()
    sleep(1.0)

# --- 主程式執行流程 ---
try:
    for i in range(1, 6):
        print(f"\n======== 開始執行第 {i} 次循環 ========")
        
        # 1. 啟動並計時
        if i == 1:
            # 確保第一次也是乾淨啟動
            restart_app_with_timer()
        
        # 2. 檢查啟動後是否有 Crash
        check_crash_log()

        # 3. 處理流程
        close_popup()
        click_payment_code()
        enter_security_password("135790")
        close_payment_page()
        
        # 4. 循環控制
        if i < 5:
            print(f"第 {i} 次完成，執行背景清理並準備下次啟動...")
            clear_app_from_background()
            restart_app_with_timer()
        else:
            print("5 次循環測試已全部完成！")

    # 輸出啟動時間統計
    if LAUNCH_TIMES:
        avg_time = round(sum(LAUNCH_TIMES) / len(LAUNCH_TIMES), 2)
        print(f"\n[測試報告總結]")
        print(f"每次啟動時間: {LAUNCH_TIMES}")
        print(f"平均啟動時間: {avg_time} 秒")

except Exception as e:
    print(f"程式在第 {i} 次循環中發生錯誤: {e}")

finally:
    print("正在產生測試報告...")
    simple_report(__file__, logpath=True, output="log/report.html")
    print("報告已產生：log/report.html")