from Common.log import log1

try:
    log1.info('开始测试')
    r = 10/0
    log1.info('result:',r)
except ZeroDivisionError as f:
    log1.error('test',exc_info=1)
log1.info('end')