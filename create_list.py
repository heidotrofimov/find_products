import os
from datetime import datetime, timedelta

list_for_senpy=open("list_for_senpy.txt","w")

for target in os.listdir("target_products"):
  if("NDVI" not in target): 
    date_str=target.split("_")[2].split("T")[0]
    date_obj = datetime(int(date_str[0:4]),int(date_str[4:6]),int(date_str[6:8]))
    date_start=date_obj-timedelta(days=8)
    date_end=date_obj+timedelta(days=2)
    date_start_str=str(date_start.year)+"-"+str(date_start.month)+"-"+str(date_start.day)
    date_end_str=str(date_end.year)+"-"+str(date_end.month)+"-"+str(date_end.day)
    list_for_senpy.write(date_start_str+","+date_end_str+"\n")

list_for_senpy.close()



