
# ig-post-bot
- 開始時間：2024-02-28 14:11:30
- 結束時間：2024-02-28 14:12:34

## 最終結果
```python
import os
import time
import instaloader
import openai
import schedule

# OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Instagram login credentials
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

# Time to post (in 24-hour format)
POST_TIME = os.getenv("POST_TIME")

# Load the LLM model
model = openai.Model("text-davinci-003")

# Function to generate a caption using LLM
def generate_caption(text):
    response = model.generate(
        prompt=f"Generate an engaging and attention-grabbing caption for the following text: {text}",
        max_tokens=64,
        temperature=0.7,
    )
    return response["candidates"][0]["output"]

# Function to post to Instagram
def post_to_instagram(image_path, caption):
    # Login to Instagram
    L = instaloader.Instaloader()
    L.login(IG_USERNAME, IG_PASSWORD)

    # Upload the image and post the caption
    L.upload_photo(image_path, caption=caption)

# Function to schedule the post
def schedule_post(image_path, caption):
    # Schedule the post to be published at the specified time
    schedule.every().day.at(POST_TIME).do(post_to_instagram, image_path, caption)

    # Start the scheduler
    while True:
        schedule.run_pending()
        time.sleep(1)

# Main function
def main():
    # Get the user input
    text = input("Enter the text you want to post: ")

    # Generate a caption using LLM
    caption = generate_caption(text)

    # Schedule the post
    schedule_post("image.jpg", caption)

# Run the main function
if __name__ == "__main__":
    main()
```
