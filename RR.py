
import matplotlib.pyplot as plt
from collections import deque

def round_robin(processes, burst_time, arrival_time, quantum):
    n = len(processes)
    remaining_burst_time = burst_time[:]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    response_time = [0] * n
    gantt_chart = []
    t = 0
    process_queue = deque()
    process_start_time = [-1] * n

    while True:
        for i in range(n):
            if arrival_time[i] <= t and remaining_burst_time[i] > 0 and i not in process_queue:
                process_queue.append(i)

        if process_queue:
            i = process_queue.popleft()
            if process_start_time[i] == -1:
                process_start_time[i] = t
            start_time = t
            burst = min(quantum, remaining_burst_time[i])
            t += burst
            remaining_burst_time[i] -= burst

            if remaining_burst_time[i] == 0:
                waiting_time[i] = t - burst_time[i] - arrival_time[i]
                turnaround_time[i] = t - arrival_time[i]
            else:
                process_queue.append(i)
            gantt_chart.append((processes[i], start_time, t))
        else:
            next_arrival = min([arrival_time[i] for i in range(n) if arrival_time[i] > t], default=None)
            if next_arrival is not None:
                t = next_arrival
            else:
                break

    for i in range(n):
        if remaining_burst_time[i] == 0 and turnaround_time[i] == 0:
            turnaround_time[i] = t - arrival_time[i]
        if response_time[i] == 0:
            response_time[i] = turnaround_time[i] - burst_time[i]

    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    avg_response_time = sum(response_time) / n
    total_time = max(t, max([arrival_time[i] + burst_time[i] for i in range(n)]))
    throughput = n / total_time if total_time > 0 else 0

    print("Gantt Chart:")
    plt.figure(figsize=(10, 3))
    for process, start, end in gantt_chart:
        plt.barh(y=0, width=end - start, left=start, edgecolor='black')
        plt.text(x=start + (end - start) / 2, y=0, s=f"P{process}", ha='center', va='center', color='white')

    plt.yticks([])
    plt.xticks(range(int(t) + 1))
    plt.xlabel("Time")
    plt.title("Gantt Chart")
    plt.show()

    print("\nProcess\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time\tResponse Time")
    for i in range(n):
        print(f"P{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}\t\t{response_time[i]}")

    print(f"\nAverage Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Response Time: {avg_response_time:.2f}")
    print(f"Throughput: {throughput:.2f} processes/unit time")

n = int(input("Enter the number of processes: "))
processes = []
burst_time = []
arrival_time = []

for i in range(n):
    process_id = i + 1
    processes.append(process_id)
    bt = int(input(f"Enter the burst time for process P{process_id}: "))
    burst_time.append(bt)
    at = int(input(f"Enter the arrival time for process P{process_id}: "))
    arrival_time.append(at)

quantum = int(input("Enter the time quantum: "))
round_robin(processes, burst_time, arrival_time, quantum)
