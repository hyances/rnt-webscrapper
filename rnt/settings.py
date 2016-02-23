# Scrapy settings for rnt project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'rnt'

SPIDER_MODULES = ['rnt.spiders']
NEWSPIDER_MODULE = 'rnt.spiders'

#ITEM_PIPELINES = ['rnt.pipelines.RntPipeline', 'rnt.pipelines.JsonWithEncodingPipeline']
#ITEM_PIPELINES = ['rnt.pipelines.RntCartagena']
ITEM_PIPELINES = ['rnt.pipelines.RntEmpty']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'rnt (+http://www.yourdomain.com)'

# LOGGING
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
LOG_FILE = 'logs/scrapy.log'
LOG_LEVEL = 'DEBUG'
LOG_STDOUT = False