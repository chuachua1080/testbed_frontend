# -*- coding: utf-8 -*-

import ConfigParser

# always use this variable to access the environment
environment = None

class Environment(object):
	def __init__(self):
		self.config = ConfigParser.ConfigParser()
		self.config.read('backend/environment.cfg')

	def rabbitmqServerAddress(self):
		return self.config.get('rabbitmq', 'address')

	def databaseUsername(self):
		return self.config.get('database', 'username')

	def databasePassword(self):
		return self.config.get('database', 'password')

	def databaseAddress(self):
		return self.config.get('database', 'address')

	def databaseName(self):
		return self.config.get('database', 'database')

	def databaseDebug(self):
		if self.config.get('database', 'debug') == 'True':
			return True
		else:
			return False
