import os

os.system("rm -r s2_zip/*")
products=[]
f=open("s2_zip/products.dat","w")
for filename in os.listdir("target_products"):
  if("NDVI" not in filename):
    f.write(filename+"\n") 
f.close()

os.system("~/miniconda3/envs/senpy/bin/python /home/heido/cvat-vsm/dias_old/main_engine.py -d s2_zip")
os.system("rm s2_zip/product*")
os.system("mv s2_zip/* ../preprocessing/s2_zip/")
