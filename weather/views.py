import requests
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import ExistingData
from .forms import CityForm, FilterForm


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f14f45730dee91a89c48c0b485ff20b1'
    form = CityForm()
    if 'name' in request.POST:
        try:
            city = request.POST['name']
            res = requests.get(url.format(city)).json()
            data = ExistingData(city=city,
                                country=res['sys']['country'],
                                main=res['weather'][0]['main'],
                                description=res['weather'][0]['description'],
                                icon=res['weather'][0]['icon'],
                                base=res['base'],
                                temp=res['main']['temp'],
                                pressure=res['main']['pressure'],
                                humidity=res['main']['humidity'],
                                temp_min=res['main']['temp_min'],
                                temp_max=res['main']['temp_max'],
                                visibility=res['visibility'],
                                wind_speed=res['wind']['speed'],
                                clouds_all=res['clouds']['all'])
            data.save()
            form = CityForm()
            return render(request, 'weather/index.html',
                          {'data': data, 'form': form})
        except:
            data = {'city': city}
            form = CityForm()
            return render(request, 'weather/index.html',
                          {'data1': data, 'form': form})
    else:
        return render(request, 'weather/index.html',
                      {'form': form})


def existingdata_list(request):
    if 'city' in request.GET:
        city = request.GET['city']
        data_from = request.GET['data_from']
        data_to = request.GET['data_to']
        data_list = ExistingData.objects.filter(
            city=city, data__gte=data_from, data__lte=data_to)
        form = FilterForm()
        page, datas = pag(request, data_list)
        return render(request,
                      'weather/data_list1.html',
                      {'page': page,
                       'data_list': datas,
                       'form': form
                       })
    data_list = ExistingData.objects.all()
    form = FilterForm()
    page, datas = pag(request, data_list)
    return render(request,
                  'weather/data_list.html',
                  {'page': page,
                   'data_list': datas,
                   'form': form
                   })


def pag(request, data_list):
    paginator = Paginator(data_list, 2)
    page = request.GET.get('page')
    datas = paginator.get_page(page)
    return (page, datas)
