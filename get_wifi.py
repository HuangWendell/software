import pywifi
wifi = pywifi.PyWiFi()
interface = wifi.interfaces()[0]
# network_pfs = interface.network_profiles()
# for network_pf in network_pfs:
#     print(network_pf.ssid)
interface.scan()
wlans = interface.scan_results()
for wlan in wlans:
    print(wlan.bssid, wlan.ssid, wlan.signal, wlan.freq)
# netsh wlan show  interfaces
#  netsh interface ipv4 show add name="WLAN"