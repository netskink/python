import sys
import traceback
import threading

from inspect import currentframe, getframeinfo

# leading_skip: specify how much of FQPN you want to skip
# by default it skips none
def get_filename(leading_skip=0):
    # current frame is this function
    cf = currentframe()
    # previous frame is my print
    pf = cf.f_back
    # previous previous frame is who called my print
    ppf = pf.f_back
    #print("ppf = ")
    #print(ppf)

    return getframeinfo(ppf).filename[leading_skip:]

def get_linenumber():
    cf = currentframe()
    pf = cf.f_back
    ppf = pf.f_back
    return ppf.f_lineno

def get_thread_id():
    # this platform version does not have native id.
    #tid = threading.get_native_id()
    tid = threading.get_ident()
    # truncate to just 4 digits
    tid = tid % 9999
    return tid

# this will parse the variable arguments
# and determine if it has a leading boolean
# which determines if the text string
# should be printed or not.
def parse_args(*args):

    # Is the first argument a True/False?
    # If not, return the entire message
    # If yes and its true, return the second parm, the message
    # If yes and its false, return None

    if isinstance(args[0], bool):
        if False == args[0]:
            return None # IGNORE message
        else:
            return args[1] # return message
    else:
        return args[0] # return message


#
# Selectively print message including 
# file name and line number of caller.
#
# usage:
# jprint("some message")
# jprint("some message%s"%(some_var))
# jprint(True, "some message%s"%(some_var))
# jprint(False, "some message%s"%(some_var))  # message is not printed
def jprint(*args):

    msg = parse_args(*args)
    if msg != None:
        print("%d:%s:%s "%( get_thread_id(), get_filename(leading_skip=39), get_linenumber() ), end = '', file=sys.stderr)
        print(msg, file=sys.stderr)


#
# Selectively print message including 
# file name and line number of caller.
# Afterwards, print the stack trace.
#
# usage:
# jprint("some message")
# jprint("some message%s"%(some_var))
# jprint(True, "some message%s"%(some_var))
# jprint(False, "some message%s"%(some_var))  # message is not printed
def print_caller(*args):

    msg = parse_args(*args)
    if msg != None:
        print("%d:%s:%s "%( get_thread_id(), get_filename(leading_skip=39), get_linenumber() ), end = '', file=sys.stderr)
        print(msg, file=sys.stderr)
        print("*********", file=sys.stderr)
        # This only works when an exception occurs
        # exc_type, exc_value, exc_traceback = sys.exc_info()
        # traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        # This works all the time
        traceback.print_stack()
        print("*********", file=sys.stderr)

#
#
#
def halt(*args):

    msg = parse_args(*args)
    if msg != None:
        print("%d:%s:%s "%( get_thread_id(), get_filename(leading_skip=39), get_linenumber() ), end = '', file=sys.stderr)
        print(msg, file=sys.stderr)
        print("*********", file=sys.stderr)
        # This only works when an exception occurs
        # exc_type, exc_value, exc_traceback = sys.exc_info()
        # traceback.print_tb(exc_traceback, limit=1, file=sys.stdout)
        # This works all the time
        traceback.print_stack()
        print("*********", file=sys.stderr)
        sys.exit(-1)


def stall(*args):
    msg = parse_args(*args)
    print("*********", file=sys.stderr)

    if msg != None:
        print(msg, file=sys.stderr)

    print("  stall  ", file=sys.stderr)
    print("*********", file=sys.stderr)
    while (True):
        pass

