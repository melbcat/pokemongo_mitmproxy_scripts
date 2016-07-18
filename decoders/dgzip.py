import cStringIO
import gzip

def decode(stream):
	buf = cStringIO.StringIO(stream)
	reader = gzip.GzipFile(fileobj=buf, mode='rb')
	
	return reader.read()
