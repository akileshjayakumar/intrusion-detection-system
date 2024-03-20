# CSCI262 - Assignment 3
# Name: Akilesh Jayakumar
# UOW ID: 7901240
# Submission Date: 24 November 2023


import os
import sys
import time
import statistics as s


SECTION_LINE = "=" * 45
SUBSECTION_LINE = "-" * 40


def print_section_heading(heading):
    print(f"\n{SECTION_LINE}\n{heading}\n{SECTION_LINE}")


def print_subsection_heading(heading):
    print(f"\n{SUBSECTION_LINE}\n{heading}\n{SUBSECTION_LINE}")


def initialInput():
    if len(sys.argv) != 4:
        print("Usage: python3 IDS.py <Events file> <Stats file> <Number of Days>")
        sys.exit(1)
    eventFile = sys.argv[1]
    statsFile = sys.argv[2]
    days = sys.argv[3]
    if not os.path.exists(eventFile):
        print(f"Error: {eventFile} does not exist.")
        sys.exit(1)

    if not os.path.exists(statsFile):
        print(f"Error: {statsFile} does not exist.")
        sys.exit(1)

    if not days.isdigit() or int(days) <= 0:
        print("Error: Number of days must be a positive integer.")
        sys.exit(1)

    return eventFile, statsFile, int(days)


def readEvents(filename):
    line = []

    with open(filename, "r") as fin:
        lines = fin.readlines()

        for each in lines:
            line.append(each.strip())

    return line


def readStats(filename):
    line = []

    with open(filename, "r") as fin:
        lines = fin.readlines()

        for each in lines:
            line.append(each.strip())

    return line


def consistencyCheck(eventData, statsData):
    noOfEventData = int(eventData[0])
    noOfStatsData = int(statsData[0])

    if noOfEventData != noOfStatsData:
        print("\nInconsistency: Number of events in Events and Stats do not match.")
        return False

    for i in range(1, noOfEventData + 1):
        eventNameInEvent = eventData[i].split(":")[0]
        eventNameInStats = statsData[i].split(":")[0]
        if eventNameInEvent != eventNameInStats:
            print(
                f"\nInconsistency: Event name mismatch at line {i}: '{
                    eventNameInEvent}' in Events and '{eventNameInStats}' in Stats."
            )
            return False

    return True


def processEvents(data):
    noOfEvents = int(data[0])
    allWeight = []

    for i in range(1, noOfEvents + 1):
        each = data[i].split(":")
        eventName = each[0]
        eventType = each[1]
        minimum = each[2]
        maximum = each[3]
        weight = each[4]
        if eventType != "C" and eventType != "D":
            print("\nEvent type must be either C or D: ")
            return

        if minimum == "":
            print("\nMinimum values cannot be empty: ")
            return

        if maximum == "":
            print("\nMaximum values cannot be empty: ")
            return

        if weight.find(".") > 0:
            print("\nWeight values must be an integer: ")
            return

        if weight == "":
            print("\nWeight values cannot be empty: ")

        if eventType == "D":
            if minimum.find(".") > 0 or maximum.find(".") > 0:
                print("\nFloat found in a Discrete Event")
                return

        if eventType == "C":
            minimum = "{:.2f}".format(float(minimum))
            maximum = "{:.2f}".format(float(maximum))
        allWeight.append(int(weight))

        print(
            f"Event: {eventName}, Type: {eventType}, Min: {
                minimum}, Max: {maximum}, Weight: {weight}"
        )
    return allWeight


def processStats(data):
    noOfEvents = int(data[0])

    for i in range(1, noOfEvents + 1):
        each = data[i].split(":")
        eventName = each[0]
        mean = each[1]
        standard_deviation = each[2]
        print(
            f"Event: {eventName}, Mean: {
                mean}, Standard Deviation: {standard_deviation}"
        )


def simulateActivity(filename, days, eventData, dataSet):
    print(f"Simulating activity and generating {filename} for {days} days...")
    with open(filename, "w") as fout:
        for i in range(days):
            fout.write(f"Day {i + 1}\n")
            fout.write(f"{len(eventData)-1}\n")

            for j in range(1, len(eventData)):
                eventInfo = eventData[j].split(":")
                eventName, eventType = eventInfo[0], eventInfo[1]
                # j-1 to align with dataSet index
                fout.write(f"{eventName}:{eventType}:{dataSet[j-1][i]}\n")

            fout.write("\n")

    print(
        f"Data for {days} days has been successfully written to {filename}\n")


