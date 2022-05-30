import multiprocessing
import sys
from stratumClientComponent import *

def main(uri,port,user,password):
    print("start test")
    #initialization of the class
    talker = StratumClientTalker()
    #creation of the queues
    solutionQ = multiprocessing.Queue()
    workQ = multiprocessing.Queue()
    addWorkerQ = multiprocessing.Queue()
    respQ = multiprocessing.Queue()
    #launching the method with the correct parameters
    stratumWorker = multiprocessing.Process(target=talker.launchTalker,args=(uri,port,solutionQ,workQ,addWorkerQ,respQ,))
    stratumWorker.start()
    
    #let s see if we can successfully receive a couple of works
    #im only printing the job id for simplicity
    print(str(workQ.get().job_id))
    print(str(workQ.get().job_id))

    #now let s see what happens if we add a worker
    addWorkerQ.put(Worker(user,password))
    response = respQ.get()
    print("response - id: "+str(response.sid)+ " method: " + response.method + " invalue: " + response.invalue + " result: " + str(response.result) + " reason: " + str(response.reason))

    #let s send a fake solution and see what happens (unfortunately I don't have a realtime valid solution to test xD)
    solutionQ.put(Solution("fake","1111","fake","fake","fake"))

    response = respQ.get()
    print("response - id: "+str(response.sid)+ " method: " + response.method + " invalue: " + response.invalue + " result: " + str(response.result) + " reason: " + str(response.reason))




if __name__ == "__main__":
    user = "1068858.my"
    password = "eheheh"
    uri = "stratum.aikapool.com"
    port = 7915

    main(uri,port,user,password)
