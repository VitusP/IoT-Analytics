import pandas as pd

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
df = pd.DataFrame(columns=['MC', 'RTCL', 'nonRTCL', 'n_RT', 'n_nonRT', 'SCL', 's', 'Pre-empted-service-time'])


## Main method
def main():
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    iat_rt = int(input("Enter IAR of RT messages: "))
    iat_nonrt = int(input("Enter IAR of non-RT messages: "))
    serviceTime_rt = int(input("Enter service time of RT messages: "))
    serviceTime_nonrt = int(input("Enter service time of non-RT messages: "))
    max_mc = int(input("Do the hand simulation until MC: "))
    record_global_vars()

    while mc <= max_mc:
        mc = mc + 1
        if mc == rtcl:
            rt_arrived()
        if mc == nonRTCL:
            nonrt_arrived()
        if mc == scl:
            service_completed()
    print(df)
    export_to_excel()


## Helper Methods
def rt_arrived():
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt
    mc = rtcl
    n_rt = n_rt + 1
    rtcl = mc + iat_rt
    
    if n_rt == 1 and s == 0:
        scl = mc + serviceTime_rt
        n_rt = n_rt - 1
        s = 1
    elif s == 2:
        # pre-empt nonRT and run RT
        if (scl - mc) > 0:
            pre_empted_service_time = (scl - mc)
            n_nonrt = n_nonrt + 1
        scl = mc + serviceTime_rt
        n_rt = n_rt - 1
        s = 1
    record_global_vars()

def nonrt_arrived():
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt
    mc = nonRTCL
    n_nonrt = n_nonrt + 1
    nonRTCL = mc + iat_nonrt

    
    if n_nonrt == 1 and s == 0:
        scl = mc + serviceTime_nonrt
        s = 2
        n_nonrt = n_nonrt - 1
    record_global_vars()

def service_completed():
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt
    mc = scl
    if n_rt > 0:
         # Check RT queue
        scl = mc + serviceTime_rt
        s = 1
        n_rt = n_rt - 1
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
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    series_obj = pd.Series( [mc,rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time], index=df.columns )
    df = df.append(series_obj, ignore_index=True)
    #print(df)

def export_to_excel():
    global mc, rtcl, nonRTCL, n_rt, n_nonrt, scl, s, pre_empted_service_time, iat_rt, iat_nonrt, serviceTime_rt, serviceTime_nonrt, df
    writer = pd.ExcelWriter('vaputra_task2pt1.xlsx')
    df.to_excel(writer)
    writer.save()
    print('Output is written successfully to Excel File.')

main()

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