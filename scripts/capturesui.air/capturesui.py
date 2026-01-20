# -*- encoding=utf8 -*-
__author__ = "P10381190"

from airtest.core.api import *
from airtest.report.report import simple_report
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import time
import subprocess
import os

# 1. 初始化環境 - 使用最相容的設定方式
# logdir 設定為 True，Airtest 會自動在腳本目錄下建立 log 資料夾
auto_setup(__file__, logdir=True)

# 初始化 Poco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# 定義 Package Name
PKG = "tw.com.icash.a.icashpay.debuging"
LAUNCH_TIMES = []

def capture_ui_status(step_name):
    """ 
    專為相容性設計的截圖：直接存入 Airtest 預設的 log 目錄
    """
    # 獲取 Airtest 自動定義的 log 路徑，若無則用當前目錄
    log_path = ST.LOG_DIR if ST.LOG_DIR else "log"
    if not os.path.exists(log_path):
        os.makedirs(log_path)
        
    disp = device().display_info
    w, h = disp['width'], disp['height']
    
    # 建立檔名：UI_步驟名_解析度_時間戳.png
    filename = f"UI_{step_name}_{w}x{h}_{int(time.time())}.png"
    filepath = os.path.join(log_path, filename)
    
    print(f"執行相容性截圖: {filename}")
    # 使用 snapshot 記錄到報告中，並指定存檔路徑
    snapshot(filename=filepath, msg=f"螢幕比例檢查: {step_name} ({w}x{h})")

def check_crash_log():
    """ 檢查 Windows 環境下的 Crash Log """
    # 使用 findstr 替代 grep
    cmd = f'adb shell logcat -d *:E | findstr /I "FATAL Exception RuntimeError"'
    try:
        res = subprocess.check_output(cmd, shell=True).decode('utf-8', errors='ignore')
        if res.strip():
            print(f"[警告] 偵測到系統錯誤日誌")
            return True
    except:
        # findstr 找不到內容時會拋出異常，直接跳過即可
        pass
    return False

def click_payment_code_with_check():
    """ 點擊付款碼並進行 UI 相容性位置分析 """
    print("正在尋找付款碼按鈕...")
    pay_code_btn = poco(resourceId=f"{PKG}:id/nav_home_or_scan")
    
    if pay_code_btn.wait(10).exists():
        # 取得相對位置 (0~1)
        pos = pay_code_btn.get_position()
        print(f"按鈕中心點位置: {pos}")
        
        # 邏輯判斷：如果 y 座標大於 0.9，代表按鈕在螢幕最下方 10% 區域
        if pos[1] > 0.92:
            print(f"!!! 警告：按鈕位置 y={pos[1]} 過低，可能被導覽列遮擋 !!!")
            
        capture_ui_status("PayCode_Position_Check")
        pay_code_btn.click()
        sleep(2.0)
    else:
        capture_ui_status("Error_NotFound_PayCode")
        raise Exception("找不到付款碼按鈕，請檢查 App 是否正常啟動")

def restart_app_logic():
    """ 完整重啟流程：停止 -> 啟動 -> 計時 """
    print(f"--- 執行冷啟動: {PKG} ---")
    stop_app(PKG)
    sleep(2.0)
    
    start_time = time.time()
    start_app(PKG)
    
    # 以首頁按鈕出現作為啟動完成標籤
    if poco(resourceId=f"{PKG}:id/nav_home_or_scan").wait(20).exists():
        duration = round(time.time() - start_time, 2)
        LAUNCH_TIMES.append(duration)
        print(f"啟動完成，耗時 {duration} 秒")
    else:
        print("啟動超過 20 秒未回應")

# --- 主程式執行流程 ---
try:
    for i in range(1, 6):
        print(f"\n======== 開始執行第 {i} 次循環 ========")
        
        # 1. 確保 App 啟動
        if i == 1:
            restart_app_logic()
        
        # 2. 監控異常
        check_crash_log()
        
        # 3. 執行核心業務邏輯與 UI 檢查
        click_payment_code_with_check()
        
        # (此處可自由加入：輸入密碼 enter_security_password)
        
        # 4. 準備下一次循環
        if i < 5:
            print(f"第 {i} 次測試完成，準備重啟...")
            # 模擬手勢滑掉 App 確保冷啟動環境
            keyevent("KEYCODE_APP_SWITCH")
            sleep(1.5)
            # 根據螢幕解析度向上滑動
            w, h = device().get_current_resolution()
            swipe((w * 0.5, h * 0.8), (w * 0.5, h * 0.2), duration=0.5)
            home()
            sleep(1.0)
            restart_app_logic()
        else:
            print("所有測試循環已完成！")

    # 顯示最終統計
    if LAUNCH_TIMES:
        print(f"\n[啟動時間統計] 平均: {sum(LAUNCH_TIMES)/len(LAUNCH_TIMES):.2f}s | 詳細: {LAUNCH_TIMES}")

except Exception as e:
    print(f"程式中斷於第 {i} 次循環，錯誤原因: {e}")

finally:
    print("正在產生測試報告...")
    # 指定 logpath=True 會讓報告抓取剛剛 snapshot 存下來的圖片
    simple_report(__file__, logpath=True, output="log/report.html")
    print("報告已產生，請查看 log/report.html")