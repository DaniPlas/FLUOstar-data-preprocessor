# FLUOstar-data-preprocessor
Allows for an initial preprocessing of FLUOstar® Omega microplate reader Excel files for further use. 

-----

This script takes initial files with signals from all chosen wells in transposed tables 
(having the general format: header + table with time and signal for each well), and allows the user to 
classify wells according to the conditions tested. It returns a final file with full data, averages with
standard deviations, normalized data (0 to 1), averages and standard deviation of normalized data,
and half-times.

### Input

Excel files with signal data for each well (all wells or those chosen for the experimental run, in case not all wells were active for recording signal)
with **transposed tables**.

To get them:

1. Open the desired experiment using the MARS Data Analysis software.
2. Select "Table view"
3. Select "All cycles"
4. Click on "Excel report"
  4.1 Mark "Transpose tables"
5. Save the file

> This script was written in Python, using Pandas and tkinter modules, so you'll need them to run it. 
> A compiled file will be made available to run this script as an executable file without needing to install anything else.

## General steps
 
### Retrieving the files 

1. Enter the number of files that you will merge. In case the experiment took only one cycle, you'll likely have only 1 document. 
2. Go to each file location and choose it. The script will open a window for you to look up the file.
<br>

### Creating groups: conditions + replicates

Here you will enter the name of each condition, next, you'll introduce the name of each replicate's column (ex. A1, B3, D12), according to your experimental design.

1. When prompted, write the name of the condition.
2. When prompted, enter the name of each replicate's column that belong to this condition, each separated by one space.
3. When prompted, write **y** or **yes** if you wish to enter a new condition, and repeat steps 1 or 2.
4. When you're done entering conditions, enter **n** or **no** when prompted.
<br>

### Deleting bad replicates / choose normalizing times.

A graph will open for each condition showing all replicates that belong to it. The order at which each replicate was entered corresponds to curves following this
color sequence: blue-yellow-green-red.

1. Identify if there is any replicate that you wish to discard for future averaging and normalizing of the data.
**Take note of initial and final times that you wish to use for normalizing your data**
2. **Close** the graphs before continuing.
3. When prompted, enter the name of the replicates to be discarded, each separated by one space.

*note: due to the way the graphs are presented, I cannot enter a legend that shows each replicate's corresponding color. This will be improved upon in the future.*

<br>

### Normalizing data

A graph with averages will appear; close it to continue. You will be prompted to enter the initial and final times of normalization for each replicate.

1. When prompted, enter the initial time for normalization of the given replicate.
2. When prompted, enter the final time for normalization of the given replicate.

A graph with normalized data (averages) will appear; close it to continue.

<br>

### Final Excel document

1. When prompted, write a name for the final Excel file.
2. With the Explorer window opened, choose your preferred location to save the file.
<br>

<h4>Final Excel file</h4>

1. **Full**: all replicates minus those discarded (if any).
2. **Averages**: averages + standard deviations for each condition.
3. **Normalized**: normalized data (0 to 1) for each replicate.
4. **Normalized (ave)**: averages of normalized data (0 to 1) + standard deviations for each condition.
5. **half-times**: half-times (time when normalized signal ≈ 0.5) for each replicate.
6. **half-times (ave)**: averages of half-times (time when normalized signal ≈ 0.5) + standar deviations for each condition.
7. **Full_data**: all replicates including those discarded (if any).

