import locale
import sys
# from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.db.models import Count, Q, Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.apps import apps
from django_datatables_view.base_datatable_view import BaseDatatableView
# import jdatetime
# import datetime
from StoreMenuApp.models import *
from StoreMenuApp.serializers import *

locale.setlocale(locale.LC_ALL, '')

# فانکشن های تبدیل متن به کلاس.
## در حالت نرمال جهت کنترل سطح دسترسی و لاگین بودن از درکوریتور های : @login_required('/'), @permission_required() استفاده می شود .
class Convertors:
    def __init__(self, modelname, serilaizerzname):
        self.modelname = modelname
        self.serilaizerzname = serilaizerzname

    def str_to_class(self):
        classname = getattr(sys.modules[__name__], self.modelname)
        return classname


    def get_model_class(self):
        ModelName = apps.get_model('StoreMenuApp', self.serilaizerzname)
        return ModelName
        

## در حالت نرمال جهت کنترل سطح دسترسی و لاگین بودن از : LoginRequiredMixin, PermissionRequiredMixin استفاده می شود .
class Crud(Convertors):
    def __init__(self, modelname, serialname):
        Convertors.__init__(self, modelname = modelname, serilaizerzname = serialname)


    def Create(self):
        SrName = Convertors(self.POST['SerializersName'], self.POST['SerializersName'])
        try:
            SerialToCalss = SrName.str_to_class()
            result = SerialToCalss(data = self.POST)
            if result.is_valid():
                result.save()

                data = {
                    'ok': 'ok'
                }
                return JsonResponse(data)
            
        except(ValueError) as Error:
            data = {
                    'Error': Error
                }
            return JsonResponse(data)


    def FindUpdateIndo(self):
        modelname = Convertors(self.POST['ModelName'], self.POST['ModelName'])
        ModelStrName = self.POST['ModelName']

        if ModelStrName == 'Store' or ModelStrName == 'GoodsAndServices' or ModelStrName == 'CustomersGroup':
            UpdateResult = modelname.get_model_class().objects.filter(id=int(self.POST['rowid'])).values_list('Name', 'Status', 'Desc')[0]
            data = {
                'Name': UpdateResult[0],
                'Status': UpdateResult[1],
                'Desc': UpdateResult[2],
            }
            return JsonResponse(data)
        
        elif ModelStrName == 'Customers':
            UpdateResult = modelname.get_model_class().objects.filter(id=int(self.POST['rowid'])).values_list('Name', 'Family', 'Status', 'Desc', 'Group')[0]
            data = {
                'Name': UpdateResult[0],
                'Family': UpdateResult[1],
                'Status': UpdateResult[2],
                'Desc': UpdateResult[3],
                'Group': UpdateResult[4],
            }
            return JsonResponse(data)
        
        elif ModelStrName == 'Recept':
            UpdateResult = modelname.get_model_class().objects.filter(id=int(self.POST['rowid'])).values_list('GoAndSer', 'Custom', 'Type', 'Desc', 'Count', 'Sto')[0]
            data = {
                'GoAndSer': UpdateResult[0],
                'Custom': UpdateResult[1],
                'Type': UpdateResult[2],
                'Desc': str(UpdateResult[3]),
                'Count': UpdateResult[4],
                'Sto': UpdateResult[5],
            }
            return JsonResponse(data)
    

    def Update(self):
        modelname = Convertors(self.POST['ModelName'], self.POST['ModelName'])
        SrName = Convertors(self.POST['SerializersName'], self.POST['SerializersName'])
        try:
            UpdateResult = modelname.get_model_class().objects.get(id=int(self.POST['rowid']))
            result = SrName.str_to_class()(UpdateResult, data=self.POST)
            if result.is_valid():
                result.save()

                data = {
                    'ok': 'ok'
                }
                return JsonResponse(data)
            
        except(ValueError) as Error:
            data = {
                    'Error': Error
                }
            return JsonResponse(data)

    def Delete(self):
        modelname = Convertors(self.POST['ModelName'], self.POST['ModelName'])
        DeleteIthem = get_object_or_404(modelname.get_model_class(), id=int(self.POST['rowid']))
        DeleteIthem.delete()
        data = {
            'ok': 'ok'
        }
        return JsonResponse(data)


#بخش مربوط به کلاس های DataTable
# در حالت نرمال جهت کنترل سطح دسترسی و لاگین بودن از : LoginRequiredMixin, PermissionRequiredMixin استفاده می شود .

## 1-Store ListView And DTView Is Here:
class StoreLV(ListView):
    model = Store
    context_object_name = 'StoreList'
    template_name = 'MasterReport.html'
    queryset = Store.objects.all()

    def get_context_data(self, **kwargs):
        context = super(StoreLV, self).get_context_data(**kwargs)
        context['Store'] = Store.objects.all()
        return context

class MasterReport(ListView):
    model = Store
    context_object_name = 'StoreListreport'
    template_name = 'MasterReport.html'
    queryset = Store.objects.all()

    def get_context_data(self, **kwargs):
        context = super(MasterReport, self).get_context_data(**kwargs)
        context['Store'] = Store.objects.all()
        GsReport = Recept.objects.filter(id__gt=0).values('GoAndSer', 'Sto').annotate(sum=Sum('Count')).order_by('GoAndSer')
        resultlist = []
        for a in GsReport:
            if len(list(a.values()))>0:
                resultlist.append((GoodsAndServices.objects.filter(id=list(a.values())[0]).values('Name')[0]['Name'],Store.objects.filter(id=list(a.values())[1]).values('Name')[0]['Name'], list(a.values())[2]))
        context['report'] = resultlist
        return context


