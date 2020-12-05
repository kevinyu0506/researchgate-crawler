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
$ scrapy runspider spider.py
```
This will generate an `result.json` file inside `output` directory containing all scraped items, serialized in JSON.

### Output JSON format:

```
[
    {
        "title": "Attention-based Deep Multiple Instance Learning",
        "url": "https://www.researchgate.net/publication/323165042_Attention-based_Deep_Multiple_Instance_Learning",
        "DOI": null,
        "conference": null,
        "citation count": 148,
        "reference count": 43,
        "references": [
            {
                "reference title": "Adam: A Method for Stochastic Optimization",
                "url": "https://www.researchgate.net/publication/269935079_Adam_A_Method_for_Stochastic_Optimization",
                "DOI": null,
                "conference": null,
                "citation count": 36235
            },
            {
                "reference title": "Gradient-Based Learning Applied to Document Recognition",
                "url": "https://www.researchgate.net/publication/2985446_Gradient-Based_Learning_Applied_to_Document_Recognition",
                "DOI": "10.1109/5.726791",
                "conference": null,
                "citation count": 20853
            },
            {
                "reference title": "Neural Machine Translation by Jointly Learning to Align and Translate",
                "url": "https://www.researchgate.net/publication/265252627_Neural_Machine_Translation_by_Jointly_Learning_to_Align_and_Translate",
                "DOI": null,
                "conference": null,
                "citation count": 9174
            },...
        ]
    }
]
```
