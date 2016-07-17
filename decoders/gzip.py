def decode(stream):
	import cStringIO
	import gzip
	
	buf = cStringIO.StringIO(stream)
	reader = gzip.GzipFile(fileobj=buf, mode='rb')
	
	return reader.read()
