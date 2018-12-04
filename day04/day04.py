import re
import datetime as dt
from collections import Counter, defaultdict, OrderedDict


class Puzzle:

    def __init__(self, test=False):
        filename = "test.txt" if test else "input.txt"
        self.data = self.load_into_memory(filename)
        
    def load_into_memory(self, filename):
        """load input into memory"""
        data = {}
        recomp = re.compile(r'\[(.+)\]|Guard #([0-9]+)|(wakes)|(asleep)')
        with open(filename) as f:
            for line in f:
                record = re.findall(recomp, line)
                timestamp = dt.datetime.strptime(record[0][0], '%Y-%m-%d %H:%M')
                event = ''.join(record[1])
                data[timestamp] = event
        return OrderedDict(sorted(data.items()))

    def get_nap_times(self):
        """
        Returns dictionary of Counters of each guard and 
        the number of times they have been asleep in each minute.
        e.g. {guard_ID: {5: 1, 6: 2, 7:2, 8: 2, 9: 3, 10: 3, ... , 58: 1}}
        """
        nap_times = defaultdict(Counter)
        for timestamp, event in self.data.items():
            if event == 'asleep':
                asleep = timestamp.minute
            elif event == 'wakes':
                nap = range(asleep, timestamp.minute)
                nap_times[current_guard] += Counter(nap)
            else:
                current_guard = int(event)
        return nap_times

    def solve_part1(self):
        """
        Returns result for part 1:
        Finds the guard that has the most minutes asleep and
        identifies the minute they are asleep the most.
        Returns the ID of the guard * minute most asleep.
        """
        nap_times = self.get_nap_times()

        mx = 0
        for guard_id, minutes in nap_times.items():
            total = sum(minutes.values())
            if total > mx:
                mx = total
                sleepiest_guard = guard_id
        
        most_common_minute = nap_times[sleepiest_guard].most_common(1)[0][0]

        return sleepiest_guard * most_common_minute
            
    def solve_part2(self):
        """
        Returns result for part 2:
        Identifies the most frequency napped minute of any guard.
        Returns ID of  guard * minute most frequently napped.
        """
        nap_times = self.get_nap_times()

        mx = 0
        for guard, minutes in nap_times.items():
            common_minute, freq = minutes.most_common(1)[0]
            if freq > mx:
                sleepiest_minute = (guard, common_minute)
                mx = freq
        
        return sleepiest_minute[0] * sleepiest_minute[1]

        

if __name__ == "__main__":
    puzzle = Puzzle()
    print("Part 1 = {}".format(puzzle.solve_part1()))
    print("Part 2 = {}".format(puzzle.solve_part2()))