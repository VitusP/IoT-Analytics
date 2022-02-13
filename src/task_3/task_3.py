import pandas as pd
import random
import math
import collections
import numpy as np
import copy

# author: vaputra@ncsu.edu

## Global Data
mc = 0
rtcl = 3
nonRTCL = 5
n_rt = 0
n_nonrt = 0
scl = 4
s = 2 #server status
pre_empted_service_time = 0

iat_rt = 10
iat_nonrt = 5
serviceTime_rt = 2
serviceTime_nonrt = 4

iat_rt_mu = 1
iat_nonrt_mu = 1
serviceTime_rt_mu = 1
serviceTime_nonrt_mu = 1

m = 0
b = 0

rt_queue = []
nonrt_queue = [4]
rt_array = []
nonrt_array = []

df = pd.DataFrame(columns=['MC', 'RTCL', 'nonRTCL', 'n_RT', 'n_nonRT', 'SCL', 's', 'Pre-empted-service-time'])


## Main method
def main():
    global m,b, mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df, iat_nonrt_mu, iat_rt_mu, serviceTime_rt_mu, serviceTime_nonrt_mu
    
    iat_rt_mu = int(input("Enter mean IAT of RT messages: "))
    iat_nonrt_mu = int(input("Enter mean IAT of non-RT messages: "))
    serviceTime_rt_mu = int(input("Enter mean service time of RT messages: "))
    serviceTime_nonrt_mu = int(input("Enter mean service time of non-RT messages: "))
    m = int(input("Enter number of batches: "))
    b = int(input("Enter batch size: "))
    record_global_vars()

    mc = rtcl
    while not (len(rt_array) >= (m*b) and len(nonrt_array) >= (m*b)):
        # print("NONRT ARR: ", len(nonrt_array))
        randomized_param()
        event = next_event()
        if event == 0:
            rt_arrived()
        elif event == 1:
            nonrt_arrived()
        elif event == 2:
            service_completed()
    # print(df)
    # print("RT: ")
    # print(rt_array)
    # print("nonRT: ")
    # print(nonrt_array)
    #export_to_excel()


## Helper Methods
def rt_arrived():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b, mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df, iat_nonrt_mu, iat_rt_mu, serviceTime_rt_mu, serviceTime_nonrt_mu
    mc = rtcl
    n_rt = n_rt + 1
    rtcl = mc + iat_rt

    # add to queue
    rt_queue.append(mc)
    
    if n_rt == 1 and s == 0:
        scl = mc + serviceTime_rt
        n_rt = n_rt - 1
        rt_array.append(scl-rt_queue.pop(0))
        s = 1
    elif s == 2:
        # pre-empt nonRT and run RT
        if (scl - mc) > 0:
            pre_empted_service_time = (scl - mc)
            n_nonrt = n_nonrt + 1
        scl = mc + serviceTime_rt
        n_rt = n_rt - 1
        rt_array.append(scl-rt_queue.pop(0))
        s = 1
    record_global_vars()

def nonrt_arrived():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b, mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df, iat_nonrt_mu, iat_rt_mu, serviceTime_rt_mu, serviceTime_nonrt_mu
    mc = nonRTCL
    n_nonrt = n_nonrt + 1
    nonrt_queue.append(mc)
    nonRTCL = mc + iat_nonrt
    if n_nonrt == 1 and s == 0:
        scl = mc + serviceTime_nonrt
        s = 2
        n_nonrt = n_nonrt - 1
    record_global_vars()

def service_completed():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b, mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df, iat_nonrt_mu, iat_rt_mu, serviceTime_rt_mu, serviceTime_nonrt_mu
    mc = scl
    if s == 2:
        nonrt_array.append(mc-nonrt_queue.pop(0))
    if n_rt > 0:
         # Check RT queue
        scl = mc + serviceTime_rt
        s = 1
        n_rt = n_rt - 1
        rt_array.append(scl-rt_queue.pop(0))
    elif n_nonrt > 0:
         # Check nonRT queue
        if pre_empted_service_time > 0:
            scl = mc + pre_empted_service_time
            pre_empted_service_time = 0
        else:
            scl = mc + serviceTime_nonrt
        s = 2
        n_nonrt = n_nonrt - 1
    else:
        s = 0
    record_global_vars()

