# -*- encoding=utf8 -*-
__author__ = "User"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

# 自動連接設備
auto_setup(__file__)

# 初始化 Poco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

def safe_click(resource_id, label, timeout=5):
    """
    封裝點擊函數：等待元件出現後點擊
    """
    print(f"⏳ 正在尋找 {label} ({resource_id})...")
    node = poco(resourceId=resource_id)
    
    if node.wait(timeout).exists():
        node.click()
        print(f"✅ 已點擊 {label}")
        return True
    else:
        print(f"❌ 找不到 {label}，跳過動作")
        return False

def test_id_cycle(times=20):
    # --- 請在此處替換成您實際在 Poco 輔助窗看到的 ID ---
    ID_1 = "tw.com.icash.a.icashpay:id/scan"  # 點擊_1 的 ID
    ID_2 = "tw.com.icash.a.icashpay:id/txt_right"    # 點擊_2 的 ID
    ID_3 = "com.android.permissioncontroller:id/permission_allow_foreground_only_button"                # 點擊_3 (通常是系統彈窗)
    ID_4 = "tw.com.icash.a.icashpay:id/toolbarRightImage"     # 點擊_4 的 ID
    
    for i in range(times):
        print(f"\n--- ⚡ 循環進度: {i+1} / {times} ---")
        
        # 1. 執行 點擊_1
        safe_click(ID_1, "點擊_1")
        sleep(1.0)
        
        # 2. 執行 點擊_2
        safe_click(ID_2, "點擊_2")
        sleep(1.0)
        
        # 3. 判斷 點擊_3 (有跳出才點)
        print("🔍 檢查 點擊_3 彈窗是否出現...")
        target_3 = poco(resourceId=ID_3)
        if target_3.exists():
            print("💡 偵測到點擊_3 彈窗，執行點擊")
            target_3.click()
            sleep(1.0)
        else:
            print("⏩ 點擊_3 未出現，跳過")

        # 4. 執行 點擊_4
        safe_click(ID_4, "點擊_4")
        
        # 5. 緩衝時間
        print(f"🏁 第 {i+1} 次循環完成")
        sleep(2.0)

if __name__ == "__main__":
    test_id_cycle(3)