class Search:
    def ReportFilter(self):
        serchithem = self.POST['serchithem']
        Gid = GoodsAndServices.objects.filter(Name__icontains = serchithem).values_list('id', flat=True)
        findresult = Recept.objects.filter(GoAndSer__in = Gid).values('GoAndSer', 'Sto').annotate(sum=Sum('Count')).order_by('GoAndSer')

        resultlist = []
        for a in findresult:
            if len(list(a.values()))>0:
                resultlist.append(
                    f'''
                        <tr>
                            <td>{GoodsAndServices.objects.filter(id=list(a.values())[0]).values('Name')[0]['Name']}</td>
                            <td>{Store.objects.filter(id=list(a.values())[1]).values('Name')[0]['Name']}</td>
                            <td>{list(a.values())[2]}</td>
                        </tr>
                    '''
                )

        data = {
            'resultlist': resultlist
        }

        return JsonResponse(data)
    

    def ReportFilterByStoreID(self):
        serchithem = '0'
        if len(self.POST)> 1:
            serchithem = list(self.POST['serchithem[]'])

        findresult = ['0','0','0']
        if serchithem == '0':
            findresult = Recept.objects.filter(id__gt = 0).values('GoAndSer', 'Sto').annotate(sum=Sum('Count')).order_by('GoAndSer')
        else:
            findresult = Recept.objects.filter(Sto__in = serchithem).values('GoAndSer', 'Sto').annotate(sum=Sum('Count')).order_by('GoAndSer')

        resultlist = []
        for a in findresult:
            if len(list(a.values()))>0:
                resultlist.append(
                    f'''
                        <tr>
                            <td>{GoodsAndServices.objects.filter(id=list(a.values())[0]).values('Name')[0]['Name']}</td>
                            <td>{Store.objects.filter(id=list(a.values())[1]).values('Name')[0]['Name']}</td>
                            <td>{list(a.values())[2]}</td>
                        </tr>
                    '''
                )

        data = {
            'resultlist': resultlist
        }

        return JsonResponse(data)
        

class StoreDT(BaseDatatableView):
    model = Store
    columns = ['', '', 'id', 'Name', 'Status', 'Desc']

    def render_column(self, row, column):
        return super(StoreDT, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(Name__icontains=search)| Q(Desc__icontains=search)| Q(Status__icontains=search))

        qs = qs.filter(Q(id__gt = 0))
        return qs
    

## 2-GoodsAndServices ListView And DTView Is Here:
class GoodsAndServicesLV(ListView):
    model = GoodsAndServices
    context_object_name = 'GoodsAndServicesList'
    template_name = 'GoodsAndServicesLV.html'
    queryset = GoodsAndServices.objects.all()

    def get_context_data(self, **kwargs):
        context = super(GoodsAndServicesLV, self).get_context_data(**kwargs)
        context['GoodsAndServices'] = GoodsAndServices.objects.all()
        return context


class GoodsAndServicesDT(BaseDatatableView):
    model = GoodsAndServices
    columns = ['', '', 'id', 'Name', 'Status', 'Desc']

    def render_column(self, row, column):
        return super(GoodsAndServicesDT, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(Name__icontains=search)| Q(Status__icontains=search)| Q(Desc__icontains=search))

        qs = qs.filter(Q(id__gt = 0))
        return qs
    

## 3-CustomersGroup ListView And DTView Is Here:
class CustomersGroupLV(ListView):
    model = CustomersGroup
    context_object_name = 'CustomersGroupList'
    template_name = 'CustomersGroupLV.html'
    queryset = CustomersGroup.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CustomersGroupLV, self).get_context_data(**kwargs)
        context['CustomersGroup'] = CustomersGroup.objects.all()
        return context


class CustomersGroupDT(BaseDatatableView):
    model = CustomersGroup
    columns = ['', '', 'id', 'Name', 'Status', 'Desc']

    def render_column(self, row, column):
        return super(CustomersGroupDT, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(Name__icontains=search)| Q(Desc__icontains=search)| Q(Status__icontains=search))

        qs = qs.filter(Q(id__gt = 0))
        return qs
    

## 4-Customers ListView And DTView Is Here:
class CustomersLV(ListView):
    model = Customers
    context_object_name = 'CustomersList'
    template_name = 'CustomersLV.html'
    queryset = Customers.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CustomersLV, self).get_context_data(**kwargs)
        context['CustomersGroup'] = CustomersGroup.objects.all()
        return context


class CustomersDT(BaseDatatableView):
    model = Customers
    columns = ['', '', 'id', 'Name', 'Family', 'Group', 'Status', 'Desc']

    def render_column(self, row, column):
        return super(CustomersDT, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(Name__icontains=search)| Q(Family__icontains=search)| Q(Desc__icontains=search)| Q(Status__icontains=search) | Q(Group__icontains=search))

        qs = qs.filter(Q(id__gt = 0))
        return qs


## 5-Recept ListView And DTView Is Here:
class ReceptLV(ListView):
    model = Recept
    context_object_name = 'Recept'
    template_name = 'index.html'
    queryset = Recept.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ReceptLV, self).get_context_data(**kwargs)
        context['GoAndSer'] = GoodsAndServices.objects.all()
        context['Custom'] = Customers.objects.all()
        context['Store'] = Store.objects.all()

        return context


class ReceptDT(BaseDatatableView):
    model = Recept
    columns = ['', '', 'id', 'Type', 'Sto', 'GoAndSer', 'Custom', 'Count',  'Desc']

    def render_column(self, row, column):
        return super(ReceptDT, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(Q(GoAndSer__icontains=search)| Q(Custom__icontains=search)| Q(Count__contains=search)| Q(Type__icontains=search)| Q(Desc__icontains=search))

        qs = qs.filter(Q(id__gt = 0))
        return qs
    

## بخش مربوط به گزارش ها
