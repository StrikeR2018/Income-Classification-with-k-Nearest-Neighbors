import sys, csv, numpy
#data loading funciton loads csv data into matrix
def loadCsv(file):
    return numpy.loadtxt(file, skiprows = 1, delimiter = ",")

def writeCsv(points):
    filename = "output.csv"
    fields = ['id', 'income']
    print("id, income")
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        for key, value in points.items():
            csvwriter.writerow([key, value])
            print(key, value)