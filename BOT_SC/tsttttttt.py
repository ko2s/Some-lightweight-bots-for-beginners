from datetime import datetime
import pytz
from main_def import *
# الحصول على التاريخ الحالي
current_date = datetime.now(pytz.utc)

# استخراج الشهر الحالي
current_month = current_date.month
current_year = current_date.year
joining_data = rest(984370413)
joining_month= str(joining_data).split("-")[1]
joining_year= str(joining_data).split("-")[0]
if current_year == int(joining_year) and current_month == int(joining_month):
    print("ok Aqila")