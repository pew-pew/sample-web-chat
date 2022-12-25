Как попробовать:
- Собрать контейнер - `docker build --tag web-chat .`
- Запустить контейнер - `docker run -p 8000:8000 web-chat`
- Открыть в браузере http://127.0.0.1:8000

Как запустить с горячей перезагрузкой кода:
```
docker run --rm -it -v `pwd`/web_chat:/usr/src/app/web_chat --entrypoint bash -p 8000:8000 web-chat -c "python -m uvicorn web_chat.main:app --host 0.0.0.0 --reload"
```