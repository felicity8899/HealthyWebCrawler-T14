BOT_NAME = 'xiaomi'
SPIDER_MODULES = ['healthy.spiders']
NEWSPIDER_MODULE = 'healthy.spiders'
DOWNLOAD_DELAY=1
ITEM_PIPELINES = {
    'healthy.pipelines.HealthyPipeline': 300,
}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "xiaomi"
MONGODB_COLLECTION = "apps"
LOG_FILE = 'scrapy.log'
