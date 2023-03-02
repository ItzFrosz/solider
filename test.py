import ipinfo
access_token = '8e457c0224df02'
handler = ipinfo.getHandler(access_token)
ip_address = '178.247.200.51'
details = handler.getDetails(ip_address)
print(f"Місто людини : {details.city}")
print(f"Координати людини : {details.loc}")
#print(details.)
