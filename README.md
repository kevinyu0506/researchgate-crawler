# ResearchGate Crawler

A python crawler for <a href="https://www.researchgate.net/">ResearchGate</a> Papers powered by ***Scrapy*** 

<a href="https://www.researchgate.net/"><img src="http://library.tmu.edu.tw/Upload/File/Form040602/20190318152002552.JPG" width="280" alt="ResearchGate"/></a>
<a href="https://scrapy.org/"><img src="https://miro.medium.com/max/1400/1*YJNS0JVl7RsVDTmORGZ6xA.png" width="280" alt="Scrapy"/></a>

## 1. About the project

A small script that help me tracking up <a href="https://www.researchgate.net/">ResearchGate</a> paper's references.
Since I often spent enormous amount of time scanning through all the related references when i'm tracing down a specific 
research topic, this script tries to reduce and make the best use of my time in reading the most valuable references (which has more citation counts). 

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
$ cd src/
$ scrapy runspider spider.py
```
This will generate an `{target_paper_to_crawl}.json` file inside `output` directory containing all scraped items, serialized in JSON.

### Output JSON format:

```
{
    # 論文標題
    "target_title": "Highlight Detection with Pairwise Deep Ranking for First-Person Video Summarization",
    # 連結
    "target_link": "https://www.researchgate.net/publication/311610693_Highlight_Detection_with_Pairwise_Deep_Ranking_for_First-Person_Video_Summarization",
    # 被引用次數
    "target_citation_count": 133,
    # 引用文獻總數
    "target_reference_count": 30
},
{
    # 最高被引用次數之引用文獻標題
    "title": "Imagenet classification with deep convolutional neural networks",
    # 連結
    "link": "https://www.researchgate.net/publication/319770183_Imagenet_classification_with_deep_convolutional_neural_networks",
    # 被引用次數
    "citation_count": 34361,
    # 引用文獻總數（可能讀取不到）
    "reference_count": 0,
    # 發表日期
    "date": "Jan 2012",
    # 發佈之研討會
    "conference": "NIPS",
    # 索引
    "id": 1
},
{
    # 第二高被引用次數之引用文獻標題
    "title": "ImageNet Classification with Deep Convolutional Neural Networks",
    "link": "https://www.researchgate.net/publication/267960550_ImageNet_Classification_with_Deep_Convolutional_Neural_Networks",
    "citation_count": 20863,
    "reference_count": 34,
    "date": "Jan 2012",
    "conference": null,
    "id": 2
},
{
    # 第三高被引用次數之引用文獻標題
    "title": "ImageNet: a Large-Scale Hierarchical Image Database",
    "link": "https://www.researchgate.net/publication/221361415_ImageNet_a_Large-Scale_Hierarchical_Image_Database",
    "citation_count": 14560,
    "reference_count": 34,
    "date": "Jun 2009",
    "conference": "2009 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2009), 20-25 June 2009, Miami, Florida, USA",
    "id": 3
},...
```
