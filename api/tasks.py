from re import T
from celery import shared_task 
from time import sleep

@shared_task
def task2():
    print('sending mail in background...')
    import time
    print(2+3)
    for i in range(10,0,-1):
        print(f"Remaining {i} seconds...", end="\r", flush=True)
        time.sleep(1)
    print('sending mail succesfully done')
    return True