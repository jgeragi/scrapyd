# Scrapy settings for craigslist_sample project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'linkbot'

SPIDER_MODULES = ['linkbot.spiders']
NEWSPIDER_MODULE = 'linkbot.spiders'
ITEM_PIPELINES = {
    'linkbot.pipelines.DuplicatesPipeline': 0,
    'linkbot.pipelines.PostPipeline': 1000,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'craigslist_sample (+http://www.yourdomain.com)'
