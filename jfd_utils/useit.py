#!/usr/bin/env python3



################################
# JFD
import jfd_utils
###############################

from pprint import pprint

def somefun():
  jfd_utils.jprint(True, "==== somefun() ====")

  x = [
    {'apple': [1,2,3], 'orange':[4,5,6]},
    {'pear': [7,8,9], 'pineapple':[10,11,12]},
    {'durian':[13,14,15], 'banana':[16,17,18]}
    ]

  print("plain print")
  print(x)
  print("pprint")
  pprint(x)




if '__main__' == __name__:
  jfd_utils.jprint(True, "---- __main__ -----")
  somefun()
  #  sys.exit(main(sys.argv[1:]))


