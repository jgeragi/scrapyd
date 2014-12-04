import re
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from linkbot.items import LinkbotItem


class LinkSpider(CrawlSpider):
    name = 'links'
    allowed_domains = ['snagajob.com']
    start_urls = ['http://www.snagajob.com/find-jobs-by-job-title?j=a']  
    REDIRECT_MAX_TIMES = 3
    COOKIES_ENABLED = False
    AUTOTHROTTLE_ENABLED = False
    CONCURRENT_REQUESTS = 600
    RETRY_ENABLED = False
    DOWNLOAD_TIMEOUT = 10
    download_delay = 0.00
    DEPTH_LIMIT = 3
    rules = (
                Rule(SgmlLinkExtractor(restrict_xpaths=('//ul[@class="jobList"]/li/a')),follow=True,callback='parse_html'),
                Rule(SgmlLinkExtractor(restrict_xpaths=('//p[@class="alphabetNav"]/a')),follow=True,callback='parse_html'),
                Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="paging cf"]/nav/a')),follow=True,callback='parse_html'),
                Rule(SgmlLinkExtractor(restrict_xpaths=('//h2[@itemprop="title"]/a')),follow=True,callback='parse_html'),
                #Rule(SgmlLinkExtractor(allow_domains='snagajob.com'),follow=True,callback='parse_html'),
                #Rule(SgmlLinkExtractor(restrict_xpaths=('//body')),follow=True,callback='parse_html'),
	    )
    def parse_html(self, response):
        sel = Selector(response)
        links = re.findall(r'(http?://www.snagajob.com/job-seeker\S+)', response.url)
        item = LinkbotItem(
            page_links=links,
            )
        yield item


