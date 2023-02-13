import threading
import time
import datetime
import random

fifo_Tank = []
moteurs =0
roue=0

class my_task():
    name = None
    period = -1
    execution_time = -1
    job = ""
    production = None

    ############################################################################
    def __init__(self, name, period, execution_time, job, fifo_Tank=False):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.job = job
        self.fifo_Tank = fifo_Tank

    ############################################################################
    def run(self):

        # Update last_execution_time

        global fifo_Tank
        global moteurs, roue

        
        print("\n")
        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Starting task ")
        print("\t \t \tJob: " + self.job)

        # fifo_tank

        if (self.fifo_Tank == True):
            if self.name == "Pump2":
                fifo_Tank.append(20)
            if self.name == "Pump1":
                fifo_Tank.append(10)
        
        

        if self.fifo_Tank == False:
            while (len(fifo_Tank) > 0):
                print("read FIFO")

        time.sleep(self.execution_time)
        

        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Ending task ")
        




####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':
    

    last_execution = datetime.datetime.now()

    # Instanciation of task objects

    task_list = []
    task_list.append(my_task(name="Pump2", period=15, execution_time=3, job="Produce 20 Oil", fifo_Tank=True))
    task_list.append(my_task(name="Pump1", period=5, execution_time=2, job="Produce 10 Oil", fifo_Tank=True))
    task_list.append(my_task(name="Pump2", period=15, execution_time=3, job="Produce 20 Oil", fifo_Tank=True))
    task_list.append(my_task(name="Machine 1", period=5, execution_time=5, job="Produce 1 Motore", fifo_Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", fifo_Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", fifo_Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", fifo_Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", fifo_Tank=True))
   
    while (1):
        time_now = datetime.datetime.now()
        print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))

        task_to_run = None

        #  Last task
        priority = {}

        for current_task in task_list[:3]:
            if sum(fifo_Tank) < 55 :
                current_task.run()

        fifo_Tank_total = sum(fifo_Tank)

        for current_task in task_list[3:9]:

            if fifo_Tank_total > 0 :
                if current_task.name =="Machine 1" :
                    current_task.run()
                    fifo_Tank_total -= 25
                    moteurs += 1



                if current_task.name == "Machine 2":
                    current_task.run()
                    fifo_Tank_total -= 5
                    roue += 1

        print(datetime.datetime.now().strftime("%H:%M:%S"), ": nous avons produits {} roues et {} motors ".format(roue, moteurs))


        fifo_Tank =[]

