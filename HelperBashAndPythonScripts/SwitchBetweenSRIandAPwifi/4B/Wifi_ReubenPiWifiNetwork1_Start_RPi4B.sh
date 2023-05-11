#CANNOT HAVE ANY SPACE IN BETWEEN VARIABLE NAME, EQUAL SIGN, AND VALUE, OR ELSE THE ASSIGNMENT WON'T TAKE.

MyScriptsPath=$(dirname "$0")
echo "MyScriptsPath = $MyScriptsPath"

echo "Copying dhcpcd.conf"
sudo cp "$MyScriptsPath"/dhcpcd.conf_ReubenPiWifiNetwork1_RPi4B /etc/dhcpcd.conf

echo "Copying dnsmasq.conf"
sudo cp "$MyScriptsPath"/dnsmasq.conf_ReubenPiWifiNetwork1_RPi4B /etc/dnsmasq.conf

sleep 0.5
echo "Started ReubenPiWifiNetwork1 on RPi4B. MUST REBOOT TO USE NEW NETWORK CONNECTION."
sleep 0.5
#sudo reboot



