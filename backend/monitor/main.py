# -*- coding: utf-8 -*-

from .. import environmentParser
from .. import rabbitmqConnector

class Monitor(object):
	def __init__(self, careList, actionFunction):
		# setup channel		
		self.channel = rabbitmqConnector.RabbitmqConnector()
		
		self.channel.exchangeDeclare('log', 'direct')

		# declare a newQueue and get its name
		newQueue = self.channel.queueDeclare('', True)
		queueName = newQueue.method.queue

		for key in careList:
			self.channel.bindDeclare('log', queueName, key)

		self.channel.consumeSetting(actionFunction, queueName, True)

	def start(self):
		self.channel.startConsuming()

def printOnScreen(channel, method, properties, body):
	print '[%s] %s' % (method.routing_key, body)


if __name__ == '__main__':
	environmentParser.environment = environmentParser.Environment()

	monitor = Monitor(['info', 'warn', 'error'], printOnScreen)
	monitor.start()