def generateDataSet(days, eventData, statsData):
    noOfEvents = int(eventData[0])
    activityData = []
    for i in range(days):
        for j in range(1, noOfEvents + 1):
            eData = eventData[j].split(":")
            eventName = eData[0]
            eventType = eData[1]
            minimum = int(eData[2])
            maximum = int(eData[3])
            sData = statsData[j].split(":")
            mean = float(sData[1])
            standardDeviation = float(sData[2])
            dataSet = generateData(
                mean, standardDeviation, days, minimum, maximum, eventType
            )
            activityData.append(dataSet)

    time.sleep(1)
    return activityData


def generateData(mean, standardDeviation, days, minimum, maximum, eventType):
    while True:
        n = s.NormalDist(mu=mean, sigma=standardDeviation)
        samples = n.samples(days)
        for index in range(len(samples)):
            if eventType == "D":
                samples[index] = round(samples[index])
            if eventType == "C":
                samples[index] = round(samples[index], 2)
            if samples[index] < minimum or samples[index] > maximum:
                continue

        if days >= 10:
            if (
                s.mean(samples) < mean * 0.95
                or s.mean(samples) > mean * 1.05
                or s.stdev(samples) < standardDeviation * 0.95
                or s.stdev(samples) > standardDeviation * 1.05
            ):
                continue
            else:
                return samples
        else:
            if (
                s.mean(samples) < mean * 0.9
                or s.mean(samples) > mean * 1.1
                or s.stdev(samples) < standardDeviation * 0.9
                or s.stdev(samples) > standardDeviation * 1.1
            ):
                continue
            else:
                return samples


def readLogs(filename):
    print("Analysing ...")
    data = []
    eventName = []
    with open(filename, "r") as fin:
        fin.readline().strip()
        noOfEvents = int(fin.readline().strip())

        for i in range(noOfEvents):
            eventName.append(fin.readline().strip().split(":")[0])

    with open(filename, "r") as fin:
        fin.readline().strip()
        noOfEvents = int(fin.readline().strip())
        count = 0
        while count < noOfEvents:
            dailyData = []
            while True:
                line = fin.readline().strip()
                if not line:
                    data.append(dailyData)
                    count += 1
                    fin.seek(0)
                    time.sleep(1)
                    print(f"Event number {count} processed")
                    for i in range(2 + count):
                        fin.readline().strip()
                    break
                lineInfo = line.split(":")
                if lineInfo[1] == "D":
                    dailyData.append(int(lineInfo[2]))
                if lineInfo[1] == "C":
                    dailyData.append(round(float(lineInfo[2]), 2))
                for i in range(noOfEvents + 2):
                    fin.readline().strip()
    print("\nBaselineStats.txt Generated\n")
    return data, eventName


def outputData(data, eventName, filename):
    mean = calculateMean(data)
    variance = calculateVariance(data, mean)
    stddev = calculateStddev(variance)
    with open(filename, "a") as fout:
        fout.write(str(len(eventName)))
        for i in range(len(eventName)):
            fout.write(f"\n{eventName[i]}:{str(mean[i])}:{str(stddev[i])}")

    return mean, stddev


def calculateMean(data):
    mean = []
    for index, value in enumerate(data):
        sum = 0
        for i, v in enumerate(value):
            sum += v
            if i + 1 == len(value):
                mean.append(round(sum / (i + 1), 2))
    return mean


def calculateVariance(data, mean):
    variance = []
    for index, value in enumerate(data):
        sum = 0
        for i, v in enumerate(value):
            sum += (v - mean[index]) ** 2

            if i + 1 == len(value):
                variance.append(round(sum / (i + 1), 2))
    return variance


def calculateStddev(variance):
    stddev = []
    for index, value in enumerate(variance):
        stddev.append(round(value**0.5, 2))

    return stddev


