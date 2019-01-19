# MyDAQ CSV Export
The [MyDAQ](https://www.ni.com/nl-nl/shop/select/mydaq-student-data-acquisition-device)
device software (ElvisNX) supports exporting measurement data to plain 
text log files. Unfortunately, these are difficult to manipulate. They
cannot be directly imported in MATLAB, for example.

That is what these scripts are for. These Python scripts can convert the
plain text log files into CSV-files that can be used with MATLAB, or 
`pandas` or other utilities.

## Usage
Using these scripts is very simple. All you need is a Python interpreter
with `pandas` installed. In order to allow easy batch processing, all
scripts have been implemented with a folder variable in the script. All
files in that folder will be converted by the script. Of course, the
original files will only be read and not modified.

It would be possible to extend this implementation with command-line
arguments, but this was unnecessary for my purposes. Feel free to make
such modifications, under the terms of the license.

The scripts could be further enhanced with a more sophisticated file 
naming system and other options, but this was all unnecessary for my 
purposes (simply converting the data to be included in a univeristy
report).

## License
    MyDAQ CSV export scripts
    Copyright (c) 2019 RedFantom
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

