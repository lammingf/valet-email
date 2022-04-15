
FROM python:3.10.4-slim-bullseye

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y cron offlineimap3 ca-certificates notmuch afew lieer bogofilter
RUN useradd -u 5000 -ms /bin/bash imapuser

USER imapuser

RUN mkdir ~/.bogofilter && chown imapuser:imapuser ~/.bogofilter
COPY ./app /app
RUN pip install -r /app/M365-IMAP/requirements.txt
RUN pip install -r /app/requirements.txt

VOLUME [ "/maildir" ] #mailstorage
VOLUME [ "/conf" ] #config files
VOLUME [ "/app" ] #app code

WORKDIR /app

CMD ["./entrypoint.sh"]
