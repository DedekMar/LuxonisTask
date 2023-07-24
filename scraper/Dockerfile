FROM python:latest
WORKDIR /scraper
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD ["scrapy", "crawl", "sreality_scraper"]