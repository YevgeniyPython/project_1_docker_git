FROM python:3.12-bookworm


COPY app /app


RUN pip install -r /app/requirements.txt


CMD ["python3", "/app/main.py"]
