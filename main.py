from textwrap import dedent
from crewai import Crew

from dotenv import load_dotenv
load_dotenv()

from tasks import CodeTasks
from agents import CodeAgents

tasks = CodeTasks()
agents = CodeAgents()

code = dedent("""\
		你將創建使用Python的專案，這是指示：
		1.寫下一段訊息、時間點，在指定時間上傳貼文
		2.可以上傳圖片、文字
		3.可以設定貼文的tag
	""")


# 創建代理人
senior_engineer_agent = agents.senior_engineer_agent()
qa_engineer_agent = agents.qa_engineer_agent()
chief_qa_engineer_agent = agents.chief_qa_engineer_agent()

# 創建任務
code_code = tasks.code_task(senior_engineer_agent, code)
review_code = tasks.review_task(qa_engineer_agent, code)
approve_code = tasks.evaluate_task(chief_qa_engineer_agent, code)

# 創建Crew
crew = Crew(
	agents=[
		senior_engineer_agent,
		qa_engineer_agent,
		chief_qa_engineer_agent
	],
	tasks=[
		code_code,
		review_code,
		approve_code
	],
	verbose=True
)

code = crew.kickoff()


# Print results
print("\n\n########################")
print("## CrewAI 產出的結果在此： ##")
print("########################\n")
print("專案最終的源碼：")
print(code)
