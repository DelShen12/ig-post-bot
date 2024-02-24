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
		* 寫下一段草稿、時間點，在指定時間上傳IG
		* 使用問句、引號、表情符號等方式，修改草稿成為'貼文'並使貼文有趣
		* 使用類似 graphic_art 的工具，根據'貼文'生成一張適合的圖片
		* 根據'貼文'性質設定貼文最吸引目光的tag
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
