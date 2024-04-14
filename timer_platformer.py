import time

time_debut = time.time()
while True:
    timer = time.time() - time_debut
    print(time.strftime('%M:%S',time.gmtime(timer)))
    time.sleep(1)
