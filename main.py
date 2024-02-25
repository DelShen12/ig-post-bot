from textwrap import dedent
from crewai import Crew
import datetime
import pytz
import os

from dotenv import load_dotenv
load_dotenv()

from tasks import CodeTasks
from agents import CodeAgents

tasks = CodeTasks()
agents = CodeAgents()

instruction = dedent("""\
你將創建使用Python的專案，這是指示：
程式名稱

自動發佈 IG 貼文

程式需求

使用者可輸入草稿文字
程式可自動以 LLM 潤飾草稿，主要以吸引人點閱的方式
程式可自動在下午三點整登入使用者的 IG 帳號
程式可自動發佈潤飾後的草稿
程式可自動加上最引人注目的 tag
程式功能

草稿輸入區：使用者可輸入草稿文字
LLM 潤飾：程式可自動以 LLM 潤飾草稿，主要以吸引人點閱的方式
IG 登入：程式可自動登入使用者的 IG 帳號
自動發佈：程式可自動發佈潤飾後的草稿
標籤推薦：程式可推薦最引人注目的 tag
程式介面

主畫面：顯示草稿輸入區、LLM 潤飾、IG 登入、自動發佈等功能
設定畫面：使用者可設定 IG 帳號、發佈時間、標籤推薦等
程式規格

程式語言：Python
開發環境：Google Colab
執行環境：Google Cloud Platform
程式測試

單元測試：測試各個功能是否正常運作
整合測試：測試各個功能是否能整合在一起正常運作
程式部署

將程式部署到 Google Cloud Platform
程式維護

定期更新 LLM 模型
修正程式錯誤
程式使用說明

在草稿輸入區輸入草稿文字
點擊「LLM 潤飾」按鈕，程式會自動以 LLM 潤飾草稿
點擊「IG 登入」按鈕，程式會自動登入使用者的 IG 帳號
點擊「自動發佈」按鈕，程式會自動發佈潤飾後的草稿
程式會自動加上最引人注目的 tag
程式注意事項

使用者需自行準備 IG 帳號
使用者需自行設定發佈時間
使用者需自行設定標籤推薦
""")

# 開始執行時間
start_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S')

# 創建代理人
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# 創建任務
write_code = tasks.code_task(senior_engineer_agent, instruction)
review_code = tasks.review_task(qa_engineer_agent, instruction)
approve_code = tasks.evaluate_task(chief_qa_engineer_agent, instruction)

# 創建Crew
crew_tasks = [write_code, review_code, approve_code]
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=crew_tasks,
	verbose=True
)

result = crew.kickoff()
# 結束執行時間
end_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S')

# 獲取當前工作目錄的路徑
current_directory = os.getcwd()
# 獲取當前工作目錄的名稱
project_name = os.path.basename(current_directory)
# 定義 Markdown 文件的頭部內容
markdown_header = dedent(f"""
# {project_name}
- 開始時間：{start_time}
- 結束時間：{end_time}

## 最終結果
{result}

--------------------------

""")

# 定義每個任務的 Markdown 內容
markdown_tasks = [{"title": t.agent.role, \
    "content": t.output.raw_output} for t in crew_tasks]

# 寫入 Markdown 檔案的功能
markdown_file_name = "記錄verbose.md"
def write_to_markdown(file_name, header, tasks):
    with open(file_name, 'w', encoding='utf-8') as md_file:
        md_file.write(header)
        for task in tasks:
            md_file.write(f"## Title: {task['title']}\n")
            md_file.write(f"- Content: {task['content']}\n\n")

# 將 verbose 寫入到 md 檔中
write_to_markdown(markdown_file_name, markdown_header, markdown_tasks)

# Print results
print("\n\n########################")
print("## CrewAI 產出的結果在此： ##")
print("########################\n")
print("專案最終的源碼：")
print(result)
