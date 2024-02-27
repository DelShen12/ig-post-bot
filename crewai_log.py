# crewai_log.py
import os

def write_to_markdown(result, start_time, end_time):
    # 獲取當前工作目錄的路徑
    current_directory = os.getcwd()
    # 獲取當前工作目錄的名稱
    project_name = os.path.basename(current_directory)
    # 定義 Markdown 文件的頭部內容
    markdown_header = (f"""
# {project_name}
- 開始時間：{start_time}
- 結束時間：{end_time}

## 最終結果
{result}
"""
).replace('\t', '')

    # 寫入 Markdown 檔案的功能
    markdown_file_name = "result.md"
    with open(markdown_file_name, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown_header)


import sys
import logging
from logging.handlers import RotatingFileHandler
import datetime


class LoggerWriter:
    def __init__(self, level):
        # 初始化 LoggerWriter 並設置其日誌級別
        self.level = level

    def write(self, message):
        # 如果消息不為空，則寫入日誌
        if message.rstrip() != "":
            logging.log(self.level, message.rstrip())

    def flush(self):
        # 此 flush 方法是為了滿足 file-like 對象的需求
        pass


def setup_logging():
    # 創建一個日誌器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 設置日誌格式
    log_format = logging.Formatter('%(message)s')

    # 創建一個流處理器，將日誌輸出到終端
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_format)
    logger.addHandler(stream_handler)

    # 創建一個文件處理器，用於將日誌寫入到文件 "run.log"，追加模式
    file_handler = RotatingFileHandler('run.log', mode='a', maxBytes=5*1024*1024, backupCount=2, encoding=None, delay=0)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    # 在日誌文件中添加分割線和當前執行時間
    separator = '\n' + '=' * 50 + '\n'
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    logging.info(separator + 'Execution Time: ' + current_time + '\n')

    # 將 sys.stdout 和 sys.stderr 重定向到日誌
    sys.stdout = LoggerWriter(logging.INFO)
    sys.stderr = LoggerWriter(logging.ERROR)

# 注意：此函數應在主腳本開始處調用，以配置日誌系統
