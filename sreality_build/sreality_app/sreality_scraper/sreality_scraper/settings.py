BOT_NAME = "sreality_scraper"
SPIDER_MODULES = ["sreality_scraper.spiders"]
NEWSPIDER_MODULE = "sreality_scraper.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "sreality_scraper.pipelines.SrealityPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

LOG_LEVEL = 'WARNING'
