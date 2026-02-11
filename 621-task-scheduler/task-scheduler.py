class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())

        max_count = sum(1 for task in task_counts if task_counts[task] == max_freq)

        intervals = (max_freq - 1) * (n+1)+max_count

        return max(len(tasks),intervals)