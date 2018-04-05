from queue import Queue
from queue import PriorityQueue

class process(object):
 	def __init__(self, pid, arrival, burst):
 		self.pid = pid
 		self.arrival = arrival
 		self.burst = burst

class processpriority(object):
 	def __init__(self, pid, arrival, burst, priority):
 		self.pid = pid
 		self.arrival = arrival
 		self.burst = burst
 		self.priority = priority
 		
def fcfs(plist):
	arrived = []
	response = {}
	readyQ = Queue()
	clock = 0
	idleTime = 0
	waitTime = 0
	responseTime = 0
	turnaroundTime = 0
	print("Simulation starting: ") 

	while True:

		for p in plist:
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put(p)
				arrived.append(p)
				continue

		if not readyQ.empty():
			peek = readyQ.queue
			curr = peek[0] # process next in queue

			if curr.burst != 0 and curr.burst != 1:
				print(clock, curr.pid, "running")
				if curr not in response:
					response[curr] = clock
				curr.burst -= 1
				clock += 1

			elif curr.burst == 1:
				print(clock, curr.pid, "running")
				curr.burst -= 1
				#print(clock, curr.pid, "finished")
				clock += 1
				readyQ.get()
				turnaroundTime += clock - curr.arrival

				# get the next process in queue and calculate wait time
				if not readyQ.empty():
					nextonQ = readyQ.queue
					nextp = nextonQ[0]
					waitTime += (clock - nextp.arrival)
					#responseTime += clock


		if readyQ.empty() and len(arrived) != len(plist):
			print("idling...........")
			idleTime += 1
			clock += 1

		if len(arrived) == len(plist) and readyQ.empty():
			# indicates last process is finished
			#responseTime += clock
			for item in response:
				responseTime += response[item] - item.arrival

			print("Average waiting time:", round(waitTime/len(plist),2))
			print("Average response time:", round(responseTime/len(plist),2))
			print("Average turnaround time:", turnaroundTime/len(plist))
			print("Average CPU usage:", str(((clock-idleTime)/clock)*100)+ "%")
			return

def sjf(plist):
	arrived = []
	readyQ = PriorityQueue()
	clock = 0
	count = 0
	print("Simulation starting: ") 
	flag = 0		#needed for nonpremptive algo
	while True:
		for p in plist:
		#	if(flag):
		#		print(clock, curr.pid, "exp")
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put((p.burst, p))
				arrived.append(p)
				continue

		if(flag == 0):				
		#It's a tuple. so use peek[0][1]
			peek = readyQ.queue
			curr = peek[0][1] # process next in queue
			readyQ.get()
			flag = 1
		#	print('curr.pid curr.burst and flag', curr.pid, curr.burst, flag)
			
		if curr.burst != 0 and curr.burst != 1:
			print(clock, curr.pid, "running")
			curr.burst -= 1
			clock += 1

		elif curr.burst == 1:
			print(clock, curr.pid, "running")
			curr.burst -= 1
			#print(clock, curr.pid, "finished")
			clock += 1
#why is this not working??? it is not removing the finished process from ready queue *********************************************
			flag = 0
			count += 1
		
		if count == len(plist):
		#	print("exit")
			# indicates last process is finished
			return

# check during each arrival if burst is less than current, if so append to queue
# maintain queue of [process burst][burst]
def srtf(plist):
	arrived = []
	response = {}
	readyQ = PriorityQueue()
	clock = 0
	idleTime = 0
	waitTime = 0
	responseTime = 0
	turnaroundTime = 0
	print("Simulation starting: ") 

	while True:

		for p in plist:
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put((p.burst, p))
				arrived.append(p)
				continue

		if not readyQ.empty():
			peek = readyQ.queue
			#peak [0][0] is burst
			#peak [0] [1] is process
			# print(peek[0][0])
			curr = peek[0][1] # process next in queue
			# print("curr is ", curr.pid, "with burst", curr.burst)


			if curr.burst != 0 and curr.burst != 1:
				print(clock, curr.pid, "running")

				if curr not in response:
					response[curr] = clock
				curr.burst -= 1
				clock += 1
				continue

			elif curr.burst == 1:
				print(clock, curr.pid, "running")
				curr.burst -= 1
				#print(clock, curr.pid, "finished")
				clock += 1
				readyQ.get()
				turnaroundTime += clock - curr.arrival

				# get the next process in queue and calculate wait time
				if not readyQ.empty():
					nextonQ = readyQ.queue
					nextp = nextonQ[0][1]
					waitTime += (clock - nextp.arrival)
					#responseTime += clock


		if readyQ.empty() and len(arrived) != len(plist):
			print("idling...........")
			idleTime += 1
			clock += 1

		if len(arrived) == len(plist) and readyQ.empty():
			# indicates last process is finished
			#responseTime += clock
			for item in response:
				responseTime += response[item] - item.arrival

			print("Average waiting time:", round(waitTime/len(plist),2))
			print("Average response time:", round(responseTime/len(plist),2))
			print("Average turnaround time:", turnaroundTime/len(plist))
			print("Average CPU usage:", str(((clock-idleTime)/clock)*100)+ "%")
			return

