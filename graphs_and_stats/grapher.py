import sys
from matplotlib import pyplot as plot

# munch up the files given without even checking what the arguments were.
if len(sys.argv) < 4:
    print "USAGE ERROR: You must specify a space-separated .csv file to plot and the two columns to plot against each other (e.g. \"grapher.py my_file.csv 0 2\" will plot my_file.csv with column 0 as x and column 2 as y.\n"
    sys.exit()
try:
    input_file_name = sys.argv[1]
    output_file_name = str.rsplit(sys.argv[1], '.', 1)[0] + ".pdf"
    x_row = int(sys.argv[2])
    y_row = int(sys.argv[3])
    
    f = open(input_file_name, 'r')
except:
    print "USAGE ERROR: You must specify a space-separated .csv file to plot and the two columns to plot against each other (e.g. \"grapher.py my_file.csv 0 2\" will plot my_file.csv with column 0 as x and column 2 as y.\n"
    raise

# grow the strings
x = []
y = []
print f
for line in f:
    vals = line.split()
    x.append(vals[x_row])
    y.append(vals[y_row])

# print
fig = plot.plot(x, y, linewidth=1.0)
plot.show()
plot.savefig(output_file_name)

# max's weird stuff
#ax = fig.add_subplot(111)
#ax1.plot(time,limit,color='r',label="limit")

#lline = ax.hlines(limit, time, time[1:] + [600],label="Limit price")
#eline = ax.plot(time,p,color='g',label="Equilibrium price")
#plot.ylabel("Price")
#plot.xlabel("Time")
#a = plot.twinx()
#aline = a.plot(time,r,color='b',label="Aggressiveness")

#lines, labels = ax.get_legend_handles_labels()
#lines2, labels2 = a.get_legend_handles_labels()

#a.set_ylabel("Aggressiveness")
#a.legend(lines+lines2, labels+labels2, loc=0)
