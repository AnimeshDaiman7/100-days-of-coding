from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime, endTime, profit):

        jobs = sorted(zip(startTime, endTime, profit),
                      key=lambda x: x[1])

        n = len(jobs)

        end_times = [job[1] for job in jobs]
        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            start, end, money = jobs[i - 1]

            # Find the last job that ends
            # before or exactly when this job starts.
            j = bisect_right(end_times, start, 0, i - 1)

            take = money + dp[j]
            skip = dp[i - 1]

            dp[i] = max(take, skip)

        return dp[n]
