import time
import datetime

currentdateTime = datetime.datetime.now()
tableoftime = [1, 60, 3600, 3600 * 24, 3600 * 24 * 7, 3600 * 24 * 30, 3600 * 24 * 365]
diffgap = ["s", "m", "h", "d", "w", "y"]

print(currentdateTime)


def timediffCalc(t):
    diff = int(time.time() - t)
    
    if diff == 0:
        print("Just now")
        return diff
    else:
        print("Not now")
        i = len(diffgap) - 1
        for interval in reversed(tableoftime):
            if diff >= interval:
                v = int(diff / interval)
                return f"{v}{diffgap[i]}"
            i -= 1
    return diff


print(timediffCalc(1689474854.9702244))
