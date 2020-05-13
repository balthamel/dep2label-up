from sklearn.preprocessing import normalize, MinMaxScaler
import numpy as np

f = open("simple_avg_17_train.seq", "r").readlines()
q = open("simple_avg_17_test.seq", "r").readlines()
p = open("simple_avg_17_dev.seq", "r").readlines()
feats = []
#feat1 = set()
#feat2 = set()
raw_feats = []

#index_raw = [2, 3, 8, 9, 11, 12, 13, 14]
index_raw = []
index = [10,11,12,13,14,15,16,17,18]

for line in q:
    if len(line) > 2:
        feat = []
        raw_feat = []
        pairs = line.strip().split()
        for i in index:
            feat.append(float(pairs[i]))
        for i in index_raw:
            raw_feat.append(float(pairs[i]))

        feats.append(feat)
        raw_feats.append(raw_feat)

for line in p:
    if len(line) > 2:
        feat = []
        raw_feat = []
        pairs = line.strip().split()
        for i in index:
            feat.append(float(pairs[i]))
        for i in index_raw:
            raw_feat.append(float(pairs[i]))
        feats.append(feat)
        raw_feats.append(raw_feat)

for line in f:
    if len(line) > 2:
        feat = []
        raw_feat = []
        pairs = line.strip().split()
        for i in index:
            feat.append(float(pairs[i]))
        for i in index_raw:
            raw_feat.append(float(pairs[i]))
        feats.append(feat)
        raw_feats.append(raw_feat)


print(len(feats))

norm_feats = normalize(feats, axis=0, norm='l1')
#scaler = MinMaxScaler()
#norm_feats = scaler.fit_transform(feats)


count = 0
id = 0


with open("ablation_all_data/context_feats_avg_test.seq", "w") as fea:
    for line in q:
        if len(line) > 2:
            pairs = line.strip().split()

            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t"
                       + str(norm_feats[id][2]) + "\t" + str(norm_feats[id][3]) + "\t" + str(norm_feats[id][4]) + "\t"
                       + str(norm_feats[id][5]) + "\t" + str(norm_feats[id][6]) + "\t" + str(norm_feats[id][7]) + "\t"
                       + str(norm_feats[id][8]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)

with open("ablation_all_data/context_feats_avg_dev.seq", "w") as fea:
    for line in p:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t"
                       + str(norm_feats[id][2]) + "\t" + str(norm_feats[id][3]) + "\t" + str(norm_feats[id][4]) + "\t"
                       + str(norm_feats[id][5]) + "\t" + str(norm_feats[id][6]) + "\t" + str(norm_feats[id][7]) + "\t"
                       + str(norm_feats[id][8]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)

with open("ablation_all_data/context_feats_avg_train.seq", "w") as fea:
    for line in f:
        if len(line) > 2:
            pairs = line.strip().split()
            text = str(pairs[0] + "\t" + pairs[1] + "\t" + str(norm_feats[id][0]) + "\t" + str(norm_feats[id][1]) + "\t"
                       + str(norm_feats[id][2]) + "\t" + str(norm_feats[id][3]) + "\t" + str(norm_feats[id][4]) + "\t"
                       + str(norm_feats[id][5]) + "\t" + str(norm_feats[id][6]) + "\t" + str(norm_feats[id][7]) + "\t"
                       + str(norm_feats[id][8]) + "\t" + pairs[-1] + "\n")
            fea.write(text)
            id += 1
            count += 1
        else:
            fea.write(line)