import subprocess

def decode(stream):
	process = subprocess.Popen(['protoc', '--decode_raw'],
				   stdin=subprocess.PIPE,
				   stdout=subprocess.PIPE)
	return process.communicate(stream)[0]
