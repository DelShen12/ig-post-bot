
# ig-post-bot
- 開始時間：2024-02-27 16:54:58
- 結束時間：2024-02-27 16:55:29

## 最終結果
```python
import streamlit as st
import openai
import instaloader
import datetime

# 建立使用者介面
st.title("自動發佈 IG 貼文")

# 草稿輸入區
draft_text = st.text_area("草稿文字")

# LLM 潤飾
llm_model = st.selectbox("LLM 模型", ["text-bison-001", "text-bison-002", "text-bison-003"])
潤飾後的草稿 = openai.Completion.create(
    model=llm_model,
    prompt=draft_text,
    temperature=0.7,
    max_tokens=256
)

# IG 登入
ig_username = st.text_input("IG 帳號")
ig_password = st.text_input("IG 密碼", type="password")

# 自動發佈
發佈時間 = st.time_input("發佈時間")
標籤推薦 = st.multiselect("標籤推薦", ["#love", "#instagood", "#photooftheday", "#fashion", "#beautiful"])

# 檢查發佈時間是否在未來
if 發佈時間 < datetime.datetime.now():
    st.error("發佈時間必須在未來")
else:
    # 登入 IG 帳號
    ig_loader = instaloader.Instaloader()
    ig_loader.login(ig_username, ig_password)

    # 發佈貼文
    ig_loader.post(潤飾後的草稿, caption=潤飾後的草稿 + "\n" + " ".join(標籤推薦))

    # 顯示訊息
    st.success("貼文已發佈")
```
