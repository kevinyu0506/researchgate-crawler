# ResearchGate Crawler

A python spider for crawling <a href="https://www.researchgate.net/">ResearchGate</a> Papers powered by ***Scrapy*** + ***Selenium***

<a href="https://www.researchgate.net/"><img src="http://library.tmu.edu.tw/Upload/File/Form040602/20190318152002552.JPG" width="240" alt="ResearchGate"/></a>
<a href="https://scrapy.org/"><img src="https://miro.medium.com/max/1400/1*YJNS0JVl7RsVDTmORGZ6xA.png" height="180" alt="Scrapy"/></a>
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

## 1. About the project

A small tool that might help grad students tracking up <a href="https://www.researchgate.net/">ResearchGate</a> paper's references.
Since grad students often spent enormous amount of time scanning through all the related references when they're trying to trace down a specific 
research topic, this script tries to reduce and make the best use of their time in reading the most valuable references. By sorting the references 
by their cited count, this gives the students a better comprehension of the topic's current research progress and the list of popular papers in the field 
that they might be interested in following up.

## 2. Getting Started

### Download:
```
$ git clone https://github.com/kevinyu0506/ResearchGate-Crawler.git
```

### Install Packages:
```
$ cd ./RGCrawler
$ pip install -r requirements.txt
```

### Usage:

Users can run the following command to start crawling.
```
$ cd ./RGCrawler
$ scrapy crawl RGSpider -a endpoint=311610693_Highlight_Detection_with_Pairwise_Deep_Ranking_for_First-Person_Video_Summarization -o output/output-file-name.json
```
This will generate an `output-file-name.json` file inside `output` directory containing all scraped items, serialized in JSON.

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

## 3. Known Issues
* Often times that ***Load More button*** did not get triggered normally.
* ~~***Selenium webDriver*** get blocked when there're some ADs need to be loaded.~~ (11/05/2020)
* ResearchGate have some duplicated papers, so we might have crawled the same article twice.
