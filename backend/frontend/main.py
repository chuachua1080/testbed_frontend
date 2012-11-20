# -*- coding: utf-8 -*-

import cPickle

from .. import environmentParser
from .. import rabbitmqConnector

class Frontend(object):
	def __init__(self):
		self.channel = rabbitmqConnector.RabbitmqConnector()

		# exchange for backend to publish 
		self.channel.exchangeDeclare('backend', 'direct')
		# exchange for frontend to publish
		self.channel.exchangeDeclare('frontend', 'direct')

	def sendConfigurationFile(self):
		fileName = 'backend/main.py'
		configurationFile = open(fileName, 'r').read()
		pickled = cPickle.dumps(configurationFile)
		self.channel.publish('frontend', 'config', pickled)

if __name__ == '__main__':
	environmentParser.environment = environmentParser.Environment()
	frontend = Frontend()
	frontend.sendConfigurationFile()
