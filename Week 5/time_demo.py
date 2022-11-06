import time

print(time.time())
print(time.gmtime(2147483647))
print(time.localtime())

print('=' * 40)
timeList = ['monotonic', 'perf_counter', 'process_time', 'thread_time', 'time']

for clock in timeList:
    print('CLOCK INFO FOR {}: {}'.format(clock, time.get_clock_info(clock)))
    print('-------------')

print('=' * 40)

tehranTime = time.localtime()

print('{}-{}-{} \t {}:{}:{}'.format(tehranTime.tm_mday,
                                    tehranTime.tm_mon,
                                    tehranTime.tm_year,
                                    tehranTime.tm_hour,
                                    tehranTime.tm_min,
                                    tehranTime.tm_sec))


