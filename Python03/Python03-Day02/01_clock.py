import time

def clock():
    while True:
        # 在此处先获取当前时间
        cur_time = time.localtime()
        t_hms = cur_time[3:6]
        # hour, minute, second = t_hms

        print("%02d:%02d:%02d" % t_hms)
        time.sleep(1)
        


clock()