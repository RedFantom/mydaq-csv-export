"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) RedFantom 2019

Convert the results of the oscilloscope utility plain text log files
into a CSV file. The measurements saved to the file are given as plain
read voltages.
"""
import pandas
import os


folder = "INSERT_PATH_TO_OSCILLOSCOPE_LOG_DATA"
os.chdir(folder)


def to_float(v):
    return float(v.strip().replace(",", ".").lower())


for file in os.listdir(os.getcwd()):
    if not file.endswith(".txt"):
        continue
    print("Processing {}...".format(file), end=" ", flush=True)
    with open(file, "r") as fi:
        lines = [l for l in fi.readlines() if l.strip() != ""]
    data, delta_t, channel = dict(), 0, ""
    for line in lines:
        if "waveform" in line:
            channel = line.split("\t")[1].strip()
            data[channel] = list()
        elif "delta t" in line:
            delta_t = to_float(line.split("\t")[1])
        elif "t0" in line:
            # Do something fun with the start time of the measurement
            # here if you feel like it
            continue
        elif "time" in line:
            continue
        else:
            date, measurement = line.split("\t")
            measurement = to_float(measurement)
            data[channel].append(measurement)
    data["time"] = [k * delta_t for k in range(len(data[channel]))]
    pandas.DataFrame(data).to_csv("{}_oscilloscope.csv".format(file.split(".")[0]))
    print("Done.", flush=True)
