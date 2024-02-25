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

code = dedent("""\
你將創建使用Python的專案，這是指示：
1. 草稿輸入與潤飾
(1)使用者可以輸入一段草稿給程式。
(2)程式需要有一個LLM（語言模型）來自動潤飾使用者的草稿。
(3)潤飾的目標是使文章更具吸引力，以增加點閱率。
2. 自動登入與發佈
(1)程式需要能夠在指定的時間（例如下午三點整）自動登入使用者的Instagram帳戶。
(2)登入後，程式需要將潤飾過的草稿發佈到Instagram。
3. 標籤生成:程式需要能夠生成引人注目的標籤並加到Instagram的發佈內容中。
4. 使用者介面: 程式需要有一個使用者介面，讓使用者可以輸入草稿，設定發佈時間，以及查看潤飾後的結果和生成的標籤。
5. 錯誤處理: 程式需要能夠處理可能出現的錯誤，例如登入失敗，發佈失敗等，並將錯誤訊息通知給使用者。
""")

# 開始執行時間
start_time = datetime.datetime.now(pytz.timezone('Asia/Taipei')).strftime('%Y-%m-%d %H:%M:%S')

# 創建代理人
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# 創建任務
code_code = tasks.code_task(senior_engineer_agent, code)
review_code = tasks.review_task(qa_engineer_agent, code)
approve_code = tasks.evaluate_task(chief_qa_engineer_agent, code)

# 創建Crew
crew_tasks = [code_code, review_code, approve_code]
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
