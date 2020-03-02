import time

def logger(n):
    time_format = '%Y-%m-%d %X'
    time_current = time.strftime(time_format)
    with open('日志记录','a') as f :
        f.write('%s end action %s\n'%(time_current, n))

def action1(n):
    print('starting action1...')
    logger(n)

def action2(n):
    print('starting action2...')
    logger(n)

def action3(n):
    print('starting action3...')
    logger(n)

action1('hello world!')
action2('ni hao!')
action3('luzhenghao')