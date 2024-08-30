FROM python:latest
WORKDIR home/mini_note
COPY . home/mini_note
RUN pip install -r home/mini_note/requirements.txt