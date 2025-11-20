# Antes de executar, dê pip install pytz pois o pytz é uma biblioteca não nativa no python.

from datetime import datetime

import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)