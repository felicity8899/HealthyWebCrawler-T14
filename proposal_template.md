# HealthyWebCrawler-T14
* Team Slack: 
* Team Trello: 

## Description
* Create a Scrapy project to crawl the content in the Xiaomi Appstore homepage (http://app.mi.com/)
* Save the crawled content in MongoDB
* Crawl more content by following next page links

## Plan

### Todo List
- [ ] Crawl list page
  - [ ] list page html breakdown  
  - [ ] disctinguish sections
  - [ ] decide tags to grap 
- [ ] Crawl app detail page
- [ ] Crawl "more" page of the list 
  - [ ] Splash + ScrapyJS if page link is written in Javascript
- [ ] Pipeline for outputing to MongoDB while crawling
- [ ] Display raw results (front end)
- [ ] More summerized results (recommender)
  - [ ] Top lists
  - [ ] 精品推荐
  - [ ] 热门应用
  - [ ] More ideas
  

### Time Schedule

| Stage | Start  | End | Goals |
| ------------- | ------------- | ------------- | ------------- |
| 1 | 06/06/16  | 06/08/16  | Project Selection, Plan Discussion, and Proposal Draft Writing |
| 2 | 06/09/16  | 06/12/16  | Crawl list page summary (1) |
| 3 | 06/13/16  | 06/19/16  | Crawl list page summary (2) + Crawl app detail page (1)|
| 4 | 06/20/16  | 06/26/16  | Crawl app detail page (2) + Crawl "more" page of the list (1)|
| 5 | 06/27/16  | 07/02/16  | Crawl "more" page of the list (2) + pipeline into MongoDB|
| 3 | 07/03/16  | 07/09/16  | Readme writup + frontend display  |
| 3 | 07/10/16  | 07/16/16  | User Manual Writing and Presentation Making  |

>Office timeline: 
>* 第二周（6月7日－6月13日）第一次团队会议，以及前期准备
>* 第三周（6月14日－6月20日）项目第一周
>* 第四周（6月21日－6月27日）项目第二周
>* 第五周（6月28日－7月4日）项目第三周
>* 第六周（7月5日－7月11日）项目第四周
>* 第七周（7月12日－7月18日）完成项目报告及Demo视频录制


## Resource
- [BitTiger Project: AppStore - Crawler](https://slack-files.com/T0GUEMKEZ-F0J4G9QTT-274d3bc97e)
- [MonkeyKing Crawler Practise](https://www.bittiger.io/blog/post/poDC9eisWZdnModZg) 
- How to design crawler series
 - [Page Analysis](https://www.bittiger.io/videos/Y74hRcKTat82aJ5vr/TpxCSKrGpiKwuhP32) 
 - [Multithreading Concurrence](https://www.bittiger.io/videos/aR2v6cezXGMwT442N/TpxCSKrGpiKwuhP32)
 - [Distributed Crawler](https://www.bittiger.io/videos/9AzCHswk4GeABWzoJ/TpxCSKrGpiKwuhP32)
- [Jing's crawler repo](https://github.com/BitTigerInst/Kumamon) 
  

## License
See the [LICENSE](LICENSE.md) file for license rights and limitations (MIT).

## Project Information
- category: full stack
- team: HealthyGrain
- description: One sentence description for your awesome project.
- stack: Scrapy, ScrapyJS,Splash, MongoDB

> **Note:** 我们使用[爬虫](https://github.com/hackjustu/Project-Markdown-Table-Generator)爬取 `Project Information` 部分的内容并生成项目统计数据。为了方便系统识别，建议`category`和`stack`部分使用下面列举的选项。 如果发现需要别的选项不在列表中，请和我们联系^^
>
>**category options:** 
>full stack, big data, mobile
>
> **stack options:**
> android angular aws big_data boostrap cordova css docker firebase flask github grunt html5 ios java javascript jquery meteor mongodb mysql nodejs python react reddis ruby_on_rails ruby spark spring_mvc tomcat windows
