
import time
import traceback, sys
from inspect import getframeinfo, stack, getmodule


def caller_frame(stack):
    for frame in stack:
        call_info = getframeinfo(frame[0])
        if __file__ != call_info.filename:
            return call_info


def log(msg, exc_info=False, level="INFO"):
    """ Prints log message in format:
          2018-07-25 23:59:59 - INFO - your_file_name.py:5324 - Log message here
          ^ date during call     ^       ^ calling file  ^ line number  ^ `msg` argument
                                 | `level` keyword argument
    """
    call_info = caller_frame(stack())
    cur_time = time.strftime("%Y-%m-%d %H:%M:%S")

    if exc_info:
        t, v, tb = sys.exc_info()
        if tb != None:
            ex = traceback.format_exception(t, v, tb)
            msg += '\n' + ''.join(ex)

    print(f"{cur_time:<20} - {level:<8} - {call_info.filename:>40}:{call_info.lineno} - {msg}", flush=True)


def info(msg, **kwargs):
    log(msg, level="INFO", **kwargs)

def debug(msg, **kwargs):
    log(msg, level="DEBUG", **kwargs)

def warn(msg, **kwargs):
    log(msg, level="WARN", **kwargs)

def error(msg, **kwargs):
    log(msg, level="ERROR", **kwargs)