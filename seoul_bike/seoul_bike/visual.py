import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seoul_bike.settings")
import django
django.setup()
from django.shortcuts import render
from seoul_bike.models import *
from django.db.models import Sum

import pandas as pd
import numpy as np



#df2 = pd.DataFrame(list(DongCode.objects.all().values()))
# usage = MonthUsage.objects.annotate(total_pages=Sum('s'))
# print(usage)

def year_usage():
    month_usage = pd.DataFrame(list(MonthUsage.objects.all().values()))
    print(month_usage['s'].sum())
    result = month_usage['s'].sum()

    return result

year_usage()