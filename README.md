# ResearchGate Crawler

A python crawler for <a href="https://www.researchgate.net/">ResearchGate</a> Papers powered by ***Scrapy*** 

<a href="https://www.researchgate.net/"><img src="http://library.tmu.edu.tw/Upload/File/Form040602/20190318152002552.JPG" width="280" alt="ResearchGate"/></a>
<a href="https://scrapy.org/"><img src="https://miro.medium.com/max/1400/1*YJNS0JVl7RsVDTmORGZ6xA.png" width="280" alt="Scrapy"/></a>

## 1. About the project

A small script that help me tracking up <a href="https://www.researchgate.net/">ResearchGate</a> paper's references.
Since I often spent enormous amount of time scanning through related references when I'm tracing down a specific 
research topic, this script tries to reduce and make the best use of my time in reading the most valuable references (which is defined as more citation counts for now). 

## 2. Getting Started

### Download:
```
$ git clone https://github.com/kevinyu0506/ResearchGate-Crawler.git
```

### Install Packages:
```
$ pip install -r requirements.txt
```

### Usage:

Users can run the following command to start crawling.
```
$ scrapy runspider src/spider.py
```
This will generate an `{paper_to_crawl}.json` file inside `output` directory containing all scraped items, serialized in JSON.

### Output JSON format:

```
{"result": [{
    "title": "Less Is More: Learning Highlight Detection From Video Duration",
    "DOI": "10.1109/CVPR.2019.00135",
    "conference": "Conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
    "citation count": "13",
    "reference count": "40"
},
{
    "reference title": "Highlight Detection with Pairwise Deep Ranking for First-Person Video Summarization",
    "ROI": "10.1109/CVPR.2016.112",
    "conference": "Conference: 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)",
    "citation count": "161"
},
{
    "reference title": "Unsupervised Video Summarization with Adversarial LSTM Networks",
    "ROI": "10.1109/CVPR.2017.318",
    "conference": "Conference: Conference on Computer Vision and Pattern Recognition (CVPR)",
    "citation count": "163"
},
{
    "reference title": "Discovering important people and objects for egocentric video summarization",
    "ROI": "10.1109/CVPR.2012.6247820",
    "conference": "Conference: Computer Vision and Pattern Recognition (CVPR), 2012 IEEE Conference on",
    "citation count": "495"
},...
```
