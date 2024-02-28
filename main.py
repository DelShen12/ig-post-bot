from textwrap import dedent
from crewai import Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
import datetime
import pytz
import os

from dotenv import load_dotenv
load_dotenv()

from crewai_io import write_to_markdown, setup_logging
from tasks import CodeTasks
from agents import CodeAgents

# Initialize the OpenAI GPT-4 language model
GeminiPro = ChatGoogleGenerativeAI(
		model="gemini-pro", 
		verbose=True, 
		temperature=0.1, 
		google_api_key=os.environ.get("GEMINI_API_KEY")
	)

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

# 设置日志
setup_logging()
# 開始執行時間
start_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S')

# 創建代理人
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# 創建任務
write_code = tasks.code_task(senior_engineer_agent, instruction)
review_code = tasks.review_task(qa_engineer_agent, [write_code], instruction)
approve_code = tasks.evaluate_task(chief_qa_engineer_agent, [review_code], instruction)

# 創建Crew
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=[write_code,
		review_code,
		approve_code
	],
    process=Process.hierarchical,
    manager_llm=GeminiPro,
    verbose=2
)

result = crew.kickoff()
# 結束執行時間
end_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S')
# 將結果寫入 Markdown 檔案
write_to_markdown(result, start_time, end_time)

print("######################")
print(result)