def record_global_vars():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b,mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    series_obj = pd.Series( [mc,rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time], index=df.columns )
    df = df.append(series_obj, ignore_index=True)
    # print(df.iloc[-1].to_frame().T)

def export_to_excel():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b,mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    writer = pd.ExcelWriter('vaputra_task2pt2.xlsx')
    df.to_excel(writer)
    writer.save()
    print('Output is written successfully to Excel File.')

def randomized_param():
    global rt_queue, nonrt_queue, rt_array, nonrt_array,m,b,mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    iat_rt = -(iat_rt_mu)*math.log(random.random())
    iat_nonrt = -(iat_nonrt_mu)*math.log(random.random())
    serviceTime_rt = -(serviceTime_rt_mu)*math.log(random.random())
    serviceTime_nonrt = -(serviceTime_nonrt_mu)*math.log(random.random())

def next_event():
    # {event(int):value}
    clock_dict= {0:rtcl, 1:nonRTCL, 2:scl}
    sorted_clock = sorted(clock_dict.items(), key=lambda kv: kv[1])
    sorted_clock_dict = collections.OrderedDict(sorted_clock)
    if s == 0:
        sorted_clock_dict.pop(2)
    return next(iter(sorted_clock_dict))

def get_result():
    global rt_array, nonrt_array, m, b

    # Find mean
    del rt_array[:b]
    del nonrt_array[:b]

    temp_rt_arr = copy.copy(rt_array)
    temp_nonrt_arr = copy.copy(nonrt_array)

    Xi_rt = []
    Xi_nonrt = []
    # print(sum(nonrt_array)/len(nonrt_array))
    # print(sum(rt_array)/len(rt_array))
    for i in range(m-1):
        Xi_rt.append(sum(temp_rt_arr[:b])/b)
        del temp_rt_arr[:b]
        Xi_nonrt.append(sum(temp_nonrt_arr[:b])/b)
        del temp_nonrt_arr[:b]
    mean_rt = sum(Xi_rt)/(m-1)
    mean_nonrt = sum(Xi_nonrt)/(m-1)
    print("RT mean response time: ", mean_rt)
    print("nonRT mean response time: ", mean_nonrt)
    
    
    # Find percentile
    np_rt_arr = np.array(rt_array)
    rt_percentile = np.percentile(np_rt_arr, 95)
    np_nonrt_arr = np.array(nonrt_array)
    nonrt_percentile = np.percentile(np_nonrt_arr, 95)

    print("RT 95-percentile response time: ", rt_percentile)
    print("nonRT 95-percentile response time: ", nonrt_percentile)

    # Find percentile 95th confidence
    rt_s = 0
    nonrt_s = 0
    z = 1.96

    counter_rt = 0
    for val in Xi_rt:
        counter_rt += (val-mean_rt)**2
    rt_s = math.sqrt(counter_rt/(m-2))

    counter_nonrt = 0
    for val in Xi_nonrt:
        counter_nonrt += (val-mean_nonrt)**2
    nonrt_s = math.sqrt(counter_nonrt/(m-2))

    rt_lower_confidence = mean_rt - ((z*rt_s)/(math.sqrt(m-1)))
    rt_upper_confidence = mean_rt + ((z*rt_s)/(math.sqrt(m-1)))
    print("RT Confidence intervals response time: ({}, {})".format(rt_lower_confidence,rt_upper_confidence))

    nonrt_lower_confidence = mean_nonrt - ((z*nonrt_s)/(math.sqrt(m-1)))
    nonrt_upper_confidence = mean_nonrt + ((z*nonrt_s)/(math.sqrt(m-1)))
    print("nonRT Confidence intervals response time: ({}, {})".format(nonrt_lower_confidence,nonrt_upper_confidence))




main()
get_result()

# clock_dict= {0:rtcl, 1:nonRTCL, 2:scl}
# sorted_clock = sorted(clock_dict.items(), key=lambda kv: kv[1])
# sorted_clock_dict = collections.OrderedDict(sorted_clock)
# print(next(iter( sorted_clock_dict.items() )))

# s_event = sched.scheduler(time.time, time.sleep)
# def do_something(sc): 
#     global mc
#     print("Doing stuff...")
#     # do your stuff
#     mc = mc + 1
#     print(mc)
#     s_event.enter(1, 1, do_something, (sc,))

# s_event.enter(1, 1, do_something, (s_event,))
# s_event.run()