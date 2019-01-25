import logging
import logging.config
import yaml


with open("app/log.yaml") as f:
	config = yaml.safe_load(f.read())
	logging.config.dictConfig(config)
logger = logging.getLogger(__name__)