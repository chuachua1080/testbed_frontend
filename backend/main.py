# -*- coding: utf-8 -*-

import environmentParser

environmentParser.environment = environmentParser.Environment()

import log
import core
from database import *

if __name__ == '__main__':
		
	# setup logger
	log.logger = log.Logger()
	logger = log.logger
	logger.log('Logger initialized','info')

	# database 
	setup_all()
	logger.log('Database initialized', 'info')

	# uncomment these lines to recreate database table
#	drop_all()
#	create_all()

	# setup core object that respones to requests
	core = core.Core()
	logger.log('Core initialized', 'info')

	core.start()
