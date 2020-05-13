import csv
from collections import Counter

sa, sb, sc, sd, se, sf, sg, sh, si, sj = [], [], [], [], [], [], [], [], [], []
with open("Dundee_DLT_freq_goldtok_newFPD.csv", "r", encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter='\t')
    for row in reader:
        if row['Participant'] == 'sa':
            sa.append(row)
        elif row['Participant'] == 'sb':
            sb.append(row)
        elif row['Participant'] == 'sc':
            sc.append(row)
        elif row['Participant'] == 'sd':
            sd.append(row)
        elif row['Participant'] == 'se':
            se.append(row)
        elif row['Participant'] == 'sf':
            sf.append(row)
        elif row['Participant'] == 'sg':
            sg.append(row)
        elif row['Participant'] == 'sh':
            sh.append(row)
        elif row['Participant'] == 'si':
            si.append(row)
        elif row['Participant'] == 'sj':
            sj.append(row)
        else:
            print("Some data issue")

count = 0
with open("simple_avg_17_test.conllu", "w", encoding='utf-8') as f:
    with open("simple_avg_17_dev.conllu", "w", encoding='utf-8') as q:
        with open("simple_avg_17_train.conllu", "w", encoding='utf-8') as p:
            for i in range(len(sa)):
                Tot_fix_dur = []
                Mean_fix_dur = []
                nFix = []
                nRefix = []
                Re_read_prob = []
                Fix_prob = []
                First_fix_dur = []
                First_pass_dur = []
                Tot_regres_from_dur = []
                n_2_fix_prob = []
                n_1_fix_prob = []
                n_plus_2_fix_prob = []
                n_plus_1_fix_prob = []
                n_2_fix_dur = []
                n_1_fix_dur = []
                n_plus_2_fix_dur = []
                n_plus_1_fix_dur = []

                sa[i]['ID'] = int(float(sa[i]['ID']))
                sa[i]['Head'] = int(float(sa[i]['Head']))

                if sa[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sa[i]["Tot_fix_dur"]))
                if sb[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sb[i]["Tot_fix_dur"]))
                if sc[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sc[i]["Tot_fix_dur"]))
                if sd[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sd[i]["Tot_fix_dur"]))
                if se[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(se[i]["Tot_fix_dur"]))
                if sf[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sf[i]["Tot_fix_dur"]))
                if sg[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sg[i]["Tot_fix_dur"]))
                if sh[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sh[i]["Tot_fix_dur"]))
                if si[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(si[i]["Tot_fix_dur"]))
                if sj[i]["Tot_fix_dur"] != '': Tot_fix_dur.append(float(sj[i]["Tot_fix_dur"]))

                if sa[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sa[i]["Mean_fix_dur"]))
                if sb[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sb[i]["Mean_fix_dur"]))
                if sc[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sc[i]["Mean_fix_dur"]))
                if sd[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sd[i]["Mean_fix_dur"]))
                if se[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(se[i]["Mean_fix_dur"]))
                if sf[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sf[i]["Mean_fix_dur"]))
                if sg[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sg[i]["Mean_fix_dur"]))
                if sh[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sh[i]["Mean_fix_dur"]))
                if si[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(si[i]["Mean_fix_dur"]))
                if sj[i]["Mean_fix_dur"] != '': Mean_fix_dur.append(float(sj[i]["Mean_fix_dur"]))

                if sa[i]["nFix"] != '': nFix.append(float(sa[i]["nFix"]))
                if sb[i]["nFix"] != '': nFix.append(float(sb[i]["nFix"]))
                if sc[i]["nFix"] != '': nFix.append(float(sc[i]["nFix"]))
                if sd[i]["nFix"] != '': nFix.append(float(sd[i]["nFix"]))
                if se[i]["nFix"] != '': nFix.append(float(se[i]["nFix"]))
                if sf[i]["nFix"] != '': nFix.append(float(sf[i]["nFix"]))
                if sg[i]["nFix"] != '': nFix.append(float(sg[i]["nFix"]))
                if sh[i]["nFix"] != '': nFix.append(float(sh[i]["nFix"]))
                if si[i]["nFix"] != '': nFix.append(float(si[i]["nFix"]))
                if sj[i]["nFix"] != '': nFix.append(float(sj[i]["nFix"]))

                if sa[i]["nRefix"] != '': nRefix.append(float(sa[i]["nRefix"]))
                if sb[i]["nRefix"] != '': nRefix.append(float(sb[i]["nRefix"]))
                if sc[i]["nRefix"] != '': nRefix.append(float(sc[i]["nRefix"]))
                if sd[i]["nRefix"] != '': nRefix.append(float(sd[i]["nRefix"]))
                if se[i]["nRefix"] != '': nRefix.append(float(se[i]["nRefix"]))
                if sf[i]["nRefix"] != '': nRefix.append(float(sf[i]["nRefix"]))
                if sg[i]["nRefix"] != '': nRefix.append(float(sg[i]["nRefix"]))
                if sh[i]["nRefix"] != '': nRefix.append(float(sh[i]["nRefix"]))
                if si[i]["nRefix"] != '': nRefix.append(float(si[i]["nRefix"]))
                if sj[i]["nRefix"] != '': nRefix.append(float(sj[i]["nRefix"]))

                if sa[i]["Re_read_prob"] != '': Re_read_prob.append(float(sa[i]["Re_read_prob"]))
                if sb[i]["Re_read_prob"] != '': Re_read_prob.append(float(sb[i]["Re_read_prob"]))
                if sc[i]["Re_read_prob"] != '': Re_read_prob.append(float(sc[i]["Re_read_prob"]))
                if sd[i]["Re_read_prob"] != '': Re_read_prob.append(float(sd[i]["Re_read_prob"]))
                if se[i]["Re_read_prob"] != '': Re_read_prob.append(float(se[i]["Re_read_prob"]))
                if sf[i]["Re_read_prob"] != '': Re_read_prob.append(float(sf[i]["Re_read_prob"]))
                if sg[i]["Re_read_prob"] != '': Re_read_prob.append(float(sg[i]["Re_read_prob"]))
                if sh[i]["Re_read_prob"] != '': Re_read_prob.append(float(sh[i]["Re_read_prob"]))
                if si[i]["Re_read_prob"] != '': Re_read_prob.append(float(si[i]["Re_read_prob"]))
                if sj[i]["Re_read_prob"] != '': Re_read_prob.append(float(sj[i]["Re_read_prob"]))

                if sa[i]["Fix_prob"] != '': Fix_prob.append(float(sa[i]["Fix_prob"]))
                if sb[i]["Fix_prob"] != '': Fix_prob.append(float(sb[i]["Fix_prob"]))
                if sc[i]["Fix_prob"] != '': Fix_prob.append(float(sc[i]["Fix_prob"]))
                if sd[i]["Fix_prob"] != '': Fix_prob.append(float(sd[i]["Fix_prob"]))
                if se[i]["Fix_prob"] != '': Fix_prob.append(float(se[i]["Fix_prob"]))
                if sf[i]["Fix_prob"] != '': Fix_prob.append(float(sf[i]["Fix_prob"]))
                if sg[i]["Fix_prob"] != '': Fix_prob.append(float(sg[i]["Fix_prob"]))
                if sh[i]["Fix_prob"] != '': Fix_prob.append(float(sh[i]["Fix_prob"]))
                if si[i]["Fix_prob"] != '': Fix_prob.append(float(si[i]["Fix_prob"]))
                if sj[i]["Fix_prob"] != '': Fix_prob.append(float(sj[i]["Fix_prob"]))

                if sa[i]["First_fix_dur"] != '': First_fix_dur.append(float(sa[i]["First_fix_dur"]))
                if sb[i]["First_fix_dur"] != '': First_fix_dur.append(float(sb[i]["First_fix_dur"]))
                if sc[i]["First_fix_dur"] != '': First_fix_dur.append(float(sc[i]["First_fix_dur"]))
                if sd[i]["First_fix_dur"] != '': First_fix_dur.append(float(sd[i]["First_fix_dur"]))
                if se[i]["First_fix_dur"] != '': First_fix_dur.append(float(se[i]["First_fix_dur"]))
                if sf[i]["First_fix_dur"] != '': First_fix_dur.append(float(sf[i]["First_fix_dur"]))
                if sg[i]["First_fix_dur"] != '': First_fix_dur.append(float(sg[i]["First_fix_dur"]))
                if sh[i]["First_fix_dur"] != '': First_fix_dur.append(float(sh[i]["First_fix_dur"]))
                if si[i]["First_fix_dur"] != '': First_fix_dur.append(float(si[i]["First_fix_dur"]))
                if sj[i]["First_fix_dur"] != '': First_fix_dur.append(float(sj[i]["First_fix_dur"]))

                if sa[i]["First_pass_dur"] != '': First_pass_dur.append(float(sa[i]["First_pass_dur"]))
                if sb[i]["First_pass_dur"] != '': First_pass_dur.append(float(sb[i]["First_pass_dur"]))
                if sc[i]["First_pass_dur"] != '': First_pass_dur.append(float(sc[i]["First_pass_dur"]))
                if sd[i]["First_pass_dur"] != '': First_pass_dur.append(float(sd[i]["First_pass_dur"]))
                if se[i]["First_pass_dur"] != '': First_pass_dur.append(float(se[i]["First_pass_dur"]))
                if sf[i]["First_pass_dur"] != '': First_pass_dur.append(float(sf[i]["First_pass_dur"]))
                if sg[i]["First_pass_dur"] != '': First_pass_dur.append(float(sg[i]["First_pass_dur"]))
                if sh[i]["First_pass_dur"] != '': First_pass_dur.append(float(sh[i]["First_pass_dur"]))
                if si[i]["First_pass_dur"] != '': First_pass_dur.append(float(si[i]["First_pass_dur"]))
                if sj[i]["First_pass_dur"] != '': First_pass_dur.append(float(sj[i]["First_pass_dur"]))

                if sa[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sa[i]["Tot_regres_from_dur"]))
                if sb[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sb[i]["Tot_regres_from_dur"]))
                if sc[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sc[i]["Tot_regres_from_dur"]))
                if sd[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sd[i]["Tot_regres_from_dur"]))
                if se[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(se[i]["Tot_regres_from_dur"]))
                if sf[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sf[i]["Tot_regres_from_dur"]))
                if sg[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sg[i]["Tot_regres_from_dur"]))
                if sh[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sh[i]["Tot_regres_from_dur"]))
                if si[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(si[i]["Tot_regres_from_dur"]))
                if sj[i]["Tot_regres_from_dur"] != '': Tot_regres_from_dur.append(float(sj[i]["Tot_regres_from_dur"]))

                if sa[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sa[i]["n_2_fix_prob"]))
                if sb[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sb[i]["n_2_fix_prob"]))
                if sc[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sc[i]["n_2_fix_prob"]))
                if sd[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sd[i]["n_2_fix_prob"]))
                if se[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(se[i]["n_2_fix_prob"]))
                if sf[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sf[i]["n_2_fix_prob"]))
                if sg[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sg[i]["n_2_fix_prob"]))
                if sh[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sh[i]["n_2_fix_prob"]))
                if si[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(si[i]["n_2_fix_prob"]))
                if sj[i]["n_2_fix_prob"] != '': n_2_fix_prob.append(float(sj[i]["n_2_fix_prob"]))

                if sa[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sa[i]["n_1_fix_prob"]))
                if sb[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sb[i]["n_1_fix_prob"]))
                if sc[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sc[i]["n_1_fix_prob"]))
                if sd[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sd[i]["n_1_fix_prob"]))
                if se[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(se[i]["n_1_fix_prob"]))
                if sf[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sf[i]["n_1_fix_prob"]))
                if sg[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sg[i]["n_1_fix_prob"]))
                if sh[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sh[i]["n_1_fix_prob"]))
                if si[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(si[i]["n_1_fix_prob"]))
                if sj[i]["n_1_fix_prob"] != '': n_1_fix_prob.append(float(sj[i]["n_1_fix_prob"]))

                if sa[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sa[i]["n+2_fix_prob"]))
                if sb[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sb[i]["n+2_fix_prob"]))
                if sc[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sc[i]["n+2_fix_prob"]))
                if sd[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sd[i]["n+2_fix_prob"]))
                if se[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(se[i]["n+2_fix_prob"]))
                if sf[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sf[i]["n+2_fix_prob"]))
                if sg[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sg[i]["n+2_fix_prob"]))
                if sh[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sh[i]["n+2_fix_prob"]))
                if si[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(si[i]["n+2_fix_prob"]))
                if sj[i]["n+2_fix_prob"] != '': n_plus_2_fix_prob.append(float(sj[i]["n+2_fix_prob"]))

                if sa[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sa[i]["n+1_fix_prob"]))
                if sb[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sb[i]["n+1_fix_prob"]))
                if sc[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sc[i]["n+1_fix_prob"]))
                if sd[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sd[i]["n+1_fix_prob"]))
                if se[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(se[i]["n+1_fix_prob"]))
                if sf[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sf[i]["n+1_fix_prob"]))
                if sg[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sg[i]["n+1_fix_prob"]))
                if sh[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sh[i]["n+1_fix_prob"]))
                if si[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(si[i]["n+1_fix_prob"]))
                if sj[i]["n+1_fix_prob"] != '': n_plus_1_fix_prob.append(float(sj[i]["n+1_fix_prob"]))

                if sa[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sa[i]["n_2_fix_dur"]))
                if sb[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sb[i]["n_2_fix_dur"]))
                if sc[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sc[i]["n_2_fix_dur"]))
                if sd[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sd[i]["n_2_fix_dur"]))
                if se[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(se[i]["n_2_fix_dur"]))
                if sf[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sf[i]["n_2_fix_dur"]))
                if sg[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sg[i]["n_2_fix_dur"]))
                if sh[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sh[i]["n_2_fix_dur"]))
                if si[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(si[i]["n_2_fix_dur"]))
                if sj[i]["n_2_fix_dur"] != '': n_2_fix_dur.append(float(sj[i]["n_2_fix_dur"]))

                if sa[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sa[i]["n_1_fix_dur"]))
                if sb[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sb[i]["n_1_fix_dur"]))
                if sc[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sc[i]["n_1_fix_dur"]))
                if sd[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sd[i]["n_1_fix_dur"]))
                if se[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(se[i]["n_1_fix_dur"]))
                if sf[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sf[i]["n_1_fix_dur"]))
                if sg[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sg[i]["n_1_fix_dur"]))
                if sh[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sh[i]["n_1_fix_dur"]))
                if si[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(si[i]["n_1_fix_dur"]))
                if sj[i]["n_1_fix_dur"] != '': n_1_fix_dur.append(float(sj[i]["n_1_fix_dur"]))

                if sa[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sa[i]["n+2_fix_dur"]))
                if sb[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sb[i]["n+2_fix_dur"]))
                if sc[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sc[i]["n+2_fix_dur"]))
                if sd[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sd[i]["n+2_fix_dur"]))
                if se[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(se[i]["n+2_fix_dur"]))
                if sf[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sf[i]["n+2_fix_dur"]))
                if sg[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sg[i]["n+2_fix_dur"]))
                if sh[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sh[i]["n+2_fix_dur"]))
                if si[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(si[i]["n+2_fix_dur"]))
                if sj[i]["n+2_fix_dur"] != '': n_plus_2_fix_dur.append(float(sj[i]["n+2_fix_dur"]))

                if sa[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sa[i]["n+1_fix_dur"]))
                if sb[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sb[i]["n+1_fix_dur"]))
                if sc[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sc[i]["n+1_fix_dur"]))
                if sd[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sd[i]["n+1_fix_dur"]))
                if se[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(se[i]["n+1_fix_dur"]))
                if sf[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sf[i]["n+1_fix_dur"]))
                if sg[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sg[i]["n+1_fix_dur"]))
                if sh[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sh[i]["n+1_fix_dur"]))
                if si[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(si[i]["n+1_fix_dur"]))
                if sj[i]["n+1_fix_dur"] != '': n_plus_1_fix_dur.append(float(sj[i]["n+1_fix_dur"]))

                if len(Fix_prob) >= 5:
                    fix_prob = "1.0"
                else:
                    fix_prob = "0.0"

                re_read_prob = Counter(Re_read_prob).most_common(1)[0][0]
                n_2_prob = Counter(n_2_fix_prob).most_common(1)[0][0]
                n_1_prob = Counter(n_1_fix_prob).most_common(1)[0][0]
                n_plus_1_prob = Counter(n_plus_1_fix_prob).most_common(1)[0][0]
                n_plus_2_prob = Counter(n_plus_2_fix_prob).most_common(1)[0][0]
                if Mean_fix_dur:
                    avg_mean_fix_dur = sum(Mean_fix_dur) / len(Mean_fix_dur)
                else:
                    avg_mean_fix_dur = 0.0
                if First_fix_dur:
                    avg_first_fix_dur = sum(First_fix_dur) / len(First_fix_dur)
                else:
                    avg_first_fix_dur = 0.0
                if First_pass_dur:
                    avg_first_pass_dur = sum(First_pass_dur) / len(First_pass_dur)
                else:
                    avg_first_pass_dur = 0.0
                if Tot_fix_dur:
                    avg_tot_fix_dur = sum(Tot_fix_dur) / len(Tot_fix_dur)
                else:
                    avg_tot_fix_dur = 0.0
                if Tot_regres_from_dur:
                    avg_tot_regres_from_dur = sum(Tot_regres_from_dur) / len(Tot_regres_from_dur)
                else:
                    avg_tot_regres_from_dur = 0.0
                if n_2_fix_dur:
                    avg_n_2_fix_dur = sum(n_2_fix_dur) / len(n_2_fix_dur)
                else:
                    avg_n_2_fix_dur = 0.0
                if n_1_fix_dur:
                    avg_n_1_fix_dur = sum(n_1_fix_dur) / len(n_1_fix_dur)
                else:
                    avg_n_1_fix_dur = 0.0
                if n_plus_1_fix_dur:
                    avg_n_plus_1_fix_dur = sum(n_plus_1_fix_dur) / len(n_plus_1_fix_dur)
                else:
                    avg_n_plus_1_fix_dur = 0.0
                if n_plus_2_fix_dur:
                    avg_n_plus_2_fix_dur = sum(n_plus_2_fix_dur) / len(n_plus_2_fix_dur)
                else:
                    avg_n_plus_2_fix_dur = 0.0
                if nRefix:
                    avg_nRefix = sum(nRefix) // len(nRefix)
                else:
                    avg_nRefix = 0

                if count <= 241:
                    if sa[i]['ID'] == 1:
                        f.write("\n")
                        count += 1
                    f.write(str(sa[i]['ID']) + '\t' + sa[i]['Word'] + '\t' + "_" + '\t' + sa[i]['UniversalPOS'] + '\t'
                            + sa[i]['CPOS'] + '\t' + "_" + '\t' + str(sa[i]['Head']) + '\t' + sa[i]['DepRel'] + '\t'
                            + str(sum(nFix) // len(nFix)) + '\t' + fix_prob + '\t' + str(avg_mean_fix_dur) + "\t"
                            + str(avg_first_fix_dur) + '\t' + str(avg_first_pass_dur) + '\t' + str(
                        avg_tot_fix_dur) + '\t'
                            + str(avg_nRefix) + '\t' + str(re_read_prob) + '\t' + str(avg_tot_regres_from_dur) + '\t'
                            + str(n_2_prob) + '\t' + str(n_1_prob) + '\t' + str(n_plus_1_prob) + '\t'
                            + str(n_plus_2_prob) + '\t' + str(avg_n_2_fix_dur) + '\t' + str(avg_n_1_fix_dur) + '\t'
                            + str(avg_n_plus_1_fix_dur) + '\t' + str(avg_n_plus_2_fix_dur) + '\n')
                elif count > 241 and count <= 471:
                    if sa[i]['ID'] == 1:
                        q.write("\n")
                        count += 1
                    q.write(str(sa[i]['ID']) + '\t' + sa[i]['Word'] + '\t' + "_" + '\t' + sa[i]['UniversalPOS'] + '\t'
                            + sa[i]['CPOS'] + '\t' + "_" + '\t' + str(sa[i]['Head']) + '\t' + sa[i]['DepRel'] + '\t'
                            + str(sum(nFix) // len(nFix)) + '\t' + fix_prob + '\t' + str(avg_mean_fix_dur) + "\t"
                            + str(avg_first_fix_dur) + '\t' + str(avg_first_pass_dur) + '\t' + str(
                        avg_tot_fix_dur) + '\t'
                            + str(avg_nRefix) + '\t' + str(re_read_prob) + '\t' + str(avg_tot_regres_from_dur) + '\t'
                            + str(n_2_prob) + '\t' + str(n_1_prob) + '\t' + str(n_plus_1_prob) + '\t'
                            + str(n_plus_2_prob) + '\t' + str(avg_n_2_fix_dur) + '\t' + str(avg_n_1_fix_dur) + '\t'
                            + str(avg_n_plus_1_fix_dur) + '\t' + str(avg_n_plus_2_fix_dur) + '\n')
                else:
                    if sa[i]['ID'] == 1:
                        p.write("\n")
                        count += 1
                    p.write(str(sa[i]['ID']) + '\t' + sa[i]['Word'] + '\t' + "_" + '\t' + sa[i]['UniversalPOS'] + '\t'
                            + sa[i]['CPOS'] + '\t' + "_" + '\t' + str(sa[i]['Head']) + '\t' + sa[i]['DepRel'] + '\t'
                            + str(sum(nFix) // len(nFix)) + '\t' + fix_prob + '\t' + str(avg_mean_fix_dur) + "\t"
                            + str(avg_first_fix_dur) + '\t' + str(avg_first_pass_dur) + '\t' + str(
                        avg_tot_fix_dur) + '\t'
                            + str(avg_nRefix) + '\t' + str(re_read_prob) + '\t' + str(avg_tot_regres_from_dur) + '\t'
                            + str(n_2_prob) + '\t' + str(n_1_prob) + '\t' + str(n_plus_1_prob) + '\t'
                            + str(n_plus_2_prob) + '\t' + str(avg_n_2_fix_dur) + '\t' + str(avg_n_1_fix_dur) + '\t'
                            + str(avg_n_plus_1_fix_dur) + '\t' + str(avg_n_plus_2_fix_dur) + '\n')

print(count)

'''
print(len(sa))
print(len(sb))
print(len(sc))
print(len(sd))
print(len(se))
print(len(sf))
print(len(sg))
print(len(sh))
print(len(si))
print(len(sj))
'''

