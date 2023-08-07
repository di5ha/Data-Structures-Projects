import queue

class Job:
    def __init__(self, name, priority, execution_time):
        self.name = name
        self.priority = priority
        self.execution_time = execution_time

    def __lt__(self, other):
        # This method is used for comparison in the priority queue
        # Lower priority values have higher priority in the queue
        return self.priority < other.priority

def schedule_jobs(jobs):
    job_queue = queue.PriorityQueue()

    for job in jobs:
        job_queue.put(job)

    while not job_queue.empty():
        next_job = job_queue.get()
        print(f"Scheduling job '{next_job.name}' with priority {next_job.priority} and execution time {next_job.execution_time}")

if __name__ == "__main__":
    # Example job list: (name, priority, execution_time)
    jobs = [
        Job("Job1", 2, 5),
        Job("Job2", 1, 3),
        Job("Job3", 3, 8),
        Job("Job4", 1, 2)
    ]

    schedule_jobs(jobs)
