from django.contrib import admin
from django.contrib.auth.models import Group
from .models import csvs
from fpdf import FPDF
# Register your models here.
from django.shortcuts import render
from django.http import HttpResponse
import csv
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus.tables import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle

def generateCSV(self,request,queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;   filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

        return response
def write_pdf_view(self,request,queryset):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(200, 800, 'END OF SERVICE SETTLEMENT')

    p.drawString(50,750,'Employee name:')
    p.drawString(300,750,'Date of Relieving:')
    p.drawString(420,750,'Status')
    
    p.drawString(50,730,'Alexagnder Matthew')
    p.drawString(300,730,'31/08/2009')
    p.drawString(420,730,'Resigned')
    #p.drawBoundary(50,50,700,w=495,h=20)

    p.drawString(200,680,'Days')
    p.drawString(250,680,'Remark')  
    p.drawString(510,680,'Amount')

    p.drawString(50,650,'Gratuity')
    p.drawString(200,650,'28.02')
    p.drawString(250,650,'Graduity details')
    p.drawString(510,650,'933.97')

    p.drawString(50,630,'EL Adjustment')
    p.drawString(200,630,'40.04') 
    p.drawString(250,630,'Earn leave calculated')
    p.drawString(510,630,'109.69')

    p.drawString(50,610,'Loan Deductiona')
    p.drawString(510,610,'00.0')

    p.drawString(50,590,'Air Tkt Adjustment')
    p.drawString(510,590,'00.0')

    p.drawString(50,570,'Miscellaneous Payments')  
    p.drawString(510,570,'1000.00')

    p.drawString(50,550,'Miscellaneous Deductions')
    p.drawString(510,550,'40')
    p.drawString(250,550,'Petty Cash')

    p.drawString(380,530,'Net Amount')
    p.drawString(510,530,'2,083.66')

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
class csvsAdmin(admin.ModelAdmin):
    model=csvs
    fields=['file_name','uploaded','activated']
    list_filter=['file_name']
    actions=[generateCSV,write_pdf_view]

    admin.site.site_header="django dashboard"
    
admin.site.unregister(Group)
admin.site.register(csvs,csvsAdmin)