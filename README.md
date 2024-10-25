
# airtestscipts
# scripts資料夾下

#1.首先執行腳本並保存日誌
# airtest run C:\airtestscipts\scripts\設定變更登入安全密碼.air --log C:\airtestscipts\logs

#2.接著使用報告生成命令
# airtest report C:\airtestscipts\scripts\設定變更登入安全密碼.air --log_root C:\airtestscipts\logs --outfile C:\airtestscipts\reports\report.html

#提高 Airtest 的執行速度，以下是一些優化建議：

#1. 減少圖像比對的時間
 #  - 降低圖像精度：如果在場景允許的情況下，可以調整找圖的精度參數（threshold），讓比對時間更短，但這樣可能會降低成功率。
  # - 預先裁剪圖像：針對需要識別的 UI 元素，預先裁剪出更小的對象範圍，以縮短匹配時間。
   
#2. 加快操作速度
 #  - 使用 Poco 代替圖像識別：如果你的應用支援，Poco 框架比單純的圖像識別快且穩定。這適用於支援 Unity、Android 和 iOS 等基於 UI 標籤識別的場景。
  # - 調整等待時間：減少不必要的 sleep 或等待時間，合理設置腳本中的 wait 參數。
   
#3. 提高測試設備的性能
 #  - 選擇高性能模擬器或真機：如果在模擬器上測試，可以選擇配置較高的模擬器或者硬件加速的真機來提升執行速度。
   
#4. 後台運行模擬器或設備
 #  - 雖然不能完全像 Selenium 的 headless 模式，Airtest 可以配合使用命令行工具或遠程桌面工具，將測試設備和屏幕放置在遠程伺服器上運行，這樣在本地感覺上更像在後台進行。
   
#5. 減少圖像辨識的重複操作
 #  - 你可以將相似步驟的結果緩存起來，避免多次相同的圖像辨識操作。

#儘管 Airtest 不能直接實現像 Selenium 的 headless 模式那樣的後台運行，但通過這些方法可以在一定程度上提升效率，讓腳本運行更快更穩定。

