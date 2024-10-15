
import matplotlib.pyplot as plt

def sjf_scheduling():
    print("SHORTEST JOB FIRST SCHEDULING")
    n = int(input("Enter number of processes: "))
    processes = []
    
    for i in range(n):
        process_id = i + 1
        arrival_time = int(input(f"Enter arrival time of process P{process_id}: "))
        burst_time = int(input(f"Enter burst time of process P{process_id}: "))
        processes.append([process_id, arrival_time, burst_time])
        
    processes.sort(key=lambda x: x[1])
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completion_time = [0] * n
    response_time = [0] * n
    
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    current_time = 0
    completed_processes = 0
    completed = [False] * n
    gantt_chart = []
    gantt_times = []

    while completed_processes < n:
        available_processes = [p for p in processes if p[1] <= current_time and not completed[p[0] - 1]]
        
        if available_processes:
            available_processes.sort(key=lambda x: x[2])
            process = available_processes[0]
            process_id = process[0]
            arrival_time = process[1]
            burst_time = process[2]
            
            if response_time[process_id - 1] == 0:
                response_time[process_id - 1] = current_time - arrival_time
            start_time = current_time
            completion_time[process_id - 1] = start_time + burst_time
            waiting_time[process_id - 1] = start_time - arrival_time
            turnaround_time[process_id - 1] = waiting_time[process_id - 1] + burst_time
            current_time += burst_time
            completed_processes += 1
            completed[process_id - 1] = True
            gantt_chart.append(f"P{process_id}")
            gantt_times.append((start_time, current_time))
        else:
            gantt_chart.append("IDLE")
            gantt_times.append((current_time, current_time + 1))
            current_time += 1

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    avg_response_time = sum(response_time) / n
    total_time = completion_time[-1]
    throughput = n / total_time if total_time > 0 else 0

    print("\nProcess | Arrival Time | Burst Time | Waiting Time | Turnaround Time")
    for i in range(n):
        print(f" P{processes[i][0]} | {processes[i][1]} | {processes[i][2]} | {waiting_time[i]} | {turnaround_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Response Time: {avg_response_time:.2f}")
    print(f"Throughput: {throughput:.2f} processes/unit time")
    print("\nGantt Chart:")
    
    plt.figure(figsize=(10, 3))
    for i in range(len(gantt_chart)):
        if gantt_chart[i] != "IDLE":
            plt.barh(y=0, width=gantt_times[i][1] - gantt_times[i][0], left=gantt_times[i][0], edgecolor='black')
            plt.text(x=gantt_times[i][0] + (gantt_times[i][1] - gantt_times[i][0]) / 2,
                     y=0, s=gantt_chart[i], ha='center', va='center', color='white')

    plt.yticks([])
    plt.xticks(range(int(current_time) + 1))
    plt.xlabel("Time")
    plt.title("Gantt Chart")
    plt.show()

sjf_scheduling()
