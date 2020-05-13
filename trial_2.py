from sklearn.preprocessing import normalize
import numpy as np

f = open("simple_avg_2_train.seq", "r").readlines()
q = open("simple_avg_2_test.seq", "r").readlines()
p = open("simple_avg_2_dev.seq", "r").readlines()
feats = []
feat1 = set()
feat2 = set()
for line in q:
    if len(line) > 2:
        pairs = line.strip().split()
        feats.append([float(pairs[2]), float(pairs[3])])
        #feat1.add(float(pairs[2]))
        #feat2.add(float(pairs[3]))
for line in p:
    if len(line) > 2:
        pairs = line.strip().split()
        feats.append([float(pairs[2]), float(pairs[3])])
        #feat1.add(float(pairs[2]))
        #feat2.add(float(pairs[3]))
for line in f:
    if len(line) > 2:
        pairs = line.strip().split()
        feats.append([float(pairs[2]), float(pairs[3])])
        #feat1.add(float(pairs[2]))
        #feat2.add(float(pairs[3]))


print(len(feats))
#disc = KBinsDiscretizer(n_bins=24, encode='ordinal', strategy='kmeans')
#feat1 = np.array(list(feat1)).reshape(-1,1)
#feat2 = np.array(list(feat2)).reshape(-1,1)
norm_feats = normalize(feats, axis=0, norm='l2')

#disc.fit(feat1)
#desc = KBinsDiscretizer(n_bins=24, encode='ordinal', strategy='kmeans')
#desc.fit(feat2)
#print("Heh")
count = 0
id = 0
with open("test_data/norm_raw_l2_simple_avg_2_test.seq", "w") as fea:
    for line in q:
        if len(line) > 2:
            pairs = line.strip().split()
            #feat1 = disc.transform([[float(pairs[2])]])
            #feat2 = disc.transform([[float(pairs[3])]])

            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)

with open("test_data/norm_raw_l2_simple_avg_2_dev.seq", "w") as fea:
    for line in p:
        if len(line) > 2:
            pairs = line.strip().split()
            #feat1 = disc.transform([[float(pairs[2])]])
            #feat2 = disc.transform([[float(pairs[3])]])
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)

with open("test_data/norm_raw_l2_simple_avg_2_train.seq", "w") as fea:
    for line in f:
        if len(line) > 2:
            pairs = line.strip().split()
            #feat1 = disc.transform([[float(pairs[2])]])
            #feat2 = disc.transform([[float(pairs[3])]])
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)


