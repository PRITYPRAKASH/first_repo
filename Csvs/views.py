from itertools import product
from django.shortcuts import render
from .forms import csvsModelform
from .models import Csvs
import csv
from django.contrib.auth.models import User
#from Sales.models import Sale
def upload_file_view(request):
    form= csvsModelform(request.POST or None, request.FILES or None)
    if form.is_valid:
        form.save()
        form=csvsModelform()
        obj=Csvs.objects.get(activated=False)
        with open(obj.file_name.path,'r')as f:
            reader=csv.reader(f)

            for i ,row in enumerate(reader):
                if i==0:
                    pass
                else:
                    row="".join(row)
                    row=row.replace(";","")
                    row = row.split()
                    user=User.object.get(username=row[''])
                   #Sale.objects.create(
                       # product=product,
                      #  quantity=int(row[2]),
                       # salesman=user,

                    #)'''
                    #print(row)
                    #print(type(row))
            obj.activated=True
            obj.save()
    return render(request,'Csvs/upload.html',{'form':form})

