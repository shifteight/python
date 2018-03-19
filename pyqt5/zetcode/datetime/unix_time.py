#!/usr/bin/env python3

from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

unix_time = now.toMSecsSinceEpoch()
print(unix_time)

d = QDateTime.fromMSecsSinceEpoch(unix_time)
print(d.toString(Qt.ISODate))
