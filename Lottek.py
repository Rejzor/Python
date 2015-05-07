#-------------------------------------------------------------------------------
# Name:        random sample 6 numbers from 1 to 49
# Purpose:
#
# Author:      Rarez
#
# Created:     05-05-2015
# Copyright:   (c) Rarez 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random as r
liczby = range(1,50)
losowanie = r.sample(liczby,6)
print(losowanie)