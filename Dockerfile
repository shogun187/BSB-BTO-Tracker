# dockerfile, Image, Container

FROM python:3.9

WORKDIR /app


COPY . /app

RUN pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
RUN pip install pymongo
RUN pip install python-telegram-bot

ENV INTERVAL_SCRAPER 5
ENV INTERVAL_DATABASE 10

# Create a single entry script that runs the desired scripts with specified intervals
COPY script.sh /app/script.sh

# Make the entry script executable
RUN chmod +x /app/script.sh

# Run the entry script by default
CMD ["/app/script.sh"]