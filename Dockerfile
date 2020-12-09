FROM python:3.7.3

WORKDIR /app

COPY ./ .

RUN pip install -r requirements.txt

WORKDIR src/

ENTRYPOINT [ "scrapy", "runspider", "spider.py", "-a" ]

CMD [ "url=https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration" ]

