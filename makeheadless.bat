<nul (set/p z=) > ssh
echo country=gb > wpa_supplicant.conf
echo update_config=1 >> wpa_supplicant.conf
echo ctrl_interface=DIR=/var/run/wpa_supplicant >> wpa_supplicant.conf

echo network={ >> wpa_supplicant.conf
echo  scan_ssid=1 >> wpa_supplicant.conf
echo  ssid= >> wpa_supplicant.conf
echo  psk= >> wpa_supplicant.conf
echo  key_mgmt=WPA-PSK >> wpa_supplicant.conf
echo } >> wpa_supplicant.conf

(goto) 2>nul & del "%~f0"