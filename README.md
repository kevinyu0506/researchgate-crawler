# ResearchGate Crawler

A python spider for crawling <a href="https://www.researchgate.net/">ResearchGate</a> Papers powered by ***Scrapy*** + ***Selenium***

<a href="https://www.researchgate.net/"><img src="http://library.tmu.edu.tw/Upload/File/Form040602/20190318152002552.JPG" width="240" alt="Selenium"/></a>
<a href="https://scrapy.org/"><img src="https://miro.medium.com/max/1400/1*YJNS0JVl7RsVDTmORGZ6xA.png" height="180" alt="Scrapy"/></a>
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

## About the project

A small tool that might help grad students tracking up <a href="https://www.researchgate.net/">ResearchGate</a> paper's references.
Since grad students often get overwhelmed by the enormous amount of references when they're trying to trace down a specific topic, this 
tool tries to assist them to leverage their time in reading the the most valuable references. By sorting the references in the most-cited 
order, this gives the readers a better comprehension of the topic's current research progress and the list of popular papers that they 
might be interested in following up.

## Known Issues
* Often times that ***Load More button*** did not get triggered normally.
* ***Selenium webDriver*** get blocked when there're some ADs need to be loaded.
* ResearchGate have some duplicated papers, so we might have crawled the same article twice.
