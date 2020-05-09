# ResearchGate Crawler

A python spider for crawling <a href="https://www.researchgate.net/">ResearchGate</a> Papers powered by ***Scrapy*** + ***Selenium***

<a href="https://www.researchgate.net/"><img src="http://library.tmu.edu.tw/Upload/File/Form040602/20190318152002552.JPG" width="240" alt="Selenium"/></a>
<a href="https://scrapy.org/"><img src="https://miro.medium.com/max/1400/1*YJNS0JVl7RsVDTmORGZ6xA.png" height="180" alt="Scrapy"/></a>
<a href="https://selenium.dev"><img src="https://selenium.dev/images/selenium_logo_square_green.png" width="180" alt="Selenium"/></a>

## About the project

A small tool that might help grad students tracking up <a href="https://www.researchgate.net/">ResearchGate</a> paper's references.
Since grad students often get overwhelmed by the enormous amount of references when they're trying to trace down a specific research topic, this 
tool tries to assist them leveraging their finite time in reading the most valuable references. By sorting the references in the most-cited 
order, this gives the students a better comprehension of the topic's current research progress and the list of popular papers that they 
might be interested in following up.

## Usage

This will generate an `output-file-name.json` file inside `output` directory containing all scraped items, serialized in JSON.
```JS
scrapy crawl RGSpider -o output/output-file-name.json
```

## Example 

```
[
  {
    "target_title": "Unsupervised Multi-stream Highlight detection for the Game \"Honor of Kings\"",
    "target_link": "https://www.researchgate.net/publication/336551306_Unsupervised_Multi-stream_Highlight_detection_for_the_Game_Honor_of_Kings",
    "target_citation_count": 0,
    "target_reference_count": 15
  },
  {
    "title": "Deep Residual Learning for Image Recognition",
    "link": "https://www.researchgate.net/publication/311609041_Deep_Residual_Learning_for_Image_Recognition",
    "citation_count": 24223,
    "reference_count": 60,
    "date": "Jun 2016",
    "conference": "2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)"
  },
  {
    "title": "ImageNet Classification with Deep Convolutional Neural Networks",
    "link": "https://www.researchgate.net/publication/267960550_ImageNet_Classification_with_Deep_Convolutional_Neural_Networks",
    "citation_count": 20567,
    "reference_count": 34,
    "date": "Jan 2012",
    "conference": null
  },
  {
    "title": "Dropout: A Simple Way to Prevent Neural Networks from Overfitting",
    "link": "https://www.researchgate.net/publication/286794765_Dropout_A_Simple_Way_to_Prevent_Neural_Networks_from_Overfitting",
    "citation_count": 14900,
    "reference_count": 14,
    "date": "Jun 2014",
    "conference": null
  },
  {
    "title": "ImageNet: a Large-Scale Hierarchical Image Database",
    "link": "https://www.researchgate.net/publication/221361415_ImageNet_a_Large-Scale_Hierarchical_Image_Database",
    "citation_count": 14230,
    "reference_count": 27,
    "date": "Jun 2009",
    "conference": "2009 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR 2009), 20-25 June 2009, Miami, Florida, USA"
  },
  {
    "title": "Rectified Linear Units Improve Restricted Boltzmann Machines Vinod Nair",
    "link": "https://www.researchgate.net/publication/221345737_Rectified_Linear_Units_Improve_Restricted_Boltzmann_Machines_Vinod_Nair",
    "citation_count": 7243,
    "reference_count": 23,
    "date": "Jun 2010",
    "conference": "Proceedings of the 27th International Conference on Machine Learning (ICML-10), June 21-24, 2010, Haifa, Israel"
  },
  {
    "title": "Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset",
    "link": "https://www.researchgate.net/publication/317062224_Quo_Vadis_Action_Recognition_A_New_Model_and_the_Kinetics_Dataset",
    "citation_count": 745,
    "reference_count": 35,
    "date": "May 2017",
    "conference": null
  },
  {
    "title": "Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?",
    "link": "https://www.researchgate.net/publication/321325134_Can_Spatiotemporal_3D_CNNs_Retrace_the_History_of_2D_CNNs_and_ImageNet",
    "citation_count": 334,
    "reference_count": 30,
    "date": "Jun 2018",
    "conference": null
  },
  {
    "title": "TVSum: Summarizing web videos using titles",
    "link": "https://www.researchgate.net/publication/308861592_TVSum_Summarizing_web_videos_using_titles",
    "citation_count": 205,
    "reference_count": 55,
    "date": "Jun 2015",
    "conference": "2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)"
  },
  {
    "title": "Highlight Detection with Pairwise Deep Ranking for First-Person Video Summarization",
    "link": "https://www.researchgate.net/publication/311610693_Highlight_Detection_with_Pairwise_Deep_Ranking_for_First-Person_Video_Summarization",
    "citation_count": 133,
    "reference_count": 30,
    "date": "Jun 2016",
    "conference": "2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)"
  },
  {
    "title": "Ranking Domain-Specific Highlights by Analyzing Edited Videos",
    "link": "https://www.researchgate.net/publication/291195077_Ranking_Domain-Specific_Highlights_by_Analyzing_Edited_Videos",
    "citation_count": 85,
    "reference_count": 27,
    "date": "Sep 2014",
    "conference": null
  },
  {
    "title": "Video2GIF: Automatic Generation of Animated GIFs from Video",
    "link": "https://www.researchgate.net/publication/303269216_Video2GIF_Automatic_Generation_of_Animated_GIFs_from_Video",
    "citation_count": 47,
    "reference_count": 53,
    "date": "May 2016",
    "conference": null
  },
  {
    "title": "Deep unsupervised multi-view detection of video game stream highlights",
    "link": "https://www.researchgate.net/publication/327635564_Deep_unsupervised_multi-view_detection_of_video_game_stream_highlights",
    "citation_count": 14,
    "reference_count": 38,
    "date": "Aug 2018",
    "conference": "the 13th International Conference"
  },
  {
    "title": "Video Highlight Prediction Using Audience Chat Reactions",
    "link": "https://www.researchgate.net/publication/318721045_Video_Highlight_Prediction_Using_Audience_Chat_Reactions",
    "citation_count": 8,
    "reference_count": 32,
    "date": "Jul 2017",
    "conference": null
  },
  {
    "title": "Less Is More: Learning Highlight Detection From Video Duration",
    "link": "https://www.researchgate.net/publication/338506484_Less_Is_More_Learning_Highlight_Detection_From_Video_Duration",
    "citation_count": 5,
    "reference_count": 0,
    "date": "Jun 2019",
    "conference": null
  },
  {
    "title": "Transfer learning from speaker verification to multispeaker text-to-speech synthesis",
    "link": null,
    "citation_count": 0,
    "reference_count": 0,
    "date": "Jan 2018",
    "conference": null
  }
]
```

## Known Issues
* Often times that ***Load More button*** did not get triggered normally.
* ***Selenium webDriver*** get blocked when there're some ADs need to be loaded.
* ResearchGate have some duplicated papers, so we might have crawled the same article twice.
