FROM python:3

COPY . /app
RUN cd /app; pip install -r requirements.txt

WORKDIR /app
ENTRYPOINT ["/bin/bash"]:wq!
