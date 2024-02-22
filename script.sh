#!/bin/bash

# Run Scraper.py every 5 minutes
while true; do
    python Scraper.py
    sleep $(( $INTERVAL_SCRAPER * 60 ))
done &

# Run database.py every 10 minutes
while true; do
    python database.py
    sleep $(( $INTERVAL_DATABASE * 60 ))
done &

# Run chatbot2.py indefinitely
python chatbot2.py