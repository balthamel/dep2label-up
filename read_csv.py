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

    with open("sample.conllu", "w") as f:
        for row in reader:
            row['ID'] = int(float(row['ID']))
            row['Head'] = int(float(row['Head']))
            if row['ID'] == 1:
                f.write("\n")
            if row['Tot_fix_dur'] == '':
                row['Tot_fix_dur'] = '0'
            if row['Mean_fix_dur'] == '':
                row['Mean_fix_dur'] = '0'
            f.write(str(row['ID']) + '\t' + row['Word'] + '\t' + "_" + '\t' + row['UniversalPOS'] + '\t'
              + row['CPOS'] + '\t' + "_" + '\t' + str(row['Head']) + '\t' + row['DepRel'] + '\t'
              + "_" + '\t' + row['Tot_fix_dur'] + '\t' + row['Mean_fix_dur'] + '\n')
            if int(float(row['SentenceID'])) >= 2400:
                break
