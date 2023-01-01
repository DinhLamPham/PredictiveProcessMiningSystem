import pandas as pd

def MakeStatistics(_file):
    minEvent, maxEvent = 100, 0
    actList, perList = [], []

    with open(_file + '.txt', encoding='utf-8') as f:
        keyWordSeparate = f.readline().strip()
        keySeparateInside = f.readline().strip()
        traceLenList = []
        count = 0
        while True:
            currentLine = f.readline()
            if not currentLine:
                break

            count += 1
            # print('reading line: %s ' % count)
            currentTrace = currentLine.strip().split(keyWordSeparate)
            traceLenList.append(len(currentTrace))

            for i in range(len(currentTrace)):
                if not currentTrace[i].split(keySeparateInside)[0] in actList:
                    if currentTrace[i].split(keySeparateInside)[0] != 'START' and currentTrace[i].split(keySeparateInside)[0] != 'END':
                        actList.append(currentTrace[i].split(keySeparateInside)[0])
                if not currentTrace[i].split(keySeparateInside)[1] in perList:

                    if currentTrace[i].split(keySeparateInside)[1] != 'START' and currentTrace[i].split(keySeparateInside)[1] != 'END':
                        perList.append(currentTrace[i].split(keySeparateInside)[1])

            num_event_in_this_trace = len(currentTrace)
            if minEvent > num_event_in_this_trace:
                minEvent = num_event_in_this_trace
            if maxEvent < num_event_in_this_trace:
                maxEvent = num_event_in_this_trace


    print('log: %s' % _file)
    print('minEvent: %s, maxEvent: %s, TotalAct: %s, totalPer: %s' %(minEvent, maxEvent, len(actList), len(perList)))

    return sum(traceLenList) / len(traceLenList)


listLog = ['5_BPIC15_1', '6_BPIC15_2']
resultDf = pd.DataFrame()
for log in listLog:
    avg = [MakeStatistics(log)]
    resultDf[log] = avg

print(resultDf)
# resultDf.to_excel('Average activity summary.xlsx')