# pokemongo_mitmproxy_scripts
A collection of scripts for `mitmproxy` tailored for Pokemon Go analysis.

## Usage
### Linux
1. Install the requirements using `pip install -r requirements.txt`.
2. Allow IPv4 forwarding using `sudo sysctl -w net.ipv4.ip_forward=1`.
3. DNAT port 443 to 8080 using `sudo iptables -t nat -A PREROUTING -i <interface> -p tcp --dport 443 -j REDIRECT --to-port 8080` where `<interface>` is the network interface that the proxy will be bound to. There should be no other applications listening on the ports 8080 or 443.
4. Run the proxy using `./start_proxy.sh [script]`. `script` is an optional argument which defaults to `dump_raw_streams.py`. Another possible script is `dump_protobuf_decoded_streams.py`, but using that one requires that `protoc` is installed.
