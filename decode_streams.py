from decoders import gzip
import os

OUTPUT_DIR = 'decoded_streams'
REQUEST_ID = 0
RESPONSE_ID = 0
REQUEST_TEMPLATE = 'request_{0}.bin'
RESPONSE_TEMPLATE = 'response_{0}.bin'

def start(context, argv):
	global OUTPUT_DIR
	
	if len(argv) == 2:
		if '--out' == argv[0]:
			OUTPUT_DIR = argv[1]
		else:
			raise ValueError('Unknown argument: {0}, expected: "--out"'.format(argv[0]))
	if not os.path.exists(OUTPUT_DIR):
		os.mkdir(OUTPUT_DIR)

def request(context, flow):
	global OUTPUT_DIR
	global REQUEST_ID
	
	if flow.request.content:
		filename = os.path.join(OUTPUT_DIR, REQUEST_TEMPLATE.format(REQUEST_ID))
		with open(filename, 'wb') as fs:
			fs.write(gzip.decode(flow.request.content))
		REQUEST_ID += 1
	
def response(context, flow):
	global OUTPUT_DIR
	global RESPONSE_ID
	
	if flow.response.body:
		filename = os.path.join(OUTPUT_DIR, RESPONSE_TEMPLATE.format(REQUEST_ID))
		with open(filename, 'wb') as fs:
			fs.write(gzip.decode(flow.response.body))
		RESPONSE_ID += 1