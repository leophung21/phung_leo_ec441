import pyshark

cap = pyshark.FileCapture('capture.pcap', display_filter='dns')

queries = set()

for pkt in cap:
    try:
        if hasattr(pkt.dns, 'qry_name'):
            queries.add(pkt.dns.qry_name)
    except:
        pass

print("DNS Queries Found:")
for q in queries:
    print(q)
