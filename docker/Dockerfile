FROM python:3.9.5

WORKDIR /code
ENV PYTHONPATH=/code/src

RUN apt-get update && apt-get install cron -y

ADD ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./ /code/
COPY ./schedule/orchestrate_etl /etc/cron.d/orchestrate_etl

RUN chmod 0644 /etc/cron.d/orchestrate_etl

RUN crontab /etc/cron.d/orchestrate_etl

RUN touch /var/log/cron.log

CMD sh /code/docker/commands.sh

