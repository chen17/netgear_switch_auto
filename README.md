# netgear_switch_auto

Netgear switch automation script with selenium

Works for GS105Ev2 and GS308E.

$ ./netgear.py -h
usage: netgear.py [-h] [--host HOST] [--port PORT] [--action ACTION]

optional arguments:
  -h, --help       show this help message and exit
  --host HOST      switch IP
  --port PORT      port number
  --action ACTION  action on port, default on
  
Can be used in crontab like:

30 22 * * * export DISPLAY=:0; /home/pi/netgear.py --action off
17 06 * * * export DISPLAY=:0; /home/pi/netgear.py
