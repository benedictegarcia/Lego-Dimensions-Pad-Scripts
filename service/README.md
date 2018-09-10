How to enable service : 
 
sudo chmod 644 /lib/systemd/system/hello.service
chmod +x /home/pi/hello_world.py
sudo systemctl daemon-reload
sudo systemctl enable hello.service
sudo systemctl start hello.service

sudo systemctl status hello.service


Manage service : 
# Check status
sudo systemctl status hello.service

# Start service
sudo systemctl start hello.service

# Stop service
sudo systemctl stop hello.service

# Check service's log
sudo journalctl -f -u hello.service


Source : 
http://www.diegoacuna.me/how-to-run-a-script-as-a-service-in-raspberry-pi-raspbian-jessie/
