# Set the baseimage
FROM python:3.9.5

# Create folder and change to working directory
WORKDIR /project

# Install cron and nano
RUN apt-get update && apt-get install cron -y nano

# Copy project folder over to container
COPY ./ /project/

# Install python packages
RUN pip install -r requirements.txt

# Copy cron file into cron directory
COPY ./schedule/orchestrate_etl /etc/cron.d/orchestrate_etl

# Give rights to cron file
RUN chmod 0644 /etc/cron.d/orchestrate_etl

# Apply cron job
RUN crontab /etc/cron.d/orchestrate_etl

# Run shell script upon container creation
CMD sh /project/docker/commands.sh

