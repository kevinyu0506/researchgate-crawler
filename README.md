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
$ cd src/
$ scrapy runspider spider.py -a url=https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration
```
This will generate an `result.json` file inside `output` directory containing all scraped items, serialized in JSON.

### Output JSON format:

```
[
    {
        "title": "Less Is More: Learning Highlight Detection From Video Duration",
        "url": "https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration",
        "date": "June 2019",
        "DOI": "10.1109/CVPR.2019.00135",
        "conference": "Conference: 2019 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)",
        "citation count": 13,
        "reference count": 40,
        "references": [
            {
                "reference title": "Deep Residual Learning for Image Recognition",
                "url": "https://www.researchgate.net/publication/286512696_Deep_Residual_Learning_for_Image_Recognition",
                "date": "December 2015",
                "DOI": null,
                "conference": null,
                "citation count": 29037
            },
            {
                "reference title": "Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?",
                "url": "https://www.researchgate.net/publication/321325134_Can_Spatiotemporal_3D_CNNs_Retrace_the_History_of_2D_CNNs_and_ImageNet",
                "date": "June 2018",
                "DOI": "10.1109/CVPR.2018.00685",
                "conference": "Conference: CVPR2018",
                "citation count": 551
            },
            {
                "reference title": "Discovering important people and objects for egocentric video summarization",
                "url": "https://www.researchgate.net/publication/261303472_Discovering_important_people_and_objects_for_egocentric_video_summarization",
                "date": "June 2012",
                "DOI": "10.1109/CVPR.2012.6247820",
                "conference": "Conference: Computer Vision and Pattern Recognition (CVPR), 2012 IEEE Conference on",
                "citation count": 495
            },...
        ]
    }
]
```
