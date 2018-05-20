# WL-Monitor-Pi
Data Source: City of Vienna (Stadt Wien) - https://data.wien.gv.at

Here is the corresponding Alexa skill [WL-Monitor-Pi-Alexa](https://github.com/mabe-at/WL-Monitor-Pi-Alexa).

Wiener Linien Departure Monitor with Raspberry Pi  
Quick and dirty python script for monitoring departures of lines at certain stations towards certain directions.

Obtain your API key [here](https://www.wien.gv.at/formularserver2/user/formular.aspx?pid=3b49a23de1ff43efbc45ae85faee31db&pn=B0718725a79fb40f4bb4b7e0d2d49f1d1).

Search for RBL numbers [here](https://till.mabe.at/rbl/).

```
usage: ./monitor.py [-h] [-t time] -k apikey rbl [rbl ...]

arguments:
  -k, --key=	API key
  rbl           RBL number

optional arguments:
  -h, --help	show this help
  -t, --time=	time between station updates in seconds, default 10
```

## Photos
![](https://raw.githubusercontent.com/mabe-at/WL-Monitor-Pi/master/PHOTOS/photo1.jpg)
![](https://raw.githubusercontent.com/mabe-at/WL-Monitor-Pi/master/PHOTOS/photo2.jpg)
![](https://raw.githubusercontent.com/mabe-at/WL-Monitor-Pi/master/PHOTOS/photo3.jpg)
