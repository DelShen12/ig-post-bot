
# ig-post-bot
- 開始時間：2024-02-28 10:45:12
- 結束時間：2024-02-28 10:46:05

## 最終結果
```python
import streamlit as st
import openai
import instaloader

# 建立使用者介面
st.title("自動發佈 IG 貼文")

# 草稿輸入區
with st.form("草稿輸入區"):
    draft = st.text_area("輸入草稿文字")
    submitted = st.form_submit_button("送出")

# LLM 潤飾
if submitted:
    # 選擇 LLM 模型
    model = st.selectbox("選擇 LLM 模型", ["text-bison-001", "text-bison-002"])

    # 使用 LLM 潤飾草稿
    response = openai.Completion.create(
        model=model,
        prompt=f"潤飾以下草稿，使其更具吸引力：\n{draft}",
        temperature=0.7,
        max_tokens=256
    )
    polished_draft = response["choices"][0]["text"]

    # 顯示潤飾後的草稿
    st.write("潤飾後的草稿：")
    st.write(polished_draft)

# IG 登入
with st.form("IG 登入"):
    username = st.text_input("輸入 IG 帳號")
    password = st.text_input("輸入 IG 密碼", type="password")
    login_submitted = st.form_submit_button("登入")

# 自動發佈
if login_submitted:
    # 登入 IG 帳號
    L = instaloader.Instaloader()
    L.login(username, password)

    # 設定發佈時間
    publish_time = st.datetime_input("選擇發佈時間")

    # 設定標籤推薦
    tags = st.multiselect("選擇標籤推薦", ["#love", "#instagood", "#photooftheday", "#fashion", "#beautiful"])

    # 自動發佈潤飾後的草稿
    L.post(polished_draft, tags, publish_time)

    # 顯示發佈成功訊息
    st.success("貼文已成功發佈！")
```
