# searching min weights in graphs
import math

def get_link_peaks(peak, D):
     for i, weight in enumerate(D[peak]):
          if weight > 0:
               yield i

def arg_min(LastStr, ViewedPeaks):
     minim = -1
     m = max(LastStr)
     for i, temp in enumerate(LastStr):
          if temp < m and i not in ViewedPeaks:
               m = temp
               minim = i

     return minim


D = ((0, 2, 2, 1, 0, 0),            # weights of branches
     (3, 0, 4, 0, 0, 0),
     (4, 5, 0, 0, 2, 5),
     (3, 0, 0, 0, 0, 2),
     (0, 0, 7, 0, 0, 4),
     (0, 0, 5, 9, 4, 0))

Num = len(D)
LastStr = [math.inf] * Num

peak = 0
ViewedPeaks = {peak}
LastStr[peak] = 0

while peak != -1:                                 #while not all peaks are viewed
     for j in get_link_peaks(peak, D):            # looking through all linked peaks
          if j not in ViewedPeaks:
               wTemp = LastStr[peak] + D[peak][j]
               if wTemp < LastStr[j]:
                    LastStr[j] = wTemp

     peak = arg_min(LastStr, ViewedPeaks)     # choosing new peak with min weight
     if peak > 0:
          ViewedPeaks.add(peak)

print(LastStr)