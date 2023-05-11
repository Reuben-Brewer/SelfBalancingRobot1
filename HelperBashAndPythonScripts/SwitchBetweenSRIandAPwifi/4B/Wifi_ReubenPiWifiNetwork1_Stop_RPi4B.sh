#CANNOT HAVE ANY SPACE IN BETWEEN VARIABLE NAME, EQUAL SIGN, AND VALUE, OR ELSE THE ASSIGNMENT WON'T TAKE.

MyScriptsPath=$(dirname "$0")
echo "MyScriptsPath = $MyScriptsPath"

echo "Copying dhcpcd.conf"
sudo cp "$MyScriptsPath"/dhcpcd.conf_ORIGINAL_RPi4B_1 /etc/dhcpcd.conf

echo "Copying dnsmasq.conf"
sudo cp "$MyScriptsPath"/dnsmasq.conf_ORIGINAL_RPi4B_1 /etc/dnsmasq.conf

sleep 0.5
echo "Stopped ReubenPiWifiNetwork1 on RPi4B. MUST RESTART TO USE NEW NETWORK CONNECTION."
sleep 0.5
#sudo reboot

