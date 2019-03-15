import csv
size_hdn_lyr = 40
a = "double b_1[size_hdn_lyr+5] = {"
with open('rounded_biases_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x = (', '.join(row))
        a = a + x + "," 
    a = a + "};"
file = open("rounded_biases_1.txt","w") 
file.write(a) 

a = "double b_2[15] = {"
with open('rounded_biases_2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        x = (', '.join(row))
        a = a + x + "," 
    a = a + "};"
file = open("rounded_biases_2.txt","w") 
file.write(a) 

a = "double w_1[605][size_hdn_lyr+5] = {"
with open('rounded_weights_1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    a = a + "{ "
    for row in spamreader:
        x = (', '.join(row))
        a = a + x
        a = a + "}," + "\n" + "{"
    a = a + "};"
file = open("rounded_weights_1.txt","w") 
file.write(a) 

a = "double w_2[size_hdn_lyr+5][15] = {"
with open('rounded_weights_2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    a = a + "{ "
    for row in spamreader:
        x = (', '.join(row))
        a = a + x
        a = a + "}," + "\n" + "{"
    a = a + "};"
file = open("rounded_weights_2.txt","w") 
file.write(a) 