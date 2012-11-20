# -*- coding: utf-8 -*-

import pika

import environmentParser

class RabbitmqConnector(object):
	def __init__(self):
		serverAddress = environmentParser.environment.rabbitmqServerAddress()
		self.connection = pika.BlockingConnection(
								pika.ConnectionParameters(
									host = serverAddress))
		self.channel = self.connection.channel()

	def exchangeDeclare(self, exchangeName, exchangeType):
		return self.channel.exchange_declare(exchange = exchangeName,
											type = exchangeType)

	def queueDeclare(self, queueName = '',exclusiveFlag = False):
		return self.channel.queue_declare(queue = queueName,
										exclusive = exclusiveFlag)

	def publish(self, exchangeName, routingKey, message, 
				replyTo = None, messageId = None):
		self.channel.basic_publish(exchange = exchangeName,
									routing_key = routingKey,
									body = message,
									properties = pika.BasicProperties(
											reply_to = replyTo,
											correlation_id = messageId))

	
	def bindDeclare(self, exchangeName, queueName, routingKey = None):
		# bind exchange with queue.
		# note that when routingKey == None, exchange type should be 'fanout',
		# when routingKey contains '#' or '*', exchange type should be 'topic',
		# when routingKey is an explicit string without '#' or '*',
		# exchange type should be 'direct'
		self.channel.queue_bind(exchange = exchangeName,
								queue = queueName,
								routing_key = routingKey)
	
	def consumeSetting(self, callback, queueName, noAckTag = True):
		self.channel.basic_consume(callback,
								queue = queueName,
								no_ack = noAckTag)

	def startConsuming(self):
		self.channel.start_consuming()

	def ack(self, deliveryTag):
		self.channel.basic_ack(deliveryTag)

	def __del__(self):
		self.connection.close()
