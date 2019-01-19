"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) RedFantom 2019

Convert the results of an FFT transform saved to a log file into a CSV
file. These files can be obtained with the Spectrum Analyzer utility
of the ElvisNX software.
"""
import pandas
import os


folder = "INSERT_PATH_TO_FFT_LOG_DATA"
os.chdir(folder)

wave = "waveformSource signal"
fft = "FFT waveform"

dictionary = dict()
for file in sorted(os.listdir(os.getcwd())):
    if not file.endswith(".txt"):
        continue
    print("Processing:", file, "...", end=" ")
    with open(file, "r") as fi:
        lines = [l.strip() for l in fi.readlines()]
    column = ""
    dictionary.clear()
    dt = 0.0
    for line in lines:
        if "waveform" in line:
            column = line.replace("\t", "")
            if column not in dictionary:
                dictionary[column] = {"k": list(), "v": list()}
            continue
        if "delta" in line:
            dt = float(line.split("\t")[1].lower().replace(",", "."))
        if line == "" or ("t" in line and "0" in line) or "Unit" in line:
            continue
        try:
            k = float(line.split("\t")[0].lower().replace(",", ".")) / 1000
        except ValueError:
            k = line.split("\t")[0]
        v = float(line.split("\t")[1].lower().replace(",", "."))
        dictionary[column]["k"].append(k)
        dictionary[column]["v"].append(v)
    length = len(dictionary[wave]["k"])
    dictionary[wave]["k"] = [t * dt for t in range(length)]
    waveform = {"Time": dictionary[wave]["k"], "Value": dictionary[wave]["v"]}
    fft_wave = {"Frequency": dictionary[fft]["k"], "Value": dictionary[fft]["v"]}
    wave_d = pandas.DataFrame(waveform)
    wave_d.to_csv("{}_waveform.csv".format(file.split(".")[0]))
    fft_d = pandas.DataFrame(fft_wave)
    fft_d.to_csv("{}_fft.csv".format(file.split(".")[0]))
    print("Done.")
