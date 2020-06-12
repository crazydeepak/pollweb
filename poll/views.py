import requests
import time
import datetime
import pytz
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import MonitorForm
from .models import Monitor, Response
import threading


# Time is not showing proper in webpage.
# Date is not displaying


# Create your views here.


def individual_monitor(request, monitor_id):
    objects = Response.objects.filter(
        url_id=monitor_id).order_by('-checked_ts')
    print(objects[0])

    print("main process")
    response_table = {
        'URL': objects[0].url_id,
        'checked_ts': objects[0].checked_ts,
        'secs_for_first_response': objects[0].secs_for_first_response,
        'response_code': objects[0].response_code
    }
    context = {'response_table': response_table}
    return render(request, 'poll/individual.html', context)


def background_process():
    # def startpolling(request):
    # objects[0].url_id.frequence_in_sec
    # objects[0].url_id.url
    # obj = Monitor.objects.get(id=monitor_id)
    url_count = Monitor.objects.all().count()
    obj = []
    urls = []
    last_checked_in = []
    frequency_url = []
    for i in range(url_count):
        print("Url count", i)
        obj.append(Response.objects.filter(url_id=i+1).order_by('-checked_ts'))
        urls.append(obj[i][0].url_id.url)
        frequency_url.append(obj[i][0].url_id.frequence_in_secs)
        last_checked_in.append(obj[i][0].checked_ts)
    print(obj)
    print(urls)
    # print(frequency_url)
    # print(last_checked_in)

    last_pinged = []
    ping_next = []
    flag = []
    last_pinged = last_checked_in
    for i in range(url_count):
        flag.append(0)
        ping_next.append(last_pinged[i] +
                         datetime.timedelta(seconds=frequency_url[i]))
    print(last_pinged)
    print(ping_next)
    while True:
        for i in range(url_count):
            # if flag[i] == 0:
            #     if ping_next[i] > datetime.datetime.now(pytz.timezone('Asia/Calcutta')):
            #         flag[i] = 1
            #     else:
            #         ping_next[i] = last_pinged[i] + \
            #             datetime.timedelta(seconds=frequency_url[i])
            #         last_pinged[i] = ping_next[i]
            #         print("Time not matured")
            #         print(
            #             f"{i}------>nextping time for {urls[i]}-{ping_next[i]}")
            #         print(
            #             f"current time is {datetime.datetime.now(pytz.timezone('Asia/Calcutta'))}")
            # else:
            if datetime.datetime.now(pytz.timezone('Asia/Calcutta')) >= ping_next[i]:
                Monitor_obj = Monitor.objects.get(id=i+1)
                start = time.clock()
                r = requests.head(obj[i][0].url_id.url)
                response_code = r.status_code
                request_time = time.clock() - start
                checked_ts = datetime.datetime.now(
                    pytz.timezone('Asia/Calcutta'))
                obj_response = Response(
                    url_id=Monitor_obj, checked_ts=checked_ts, secs_for_first_response=request_time, response_code=response_code)
                obj_response.save()
                print(
                    f"***********current_time is {datetime.datetime.now(pytz.timezone('Asia/Calcutta'))} pinging {urls[i]}***********")
                last_pinged[i] = ping_next[i]
                ping_next[i] = last_pinged[i] + \
                    datetime.timedelta(seconds=frequency_url[i])
                print(
                    f"{i}------>nextping time for {urls[i]}-{ping_next[i]}=================TIME MATURED=================")

        # print(ping_next)

        time.sleep(5)

    # while True:

    # obj = Monitor.objects.get(id=monitor_id)

    # response_code = '-999'
    # flag = 1
    # try:

    #     # check for the last poll time
    #     # check for the frewquenc
    #     # initialte rewqus if due
    #     temp_time = obj.frequence_in_secs
    #     print(temp_time)

    #     while True:
    #         if flag == 1:
    #             print("inside Flag")
    #             flag = 0
    #             start = time.clock()
    #             r = requests.head(obj.url)
    #             response_code = r.status_code
    #             request_time = time.clock() - start
    #             checked_ts = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
    #             print(
    #                 f"visiting {obj.url} and frequency of polling is {obj.frequence_in_secs}")
    #             print(f"current time is {checked_ts}")
    #             obj_response = Response(url_id=obj,
    #                                     checked_ts=checked_ts, secs_for_first_response=request_time, response_code=response_code)
    #             obj_response.save()
    #             # insert to response table
    #             print(
    #                 f" statuscode received {response_code} in {request_time} secs")
    #             print(checked_ts)
    #         obj.frequence_in_secs = obj.frequence_in_secs-1
    #         print(obj.frequence_in_secs)
    #         if obj.frequence_in_secs == 0:
    #             flag = 1
    #             obj.frequence_in_secs = temp_time
    #         time.sleep(1)

    #     # prints the int of the status code. Find more at httpstatusrappers.com :)
    # except requests.ConnectionError:
    #     print("failed to connect")


def dashboard(request):
    query_set = Response.objects.all()
    context = {"object_set": query_set}
    return render(request, "poll/response_list.html", context)

    # pull all records from response table
    # show it on scrren
    # return HttpResponse('dashboard')


def startpolling(request):
    t = threading.Thread(target=background_process,
                         args=(), kwargs={})
    t.setDaemon(True)
    t.start()
    query_set = Response.objects.all()
    context = {"object_set": query_set}
    return render(request, "poll/response_list.html", context)

#     whilte(1):
#         magic
#         table
#     yahoo
#     1200s/last ping: 7: 00
#     google
#     1200s/last ping: 7: 00


# while(1sec):
#     yahoo:
#         7: 02 - insert
#         7: 04 - insert
