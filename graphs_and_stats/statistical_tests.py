from scipy.stats import mannwhitneyu
from scipy.stats import normaltest
from scipy.stats import wilcoxon
from scipy.stats import ttest_rel
from scipy.stats import ranksums
import matplotlib.pyplot as plot
import sys

input_filename = "run2.csv)"
if len(sys.argv) > 1:
    input_filename = sys.argv[1]
f = open(input_filename, "r")

results = []

for line in f:
	cols = [float(x) for x in line.split()]

	for i, col in zip(range(len(cols)), cols):
		try:
			results[i].append(col)
		except:
			results.append([col])

for i, result in zip(range(len(results)), results):
    print i, sum(result) / len(result)

print "---------- RESULTS ----------"
print "Normal Test", normaltest(results[1])
print "Mann-Whitney", mannwhitneyu(results[1], results[3])
print "Wilcoxon", wilcoxon(results[1], results[3])
print "T-Test", ttest_rel(results[1], results[3])

print "Rank Sums", ranksums(results[1], results[9])
