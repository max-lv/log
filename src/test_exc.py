
import log

try:
    a = 5/0
except:
    log.error('woah an error',exc_info=True)
    log.log('no trace')
    log.warn('after trace',exc_info=True)

log.log('normal log')
