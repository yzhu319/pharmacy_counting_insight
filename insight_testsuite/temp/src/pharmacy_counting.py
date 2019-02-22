## Pharmacy counting insight challange
## @Author: Yuanzheng Zhu
## ...Cannot use any external packages like pandas, np, etc...

#test files
#input_path = "../insight_testsuite/tests/test_1/input/itcont.txt"
#output_path = "../insight_testsuite/tests/test_1/output/top_cost_drug.txt"

input_path = "input/itcont.txt"
output_path = "output/top_cost_drug.txt"

input_file = open(input_path, 'r')
lines = input_file.read().splitlines()
input_file.close()

split_lines = [line.split(',') for line in lines]
features = split_lines[0] # first row, feature names
split_lines = split_lines[1:] #skip first line

mapped = list(zip(*split_lines)) # a collection of column values

first_name = list(mapped[features.index('prescriber_first_name')])
last_name = list(mapped[features.index('prescriber_last_name')])
drug_name = list(mapped[features.index('drug_name')])
drug_cost = list(mapped[features.index('drug_cost')])
full_name = [(a + ' ' + b) for a, b in zip(first_name, last_name)]

unique_drug_name = list(set(drug_name))
unique_drug_name = sorted(unique_drug_name, reverse = True) # sort in descending order
#print(full_name)
#print(drug_cost)
#print(drug_name)

output_file = open(output_path, 'w')
output_file.write('drug_name,num_prescriber,total_cost') #first line

# Two dictionary, key is unique_drug_name, value is empty list [], to be filled with name and cost, respectively
name_list_val = [[] for x in range(len(unique_drug_name))]
cost_list_val = [[] for x in range(len(unique_drug_name))]
totalcost = [0 for x in range(len(unique_drug_name))]

# initialize empty dictionary
name_dict = {k:v for k,v in zip(unique_drug_name, name_list_val)}
cost_dict = {k:v for k,v in zip(unique_drug_name, cost_list_val)}
total_cost_dict = {k:v for k,v in zip(unique_drug_name, totalcost)}
#print(name_dict)

### Method: fill dictionary; time complexity 1 * total_entries; use drug_name as key
for i, thisDrug in enumerate(drug_name):
    name_dict[thisDrug].append(full_name[i])
    cost_dict[thisDrug].append(int(drug_cost[i]))
    total_cost_dict[thisDrug] += int(drug_cost[i])

#print(name_dict)
#print(cost_dict)
#print(total_cost_dict)

sorted_total_cost = sorted(total_cost_dict.items(), key=lambda x: (x[1],x[0]), reverse=True)
#print(sorted_total_cost)

for (thisDrug, total_cost) in sorted_total_cost:
    #unique full_name list for this drug
    unique_full_name = list(set(name_dict[thisDrug]))
    #print(unique_full_name)
    #print("{},{},{}\n".format(thisDrug, len(unique_full_name), sum(cost_dict[thisDrug])))
    output_file.write("\n{},{},{}".format(thisDrug, len(unique_full_name), total_cost))

output_file.close()