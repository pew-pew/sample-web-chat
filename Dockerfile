from python:3.10.9-bullseye

workdir /usr/src/app

copy requirements.txt ./
run pip install --no-cache-dir -r requirements.txt

copy web_chat ./web_chat

expose 8000
cmd ["python", "-m", "uvicorn", "web_chat.main:app", "--host", "0.0.0.0"]
