"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) RedFantom 2019

Convert the results of a Bode Plot analysis of the bode plot utility
into a three-column CSV-file. Columns:
1. Test Frequency (Hz)
2. Gain (dB)
3. Phase (degrees)
"""
import pandas
import os


folder = "INSERT_PATH_TO_BODE_LOG_DATA"
os.chdir(folder)

for file in os.listdir(os.getcwd()):
    if not file.endswith(".txt"):
        continue
    with open(file, "r") as fi:
        # First three lines are meta-data
        lines = fi.readlines()[3:]
    data = {"frequency": list(), "gain": list(), "phase": list()}
    for line in lines:
        elements = [e for e in line.split(" ") if e != ""]
        freq, gain, phase = [float(e.replace(",", ".")) for e in elements]
        data["frequency"].append(freq)
        data["gain"].append(gain)
        data["phase"].append(phase)
    d = pandas.DataFrame(data)
    d.to_csv("{}_bode.csv".format(file.split(".")[0]))
