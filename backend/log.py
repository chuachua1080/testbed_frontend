# -*- coding: utf-8 -*-

import datetime
import socket

import rabbitmqConnector
import environmentParser

# a global logger
logger = None

class Logger(object):
	def __init__(self):
		# setup channel
		self.channel = rabbitmqConnector.RabbitmqConnector()

		# declare an exchange for logging, with name 'log' and type 'direct'
		self.channel.exchangeDeclare('log', 'direct')

		self.loggingLevel = ['info', 'warn', 'error']

		# get local public IP address
		self.ip = socket.gethostbyname(socket.gethostname())

	def log(self, message, level = 'info'):
		if level in self.loggingLevel:
			timeStamp = str( datetime.datetime.now() )
			message = '[%s][%s] %s' % (self.ip, timeStamp, message)
			self.channel.publish('log', level, message)
		else:
			print 'Logging level should be "info", "warn" or "error"'

