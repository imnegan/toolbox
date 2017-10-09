import logging


def testLog():
	logging.warning('testing debug')
	#for some reason, anything below warning doesn't seem to output to console.
	return 1

testLog()

print('fin')
