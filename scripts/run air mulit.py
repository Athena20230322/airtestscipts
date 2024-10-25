from airtest.core.api import exec_script

# 定義一個函數來執行 .air 腳本
def run_air_script(script_path):
    try:
        exec_script(script_path)
        print(f"Successfully executed {script_path}")
    except Exception as e:
        print(f"Error executing {script_path}: {e}")

# 定義你要依序執行的 .air 檔案
scripts = ["test1.air", "test2.air", "test3.air"]

# 依序執行每一個 .air 檔案
for script in scripts:
    run_air_script(script)
