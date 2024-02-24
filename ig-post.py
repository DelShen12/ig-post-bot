import requests
from datetime import datetime
import pytz
# first post
class Post:
    def __init__(self, text, image_path, tags):
        self.text = text
        self.image_path = image_path
        self.tags = tags

    def upload(self, time):
        if datetime.now(pytz.utc) >= time:
            try:
                with open(self.image_path, 'rb') as image_file:
                    response = requests.post(
                        "http://real-social-media-api.com/post",
                        files = {
                            "image": image_file
                        },
                        data = {
                            "text": self.text,
                            "tags": ','.join(self.tags)
                        }
                    )
                if response.status_code == 200:
                    return "Post uploaded successfully."
                else:
                    return f"Failed to upload post. Status code: {response.status_code}"
            except (FileNotFoundError, requests.RequestException) as e:
                return str(e)
        else:
            return "It's not time yet."

post = Post("Hello, world!", "/real/path/to/image.jpg", ["greetings", "world"])
print(post.upload(datetime(2022, 12, 31, 23, 59, 59, tzinfo=pytz.utc)))