def getNewInput():
    while True:
        statsFile = input("Enter filename for new Stats File: ")
        if not os.path.exists(statsFile):
            print("\nPlease enter the correct Stats File again: ")
            continue
        break
    print("")

    while True:
        days = input("Enter the number of Days: ")
        if days.__contains__("."):
            print("\nPlease enter a whole number: ")
            continue
        try:
            days = int(days)
        except:
            print("\nPlease enter a whole number: ")
            continue
        if days == 0:
            print("\nPlease enter number more than 0: \n")
            continue
        break
    return statsFile, int(days)


def getThreshold(allWeight):
    sum = 0
    for i in range(len(allWeight)):
        sum += allWeight[i]

    return 2 * sum


def readNewLogs(filename):
    print("Analysing ...")
    dailyData = []
    with open(filename, "r") as fin:
        while True:
            line = fin.readline().strip()
            if not line:
                break
            daily = []
            noOfEvents = int(fin.readline().strip())
            for i in range(noOfEvents):
                daily.append(fin.readline().strip().split(":")[2])
            dailyData.append(daily)
            fin.readline().strip()
    return dailyData


def anomalyCounter(filename, weight, mean, stddev):
    print_subsection_heading("Calculating ...")
    data = readNewLogs(filename)
    dailyCounter = []

    for index, value in enumerate(data):
        counter = 0
        for i, v in enumerate(value):
            counter += float(
                round(((abs((float(v) - mean[i])) / stddev[i]) * weight[i]), 2)
            )

        dailyCounter.append(counter)
    print("Calculated!")
    return dailyCounter


def flagging(data, threshold):
    print("Checking for anomalies ...")
    anomalies = []
    with open("anomalyCounter.txt", "w") as file:
        for day, count in enumerate(data, start=1):
            if count > threshold:
                anomalies.append(day)
                file.write(
                    f"Day {day} anomaly count = {
                        round(count, 2)} - ANOMALY DETECTED\n"
                )
                print(
                    f"\nDay {day} anomaly count = {
                        round(count, 2)} - ANOMALY DETECTED"
                )
            else:
                print(f"\nDay {day} anomaly count = {round(count, 2)}")

        if anomalies:
            print_section_heading("ALERT! ANOMALIES DETECTED!")
            for day in anomalies:
                print(f"Day {day} has been flagged!")
            file.write("\nALERT! Anomalies detected!\n")
            for day in anomalies:
                file.write(f"\nDay {day} has been flagged!\n\n")
        else:
            print("\n\nThere are no anomalies!\n")
            file.write("\n\nNo anomalies detected.\n")

    return anomalies


def main():
    print_section_heading("Welcome to the Intrusion Detection System!")

    # Initial Input
    eventFile, statsFile, days = initialInput()
    eventData = readEvents(eventFile)
    statsData = readStats(statsFile)
    if not consistencyCheck(eventData, statsData):
        exit()
    print("\n")
    time.sleep(1)

    print_subsection_heading(f"Reading and Processing {eventFile}")
    allWeight = processEvents(eventData)

    print("\n")
    time.sleep(1)

    print_subsection_heading(f"Reading and Processing {statsFile}")
    processStats(statsData)

    print("\n")
    time.sleep(1)

    # Activity Simulation Engine and the Logs
    print_subsection_heading("Generating Activity Logs")
    dataSet = generateDataSet(days, eventData, statsData)
    time.sleep(1)
    simulateActivity("ActivityLogs.txt", days, eventData, dataSet)
    time.sleep(1)

    # Analysis Engine
    print_subsection_heading("Analyzing Activity Logs")
    data, eventName = readLogs("ActivityLogs.txt")
    mean, stddev = outputData(data, eventName, "BaselineStats.txt")

    # Alert Engine
    while True:
        newStatsFile, newDays = getNewInput()
        newStatsData = readStats(newStatsFile)
        newDataSet = generateDataSet(newDays, eventData, newStatsData)
        simulateActivity("ActivityLogs.txt", newDays, eventData, newDataSet)
        threshold = getThreshold(allWeight)
        dailyAnomalyCounter = anomalyCounter(
            "ActivityLogs.txt", allWeight, mean, stddev)
        print(f"\nThreshold for Anomaly Detection: {threshold}")
        flagged = flagging(dailyAnomalyCounter, threshold)
        option = input(
            "\nDo you want to read a new Stats text file? (yes/no): ")
        print("")
        if option.lower() == "no":
            break
    exit("\nThank you for using the Intrusion Detection System!\n\n")


if __name__ == "__main__":
    main()
