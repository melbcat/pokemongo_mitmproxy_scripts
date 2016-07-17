SCRIPT="decode_streams.py"
if (( $# == 1))
then
	SCRIPT="$1"
fi

mitmdump -s "$SCRIPT" -p 8080 -R https://pgorelease.nianticlabs.com -v
