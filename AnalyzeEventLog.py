

inputFile = r'media/0 Helpdesk.txt'
with open(inputFile, encoding='utf-8') as f:
    f.readline().strip()
    f.readline().strip()
    count = 0
    minEvent = 1000
    maxEvent = 0
    count4 = 0
    count7 = 0
    while True:
        traceStr = f.readline()
        if not traceStr:
            break
        count += 1
        traces = traceStr.split('!@#')
        if minEvent > len(traces):
            minEvent = len(traces)

        if maxEvent < len(traces):
            maxEvent = len(traces)

        if len(traces) >= 7:
            count7 += 1

        if len(traces) >= 4:
            count4 += 1


    print('%s total traces: %d, minEvent: %d, maxEvent: %d' %(inputFile, count, minEvent, maxEvent))
    print('count4: %d, count6: %d' % (count4, count7))