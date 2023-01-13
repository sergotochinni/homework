from datetime import datetime

logFileName = ''

def init():
    global logFileName
    now = datetime.now()
    logFileName = now.strftime("%Y%m%d%H%M%S") + '.log'
    f = open(logFileName, 'w')
    f.write(now.strftime("%Y/%M/%D %H:%M:%S") + " Log init.\n")
    f.close()

def writeToLog(info: str):
    if logFileName != '':
        f = open(logFileName, 'a')
        now = datetime.now()
        f.write(now.strftime("%Y/%M/%D %H:%M:%S") + " " + info + '\n')
        f.close()
