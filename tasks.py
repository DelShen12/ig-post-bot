from textwrap import dedent
from crewai import Task

class CodeTasks():
	def code_task(self, agent, code):
		return Task(description=dedent(f"""
				你將使用Python創建一段程式碼，以下是指令:

				指令：
				------------
				{code}

				你的中間決策過程將以繁體中文顯示並記錄下來，以用於評估你的工作。
				你的最終答案必須是完整的Python程式碼，只有Python程式碼，除此之外，一無所有。
			""").replace('\t', ''),
			async_execution=True,
			agent=agent
		)

	def review_task(self, agent, context, code):
		return Task(description=dedent(f"""\
				你正在協助使用Python創建一段程式碼，以下是指令：

				指令：
				------------
				{code}

				使用你得到的程式碼，檢查是否有錯誤。檢查邏輯錯誤，
                語法錯誤，缺失的導入，變量聲明，不匹配的括號，
                以及安全漏洞。

				你的中間決策過程將以繁體中文顯示並記錄下來，以用於評估你的工作。
				你的最終答案必須是完整的Python程式碼，只有Python程式碼，除此之外，一無所有。
			""").replace('\t', ''),
            context=context,
			async_execution=True,
			agent=agent
		)

	def evaluate_task(self, agent, context, code):
		return Task(description=dedent(f"""\
				你正在協助使用Python創建一段程式碼，以下是指令：

				指令：
				------------
				{code}

				你將檢查程式碼以確保它是完整的，並且能完成它應該做的工作。

				你的中間決策過程將以繁體中文顯示並記錄下來，以用於評估你的工作。
				你的最終答案必須是完整的Python程式碼，只有Python程式碼，除此之外，一無所有。
			""").replace('\t', ''),
			context=context,
			agent=agent
		)