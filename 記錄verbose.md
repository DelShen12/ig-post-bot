
# ig-post-bot
- 開始時間：2024-02-24 22:09:48
- 結束時間：2024-02-24 22:12:16

## 最終結果
```python
import os
from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import time
import random

# 初始化Instagram API
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")
api = InstagramAPI(username, password)
if not api.login():
    print("Instagram API 登入失敗")
    exit()

# 草稿貼文
draft_post = "這是一個草稿貼文。"

# 添加問句、引號、表情符號
final_post = f'"{draft_post} 🤔😄💡"'

# 建立一個適合的圖片
image = Image.new('RGB', (500, 500), color = (73, 109, 137))
d = ImageDraw.Draw(image)
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d.text((10,10), final_post, font=fnt, fill=(255, 255, 0))

# 儲存圖片
image_name = 'post_image_'+str(time.time())+'.jpg'
try:
    image.save(image_name)
except Exception as e:
    print(f"儲存圖片時發生錯誤: {e}")
    exit()

# 設定標籤
tags = ["#interesting", "#funny", "#insightful"]

# 設定指定時間發布
post_time = time.mktime(time.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
time_diff = post_time - current_time
if time_diff > 0:
    time.sleep(time_diff)
try:
    api.uploadPhoto(image_name, caption = final_post + ' ' + ' '.join(tags))
except Exception as e:
    print(f"上傳圖片時發生錯誤: {e}")
```

--------------------------

## Title: 資深軟體工程師
- Content: ```python
from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import time
import random

# 初始化Instagram API
username = "你的Instagram用戶名"
password = "你的Instagram密碼"
api = InstagramAPI(username, password)
api.login()

# 草稿貼文
draft_post = "這是一個草稿貼文。"

# 添加問句、引號、表情符號
final_post = f'"{draft_post} 🤔😄💡"'

# 建立一個適合的圖片
image = Image.new('RGB', (500, 500), color = (73, 109, 137))
d = ImageDraw.Draw(image)
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d.text((10,10), final_post, font=fnt, fill=(255, 255, 0))

# 儲存圖片
image.save('post_image.jpg')

# 設定標籤
tags = ["#interesting", "#funny", "#insightful"]

# 發布貼文
api.uploadPhoto('post_image.jpg', caption = final_post + ' ' + ' '.join(tags))

# 設定指定時間發布
post_time = time.mktime(time.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
time_diff = post_time - current_time
if time_diff > 0:
    time.sleep(time_diff)
    api.uploadPhoto('post_image.jpg', caption = final_post + ' ' + ' '.join(tags))
```

## Title: 軟體品質控制工程師
- Content: ```python
import os
from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import time
import random

# 初始化Instagram API
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")
api = InstagramAPI(username, password)
api.login()

# 草稿貼文
draft_post = "這是一個草稿貼文。"

# 添加問句、引號、表情符號
final_post = f'"{draft_post} 🤔😄💡"'

# 建立一個適合的圖片
image = Image.new('RGB', (500, 500), color = (73, 109, 137))
d = ImageDraw.Draw(image)
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d.text((10,10), final_post, font=fnt, fill=(255, 255, 0))

# 儲存圖片
image_name = 'post_image_'+str(time.time())+'.jpg'
image.save(image_name)

# 設定標籤
tags = ["#interesting", "#funny", "#insightful"]

# 發布貼文
api.uploadPhoto(image_name, caption = final_post + ' ' + ' '.join(tags))

# 設定指定時間發布
post_time = time.mktime(time.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
time_diff = post_time - current_time
if time_diff > 0:
    time.sleep(time_diff)
    api.uploadPhoto(image_name, caption = final_post + ' ' + ' '.join(tags))
```

## Title: 首席軟體品質控制工程師
- Content: ```python
import os
from InstagramAPI import InstagramAPI
from PIL import Image, ImageDraw, ImageFont
import time
import random

# 初始化Instagram API
username = os.getenv("INSTAGRAM_USERNAME")
password = os.getenv("INSTAGRAM_PASSWORD")
api = InstagramAPI(username, password)
if not api.login():
    print("Instagram API 登入失敗")
    exit()

# 草稿貼文
draft_post = "這是一個草稿貼文。"

# 添加問句、引號、表情符號
final_post = f'"{draft_post} 🤔😄💡"'

# 建立一個適合的圖片
image = Image.new('RGB', (500, 500), color = (73, 109, 137))
d = ImageDraw.Draw(image)
fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', 15)
d.text((10,10), final_post, font=fnt, fill=(255, 255, 0))

# 儲存圖片
image_name = 'post_image_'+str(time.time())+'.jpg'
try:
    image.save(image_name)
except Exception as e:
    print(f"儲存圖片時發生錯誤: {e}")
    exit()

# 設定標籤
tags = ["#interesting", "#funny", "#insightful"]

# 設定指定時間發布
post_time = time.mktime(time.strptime("2022-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))
current_time = time.time()
time_diff = post_time - current_time
if time_diff > 0:
    time.sleep(time_diff)
try:
    api.uploadPhoto(image_name, caption = final_post + ' ' + ' '.join(tags))
except Exception as e:
    print(f"上傳圖片時發生錯誤: {e}")
```