def priorityp(plist):
	arrived = []
	response = {}
	readyQ = PriorityQueue()
	clock = 0
	idleTime = 0
	waitTime = 0
	responseTime = 0
	turnaroundTime = 0
	print("Simulation starting: ") 

	while True:

		for p in plist:
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put((p.priority, p))
				arrived.append(p)
				continue

		if not readyQ.empty():
			peek = readyQ.queue
			#peak [0][0] is burst
			#peak [0] [1] is process
			# print(peek[0][0])
			curr = peek[0][1] # process next in queue
			# print("curr is ", curr.pid, "with burst", curr.burst)


			if curr.burst != 0 and curr.burst != 1:
	#			print(clock, curr.pid, "running")

				if curr not in response:
					response[curr] = clock
				curr.burst -= 1
				clock += 1
				continue

			elif curr.burst == 1:
				print(clock, curr.pid, "running")
				curr.burst -= 1
				#print(clock, curr.pid, "finished")
				clock += 1
				readyQ.get()
	#			peek = readyQ.queue
	#			curr = peek[0][1]
	#			print('flag should be zero and curr.pid',curr.pid)
				turnaroundTime += clock - curr.arrival

				# get the next process in queue and calculate wait time
				if not readyQ.empty():
					nextonQ = readyQ.queue
					nextp = nextonQ[0][1]
					waitTime += (clock - nextp.arrival)
					#responseTime += clock


		if readyQ.empty() and len(arrived) != len(plist):
			print("idling...........")
			idleTime += 1
			clock += 1

		if len(arrived) == len(plist) and readyQ.empty():
			# indicates last process is finished
			#responseTime += clock
			for item in response:
				responseTime += response[item] - item.arrival

			print("Average waiting time:", round(waitTime/len(plist),2))
			print("Average response time:", round(responseTime/len(plist),2))
			print("Average turnaround time:", turnaroundTime/len(plist))
			print("Average CPU usage:", str(((clock-idleTime)/clock)*100)+ "%")
			return


def prioritynp(plist):
	arrived = []
	readyQ = PriorityQueue()
	clock = 0
	count = 0
	print("Simulation starting: ") 
	flag = 0		#needed for nonpremptive algo
	while True:
		for p in plist:
		#	if(flag):
		#		print(clock, curr.pid, "exp")
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put((p.priority, p))
				arrived.append(p)
				continue

		if(flag == 0):				
		#It's a tuple. so use peek[0][1]
			peek = readyQ.queue
			curr = peek[0][1] # process next in queue
			readyQ.get()
			flag = 1
	#		print('curr.pid curr.burst and flag', curr.pid, curr.burst, flag)
			
		if curr.burst != 0 and curr.burst != 1:
			print(clock, curr.pid, "running")
			curr.burst -= 1
			clock += 1

		elif curr.burst == 1:
			print(clock, curr.pid, "running")
			curr.burst -= 1
			#print(clock, curr.pid, "finished")
			clock += 1
#why is this not working??? it is not removing the finished process from ready queue *********************************************
			flag = 0
			count += 1
		
		if count == len(plist):
#			print("exit")
			# indicates last process is finished
			return
			 
