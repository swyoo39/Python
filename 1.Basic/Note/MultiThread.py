# # Before
# total1 = 0

# for i in range(0, 100000000):
#   total1 += i
# print(total1)

# After
from concurrent.futures import thread
from threading import Thread
def calc(start, end):
  total = 0
  for i in range(start, end):
    total += i
  print(total)

if __name__ == "__main__":
  start, end = 0, 100000000
  thr1 = Thread(target=calc, args=(start, end))

  thr1.start()
  thr1.join()

# MultiThread 와 MultyProcessing 의 차이
# MultiThread는 하나의 문제를 나눠서 협업하는 거고
# Multiprocessing은 여러개의 문제를 각각 같이 협업하는 것이다. 