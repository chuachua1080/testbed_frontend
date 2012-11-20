# -*- coding: utf-8 -*-


import environmentParser

environment = environmentParser.environment

username = environment.databaseUsername()
password = environment.databasePassword()
address = environment.databaseAddress()
databaseName = environment.databaseName()
debug = environment.databaseDebug()

from elixir import *

metadata.bind = 'mysql+mysqlconnector://%s:%s@%s/%s' % \
					(username, password, address, databaseName)
metadata.bind.echo = debug

tablePrefix = 'dbapp_'

class Connection(Entity):
	using_options(tablename = tablePrefix + 'connection')
	
	source = Field(Unicode(30))
	sourcePort = Field(Unicode(30))
	target = Field(Unicode(30))
	targetPort = Field(Unicode(30))
	bandwidth = Field(Unicode(30))
	note = Field(Unicode(600))
	
	topology = ManyToOne('Topology')

class Device(Entity):
	using_options(tablename = tablePrefix + 'device')

	name = Field(Unicode(30))
	dtype = Field(Unicode(30))	# device type
	pos = Field(Unicode(60))

	topology = ManyToOne('Topology')

class Ovs(Entity):
	using_options(tablename = tablePrefix + 'ovs')

	name = Field(Unicode(30))
	dtype = Field(Unicode(30))	# device type
	pos = Field(Unicode(60))

	topology = ManyToOne('Topology')

class Project(Entity):
	using_options(tablename = tablePrefix + 'project')

	name = Field(Unicode(30))
	owner = Field(Unicode(30))
	attrs = Field(Unicode(300))
	start_time = Field(Unicode(30))
	end_time = Field(Unicode(30))

	topology = OneToMany('Topology')

class Topology(Entity):
	using_options(tablename = tablePrefix + 'topology')

	name = Field(Unicode(30))
	owner = Field(Unicode(30))
	attrs = Field(Unicode(300))

	project = ManyToOne('Project')
	connection = OneToMany('Connection')
	device = OneToMany('Device')
	ovs = OneToMany('Ovs')

