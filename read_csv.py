import csv


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
    with open("sample_train.conllu", "w") as f:
        with open("sample_test.conllu", "w") as q:
            for row in reader:
                row['ID'] = int(float(row['ID']))
                row['Head'] = int(float(row['Head']))

                if row['Tot_fix_dur'] == '':
                    row['Tot_fix_dur'] = '0'
                if row['Mean_fix_dur'] == '':
                    row['Mean_fix_dur'] = '0'
                if count <= 2131 and row['Participant'] == 'sa':
                    if row['ID'] == 1:
                        f.write("\n")
                        count += 1
                    f.write(str(row['ID']) + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
                            + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
                            + row['Tot_fix_dur'] + "\t" + row['Mean_fix_dur'] + '\n')
                elif count > 2131 and row['Participant'] == 'sa':
                    if row['ID'] == 1:
                        q.write("\n")
                        count += 1
                    q.write(str(row['ID']) + '\t' + row['Word'] + '\t' +"_" + '\t' + row['UniversalPOS'] + '\t'
                            + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
                            + row['Tot_fix_dur'] + "\t" + row['Mean_fix_dur'] + '\n')

            print(count)