def rr(plist, quantum):

	wait = {}
	response = {}
	firstrun = {}
	completed = []
	readyQ = Queue()
	clock = 0
	idleTime = 0
	waitTime = 0 
	responseTime = 0
	turnaroundTime = 0
	qtime = 0
	enqueue = None

	while True:

		for p in plist:
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.put(p)
				wait[p] = 0
				continue

		if enqueue != None:
			readyQ.put(enqueue)
			enqueue = None

		if not readyQ.empty():
			peek = readyQ.queue
			curr = peek[0] # process next in queue

		#for i in range(0,quantum):
		if qtime <= quantum:

			# this loops twice if the burst is not done
			if curr.burst != 1 and curr.burst != 0:
				print(clock, curr.pid, "running")
				for k in wait:
					if curr != k:
						wait[k] += 1
				if curr not in response:
					response[curr] = clock
				curr.burst -= 1
				clock += 1

			elif curr.burst == 1:
				print(clock, curr.pid, "running")

				curr.burst -= 1
				clock += 1
				print(clock, curr.pid, "finished")
				completed.append(curr)
				#readyQ.get()
				turnaroundTime += clock - curr.arrival

			# get the next process in queue and calculate wait time
			if not readyQ.empty():
				nextonQ = readyQ.queue
				nextp = nextonQ[0]

			qtime += 1

			if qtime == quantum:
				enqueue = readyQ.get()
				#readyQ.put(enqueue)
				qtime = 0

		if readyQ.empty() and len(arrived) != len(plist):
			print("idling...........")
			idleTime += 1
			clock += 1

		if len(completed) == len(plist):
			# indicates last process is finished
			for item in wait:
				waitTime += wait[item]

			for item in response:
				responseTime += response[item] - item.arrival

			print("Average waiting time:", round(waitTime/len(plist),2))
			print("Average response time:", round(responseTime/len(plist),2))
			print("Average turnaround time:", round(turnaroundTime/len(plist),2))
			print("Average CPU usage:", str(((clock-idleTime)/clock)*100)+ "%")
			return


#don't need a queue in here. Just a normal list is fine for readyQ	
def HRRN(plist):
	arrived = []
	response = {}
	readyQ = []
	clock = 0
	idleTime = 0
	waitTime = 0
	responseTime = 0
	turnaroundTime = 0
	print("Simulation starting: ") 
	flag = 0
	count = 0
	while True:
		for p in plist:
			if p.arrival == clock:
				print(clock, p.pid, "arriving")
				readyQ.append(p)
				arrived.append(p)
				continue
	#	for t in readyQ:
	#		print(t.pid, t.arrival, t.burst)
		
		if(flag == 0):
			flag = 1
		#	print('flag', flag)
			max = 0
			for t in readyQ:
		#		print('t.pid clock t.arrival t.burst',t.pid, clock, t.arrival, t.burst)
				val = float((clock - t.arrival) / t.burst)
		#		print('val',val)
				if(max <= val):
					max = val
					maxt = t
			curr = maxt
		#	print('curr',curr.pid)
			readyQ.remove(curr)

		if curr.burst != 0 and curr.burst != 1:
			print(clock, curr.pid, "running")
			if curr not in response:
				response[curr] = clock
			curr.burst -= 1
			clock += 1

		elif curr.burst == 1:
			print(clock, curr.pid, "running")
			curr.burst -= 1
			#print(clock, curr.pid, "finished")
			clock += 1
			flag = 0
			count += 1
		
		if(count == len(plist)):
			break
				
	return


def main():
	processes = []
	
	play = int(input("Which algorithm would you like to run: (1) FCFS, (2) SJF, (3) SRTF?, (4) Priority preemptive, (5) Priority non-preemptive, (6) RR, (7) HRRN"))
	
	if(play == 4 or play == 5):
		print('processid\tarrival time\tbursttime\tpriority')
		while(1):
			inputstr = input()
			pieces = list(map(int,inputstr.split()))
			if (pieces[0] == 0) and (pieces[1] == 0) and (pieces[2] == 0) and (pieces[3] == 0):
				break

			p = processpriority(pieces[0], pieces[1], pieces[2], pieces[3])
			processes.append(p)

	else:
		print('processid\tarrival time\tbursttime')
		while(1):
			inputstr = input()
			pieces = list(map(int,inputstr.split()))
			if (pieces[0] == 0) and (pieces[1] == 0) and (pieces[2] == 0):
				break

			p = process(pieces[0], pieces[1], pieces[2])
			processes.append(p)

	if play == 1:
		fcfs(processes)
	elif play == 2:
		sjf(processes)
	elif play == 3:
		srtf(processes)
	elif play == 4:
	#preemptive
		priorityp(processes)
	elif play == 5:
		prioritynp(processes)
	elif play == 6:
		quan = int(input("Enter quantum size: "))
		rr(processes, quan)
	elif play == 7:
		HRRN(processes)
	else:
		print('choose properly')

main()
