
f = open("sample_split_avg_17_train.seq", "r").readlines()

with open("test_data/baseline_sample_split_train.seq", "w") as fea:
    for line in f:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)

p = open("sample_split_avg_17_test.seq", "r").readlines()

with open("test_data/baseline_sample_split_test.seq", "w") as fea:
    for line in p:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)

q = open("sample_split_avg_17_dev.seq", "r").readlines()

with open("test_data/baseline_sample_split_dev.seq", "w") as fea:
    for line in q:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)
'''

f = open("simple_avg_17_train.seq", "r").readlines()

with open("simple_avg_2_train.seq", "w") as fea:
    for line in f:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[7] + "\t" + pairs[4] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)

p = open("simple_avg_17_test.seq", "r").readlines()

with open("simple_avg_2_test.seq", "w") as fea:
    for line in p:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[7] + "\t" + pairs[4] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)

q = open("simple_avg_17_dev.seq", "r").readlines()

with open("simple_avg_2_dev.seq", "w") as fea:
    for line in q:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + pairs[7] + "\t" + pairs[4] + "\t" + pairs[-1] + "\n")
            fea.write(text)
        else:
            fea.write(line)
'''