# -*- encoding=utf8 -*-
__author__ = "User"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 自動連接設備
auto_setup(__file__)

# 初始化 Poco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def safe_click(resource_id, label, timeout=10):
    """
    加強版點擊函數：確保元素存在後執行點擊
    """
    print(f"⏳ 正在尋找 {label} ({resource_id})...")
    node = poco(resourceId=resource_id)
    
    if node.wait(timeout).exists():
        node.click()
        print(f"✅ 已點擊 {label}")
        return True
    else:
        print(f"🔍 ID 找不到 {label}，嘗試文字偵測...")
        backup_node = poco(textMatches=".*(同意|下一步|允許|確定|完成).*")
        if backup_node.exists():
            backup_node.click()
            print(f"✅ 已透過文字點擊 {label}")
            return True
        return False

def test_full_cycle(times=5): # 這裡預設改為 5 次
    # --- ID 定義 ---
    ID_1 = "tw.com.icash.a.icashpay.debuging:id/scan"
    ID_2 = "tw.com.icash.a.icashpay.debuging:id/txt_right"
    ID_3 = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"
    ID_4_NAME = "tw.com.icash.a.icashpay.debuging:id/right_text"
    ID_5 = "tw.com.icash.a.icashpay.debuging:id/picture"
    ID_7_NAME = "android.view.View" 
    ID_8 = "tw.com.icash.a.icashpay.debuging:id/input"
    ID_9 = "tw.com.icash.a.icashpay.debuging:id/btn_next"
    ID_FINISH = "tw.com.icash.a.icashpay.debuging:id/text"
    
    PIN_VALUES = ["2", "4", "6", "7", "9", "0"]
    PIN_BASE_ID = "tw.com.icash.a.icashpay.debuging:id/pin"

    for i in range(times):
        print(f"\n{'='*20}")
        print(f"🚀 流程開始 (第 {i+1} / {times} 次)")
        print(f"{'='*20}")
        
        # 1. 點擊掃碼
        safe_click(ID_1, "點擊_1")
        sleep(1.5)
        
        # 2. 點擊右側文字
        safe_click(ID_2, "點擊_2")
        
        print("⌛ 等待畫面穩定...")
        sleep(3.5) 
        
        # 3. 處理系統權限彈窗
        if poco(resourceId=ID_3).exists():
            poco(resourceId=ID_3).click()
            print("✅ 已點擊系統權限")
            sleep(2.0)

        # 4. 點擊相簿
        safe_click(ID_5, "點擊_5 (進入相簿)")
        sleep(2.5)

        # 5. 執行「同意」按鈕檢查
        print("🔍 執行「同意」按鈕檢查...")
        if poco(text="同意").exists():
            poco(text="同意").click()
            print("✅ 已透過文字點擊「同意」")
        elif poco(resourceId=ID_4_NAME).exists():
            poco(resourceId=ID_4_NAME).click()
            print("✅ 已透過 ID 點擊「同意」")
        else:
            shell("input tap 760 1100") 
            print("✅ 已執行同意按鈕座標點擊")
        
        sleep(2.5)

        # 7. 點擊照片
        print("⏳ 正在選取照片 (ID_7)...")
        photo_target = poco(name=ID_7_NAME, type="android.view.View")
        if photo_target.exists():
            photo_target.click()
            print("✅ 已成功選取照片")
        else:
            touch([150, 410])
            print("✅ 已執行照片座標點擊")
        sleep(3.0)

        # 8. 輸入金額
        print("⌨️ 正在輸入金額: 1")
        input_node = poco(resourceId=ID_8)
        if input_node.wait(5).exists():
            input_node.set_text("1")
            sleep(1.0)
        
        # 9. 點擊下一步
        safe_click(ID_9, "點擊_9 (下一步)")
        sleep(3.0)

        # 10. 密碼輸入
        print("🔐 輸入安全密碼...")
        for idx, val in enumerate(PIN_VALUES):
            target_pin = f"{PIN_BASE_ID}{idx+1}"
            pin_field = poco(resourceId=target_pin)
            if pin_field.wait(3).exists():
                pin_field.set_text(val)
                sleep(0.5)

        # 11. 等待付款成功並點擊「完成」
        print("⌛ 等待付款結果出現...")
        finish_btn = poco(text="完成")
        if finish_btn.wait(15).exists():
            finish_btn.click()
            print("✅ 已點擊「完成」，該次流程結束")
        else:
            if not safe_click(ID_FINISH, "完成按鈕", timeout=5):
                print("⚠️ 找不到完成按鈕，可能已經在初始畫面")

        print(f"🏁 第 {i+1} 次循環完成")
        
        # 額外建議：每次循環完可以稍微多停一下，確保回到主頁面
        sleep(5.0) 

if __name__ == "__main__":
    # 將這裡的參數改為 5 即可執行五次
    test_full_cycle(5)