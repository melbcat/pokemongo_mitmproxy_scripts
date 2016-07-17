def decode(stream):
	import zlib
	return zlib.decompress(stream, zlib.MAX_WBITS + 16)