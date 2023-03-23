# 讀取檔案
with open('hw2_data.txt', 'r') as file:
    # 建立空字典紀錄每個單字出現次數
    word_count = {}
    # 逐行讀取檔案
    for line in file:
        # 將每行轉為小寫並移除換行符號
        words = line.lower().strip().split()
        for word in words:
            # 若字典中沒有該單字，則新增一個key-value pair，value為1
            if word not in word_count:
                word_count[word] = 1
            # 若字典中已經有該單字，則value加1
            else:
                word_count[word] += 1

    # 統計不重複的英文字
    unique_words = len(word_count)
    print(f"總共有 {unique_words} 個不重複的英文字")
    # 統計每個英文字出現次數和
    print(word_count)
    
