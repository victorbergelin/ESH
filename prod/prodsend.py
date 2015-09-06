# prodsend.py

from datetime import datetime
datestring = "2015-09-03_17-03-16"
date_object = datetime.strptime('datestring', '%Y-%m-%d_%H-%M-%s')


POST till http://kontoret.exceed-it.se/measurements
Data:
measurement[timestamp]: string (åååå-mm-dd hh:mm:ss) 2015-09-03_17-03-16
measurement[study_level]: integer (0-100)
measurement[confidence]: integer (0-100)
measurement[co2]: integer (0-100)
measurement[temperature]: integer
measurement[punkt_id]: integer