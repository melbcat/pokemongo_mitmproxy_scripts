from decoders import drequest, dresponse, protocdecoder
import os

OUTPUT_DIR = 'dump.protobuf.decoded'
SESSION_FILE_PATH = 'session.pd'
DELIMITER = '\n' + ('-' * 60) + '\n'
SESSION_FILE = None

def decode_request(stream):
	return protocdecoder.decode(drequest.decode(stream))

def decode_response(stream):
	return protocdecoder.decode(dresponse.decode(stream))

def append_data(data):
	global SESSION_FILE
	
	SESSION_FILE.write(data)
	SESSION_FILE.write(DELIMITER)

def start(context, argv):
	global OUTPUT_DIR
	global SESSION_FILE
	
	if len(argv) == 2:
		if '--out' == argv[0]:
			OUTPUT_DIR = argv[1]
		else:
			raise ValueError('Unknown argument: {0}, expected: "--out"'.format(argv[0]))

	if not os.path.exists(OUTPUT_DIR):
		os.mkdir(OUTPUT_DIR)

	SESSION_FILE = open(os.path.join(OUTPUT_DIR, SESSION_FILE_PATH), 'w')

def done(context):
	global SESSION_FILE

	if SESSION_FILE:
		SESSION_FILE.close()

def request(context, flow):	
	if flow.request.content:
		append_data(decode_request(flow.request.content))
	
def response(context, flow):
	if flow.response.body:
		append_data(decode_response(flow.response.body))
