# -*- coding: utf-8 -*-

import cPickle

import environmentParser
import rabbitmqConnector
import log

from database import *

class Core(object):
	def __init__(self):
		self.logger = log.logger

		self.channel = rabbitmqConnector.RabbitmqConnector()

		# exchange for backend to publish 
		self.channel.exchangeDeclare('backend', 'direct')
		# exchange for frontend to publish
		self.channel.exchangeDeclare('frontend', 'direct')

		queueNames = ['config', 'cmd']
		for queueName in queueNames:
			self.channel.queueDeclare(queueName)
			self.channel.bindDeclare(exchangeName = 'frontend',
									queueName =	queueName,
									routingKey = queueName)
			# note the noACK tag is set to False
			# so don't forget to send ACKs
			self.channel.consumeSetting(self.serve, queueName, False)

	def start(self):
		self.channel.startConsuming()

	def serve(self, channel, method, properties, body):
		if method.routing_key == 'config':
			# xml config file
			try:
				# plan to use cPickle to serialize config file,
				data = cPickle.loads(body)
				self.logger.log('Config file received')
			except cPickle.UnpicklingError:
				print 'Config file should be serialized'
		elif method.routing_key == 'cmd':
			# instructions
			self.logger.log('Command received')
		
		# labor code here...

		# database test case:
#		projects = Project.query.all()
#		print "[core]", projects[0].name
#		print "[core]", projects[0].topology[0].name
#		print "[core]", projects[0].topology[0].device[0].pos

		# when job done, send ack
		self.channel.ack(method.delivery_tag)

			
	def __del__(self):
		pass
