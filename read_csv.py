import csv
import numpy as np
#from sklearn.preprocessing import KBinsDiscretizer

with open("Dundee_DLT_freq_goldtok_newFPD.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file, delimiter='\t')

    '''i = 0
    prev_sent_id = 1.0
    for row in reader:
        pres_id = float(row['SentenceID'])
        #print(row)
        if row['Tot_fix_dur'] == '':
            row['Tot_fix_dur'] = '0'
        if row['Mean_fix_dur'] == '':
            row['Mean_fix_dur'] = '0'
        print(row['ID'] + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
              + row['CPOS'] + '\t' + "_" + '\t' + row['Head'] + '\t' + row['DepRel'] + '\t'
              + "_" + '\t' + row['Tot_fix_dur'] + '\t' + row['Mean_fix_dur'] + '\n')
        if pres_id != prev_sent_id:
            print("\n")
        i += 1
        prev_sent_id = pres_id
        if i >= 5:
            break'''
    count = 0
    #tot_fix_dur = []
    #enc = KBinsDiscretizer(n_bins=24, encode='ordinal', strategy='kmeans')
    with open("sample_split_17_test.conllu", "w") as f:
        with open("sample_split_17_dev.conllu", "w") as q:
            with open("sample_split_17_train.conllu", "w") as p:
                for row in reader:
                    row['ID'] = int(float(row['ID']))
                    row['Head'] = int(float(row['Head']))

                    if row['Tot_fix_dur'] == '':
                        row['Tot_fix_dur'] = '0'
                    if row['Mean_fix_dur'] == '':
                        row['Mean_fix_dur'] = '0'
                    if row['nFix'] == '':
                        row['nFix'] = '0.0'
                    if row['nRefix'] == '':
                        row['nRefix'] = '0.0'
                    if row['Re_read_prob'] == '':
                        row['Re_read_prob'] = '0.0'
                    if row['Fix_prob'] == '':
                        row['Fix_prob'] = '0.0'
                    if row['First_fix_dur'] == '':
                        row['First_fix_dur'] = '0'
                    if row['First_pass_dur'] == '':
                        row['First_pass_dur'] = '0'
                    if row['Tot_regres_from_dur'] == '':
                        row['Tot_regres_from_dur'] = '0'
                    if row['n_2_fix_prob'] == '':
                        row['n_2_fix_prob'] = '0.0'
                    if row['n_1_fix_prob'] == '':
                        row['n_1_fix_prob'] = '0.0'
                    if row['n+2_fix_prob'] == '':
                        row['n+2_fix_prob'] = '0.0'
                    if row['n+1_fix_prob'] == '':
                        row['n+1_fix_prob'] = '0.0'
                    if row['n_2_fix_dur'] == '':
                        row['n_2_fix_dur'] = '0.0'
                    if row['n_1_fix_dur'] == '':
                        row['n_1_fix_dur'] = '0.0'
                    if row['n+2_fix_dur'] == '':
                        row['n+2_fix_dur'] = '0.0'
                    if row['n+1_fix_dur'] == '':
                        row['n+1_fix_dur'] = '0.0'
                    if count <= 241 and row['Participant'] == 'sa':
                        #tot_fix_dur.append(float(row['Tot_fix_dur']))
                        if row['ID'] == 1:
                            f.write("\n")
                            count += 1
                        f.write(str(row['ID']) + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
                                + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
                                + row['nFix'] + '\t' + row['Fix_prob'] + '\t' + row['Mean_fix_dur'] + "\t"
                                + row['First_fix_dur'] + '\t' + row['First_pass_dur'] + '\t' + row['Tot_fix_dur'] + '\t'
                                + row['nRefix'] + '\t' + row['Re_read_prob'] + '\t' + row['Tot_regres_from_dur'] + '\t'
                                + row['n_2_fix_prob'] + '\t' + row['n_1_fix_prob'] + '\t' + row['n+1_fix_prob'] + '\t'
                                + row['n+2_fix_prob'] + '\t' + row['n_2_fix_dur'] + '\t' + row['n_1_fix_dur'] + '\t'
                                + row['n+1_fix_dur'] + '\t' + row['n+2_fix_dur'] + '\n')
                    elif count > 241 and count <= 471 and row['Participant'] == 'sa':
                        #tot_fix_dur.append(float(row['Tot_fix_dur']))
                        if row['ID'] == 1:
                            q.write("\n")
                            count += 1
                        q.write(str(row['ID']) + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
                                + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
                                + row['nFix'] + '\t' + row['Fix_prob'] + '\t' + row['Mean_fix_dur'] + "\t"
                                + row['First_fix_dur'] + '\t' + row['First_pass_dur'] + '\t' + row['Tot_fix_dur'] + '\t'
                                + row['nRefix'] + '\t' + row['Re_read_prob'] + '\t' + row['Tot_regres_from_dur'] + '\t'
                                + row['n_2_fix_prob'] + '\t' + row['n_1_fix_prob'] + '\t' + row['n+1_fix_prob'] + '\t'
                                + row['n+2_fix_prob'] + '\t' + row['n_2_fix_dur'] + '\t' + row['n_1_fix_dur'] + '\t'
                                + row['n+1_fix_dur'] + '\t' + row['n+2_fix_dur'] + '\n')
                    elif count > 471 and row['Participant'] == 'sa':
                        if row['ID'] == 1:
                            p.write("\n")
                            count += 1
                        p.write(str(row['ID']) + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
                                + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
                                + row['nFix'] + '\t' + row['Fix_prob'] + '\t' + row['Mean_fix_dur'] + "\t"
                                + row['First_fix_dur'] + '\t' + row['First_pass_dur'] + '\t' + row['Tot_fix_dur'] + '\t'
                                + row['nRefix'] + '\t' + row['Re_read_prob'] + '\t' + row['Tot_regres_from_dur'] + '\t'
                                + row['n_2_fix_prob'] + '\t' + row['n_1_fix_prob'] + '\t' + row['n+1_fix_prob'] + '\t'
                                + row['n+2_fix_prob'] + '\t' + row['n_2_fix_dur'] + '\t' + row['n_1_fix_dur'] + '\t'
                                + row['n+1_fix_dur'] + '\t' + row['n+2_fix_dur'] + '\n')

                print(count)
                '''tot_fix_dur = np.asarray(tot_fix_dur).reshape(-1,1)
                tot_fix_dur = enc.fit_transform(tot_fix_dur)
                print("----------------------------")
                print(max(tot_fix_dur))
                print(min(tot_fix_dur))
                #print(tot_fix_dur.index(max(tot_fix_dur)))
                print(tot_fix_dur)'''



