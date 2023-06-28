import time 
import json
from web import control
from multiprocessing import Process
import multiprocessing
# from led_status import estadoLed

# import led_status

# modo = led_status.estadoLed()


# def estadito():
#     while True:
#         print(modo.value)
#         time.sleep(3)
        
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     Process(target=visualization).start()
#     Process(target=control).start()


control()