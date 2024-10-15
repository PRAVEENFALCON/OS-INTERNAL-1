import matplotlib.pyplot as plt

print("FIRST COME FIRST SERVE SCHEDULING")
n = int(input("Enter number of processes: "))
processes = {}

for i in range(n):
    key = "P" + str(i + 1)
    arrival_time = int(input(f"Enter arrival time of process {key}: "))
    burst_time = int(input(f"Enter burst time of process {key}: "))
    processes[key] = [arrival_time, burst_time]

processes = dict(sorted(processes.items(), key=lambda item: item[1][0]))

ET = []
TAT = []
WT = []

for i in range(len(processes)):
    if i == 0:
        ET.append(processes[list(processes.keys())[i]][0] + processes[list(processes.keys())[i]][1])
    else:
        ET.append(ET[i - 1] + processes[list(processes.keys())[i]][1])

TAT = [ET[i] - processes[list(processes.keys())[i]][0] for i in range(len(processes))]
WT = [TAT[i] - processes[list(processes.keys())[i]][1] for i in range(len(processes))]

RT = []
for i in range(len(processes)):
    if i == 0:
        RT.append(0)
    else:
        RT.append(ET[i - 1] - processes[list(processes.keys())[i]][0])

avg_WT = sum(WT) / n
avg_TAT = sum(TAT) / n
total_time = ET[-1]
throughput = n / total_time

print("Process | Arrival | Burst | Exit | Turn Around | Wait | Response")
for i in range(n):
    process_key = list(processes.keys())[i]
    print(f"  {process_key}    |   {processes[process_key][0]}    |  {processes[process_key][1]}  | {ET[i]}  |   {TAT[i]}     | {WT[i]}  |   {RT[i]}")

print("Average Waiting Time:", avg_WT)
print("Average Turnaround Time:", avg_TAT)
print("Throughput:", throughput, "processes/unit time")

plt.figure(figsize=(10, 3))
current_time = 0
for i in range(n):
    plt.barh(y=0, width=processes[list(processes.keys())[i]][1], left=current_time, edgecolor='black')
    plt.text(x=current_time + processes[list(processes.keys())[i]][1] / 2, 
             y=0, 
             s=list(processes.keys())[i], 
             ha='center', 
             va='center', 
             color='white')
    current_time += processes[list(processes.keys())[i]][1]

plt.yticks([])
plt.xticks(range(current_time + 1))
plt.xlabel("Time")
plt.title("Gantt Chart")
plt.show()
