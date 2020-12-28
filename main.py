import os
from procstream import TwitterDataCollector

config = {"TWITTER_ACCESS_TOKEN": os.environ.get("TWITTER_ACCESS_TOKEN", ""),
              "TWITTER_ACCESS_TOKEN_SECRET": os.environ.get("TWITTER_ACCESS_TOKEN_SECRET", ""),
              "TWITTER_CONSUMER_KEY": os.environ.get("TWITTER_CONSUMER_KEY", ""),
              "TWITTER_CONSUMER_SECRET": os.environ.get("TWITTER_CONSUMER_SECRET", ""),
              "TWITTER_FILTER_TRACK": os.environ.get("TWITTER_FILTER_TRACK", ""),
              "MODULE_NAME": os.environ.get("MODULE_NAME", "TWITTER_DATA_COLLECTOR"),
              "CONSUMER_GROUP": os.environ.get("CONSUMER_GROUP", "TWITTER_DATA_COLLECTOR_CG")
              }

def main():
    twitter_data_collector = TwitterDataCollector()
    twitter_data_collector.run(config)


if __name__ == "__main__":
    main()