
true_parse = open("sample_test.conllu", encoding='utf-8').readlines()
base_parse = open("res.conllu", encoding='utf-8').readlines()
parse = open("myModel/result.conllu", encoding='utf-8').readlines()

base_parse_cor = 0
base_parse_incor = 0
base_cor_parse_incor = 0
base_incor_parse_cor = 0
count = 0

for idx in range(len(true_parse)):
    if len(true_parse[idx]) > 2:
        if true_parse[idx].split()[1] == base_parse[idx].split()[1] and true_parse[idx].split()[1] == parse[idx].split()[1]:
            if true_parse[idx].split()[6] == base_parse[idx].split()[6] and true_parse[idx].split()[6] == parse[idx].split()[6] \
                    and true_parse[idx].split()[7] == base_parse[idx].split()[7] and true_parse[idx].split()[7] == parse[idx].split()[7]:
                base_parse_cor += 1
            elif (true_parse[idx].split()[6] != base_parse[idx].split()[6] or true_parse[idx].split()[7] != base_parse[idx].split()[7]) \
                    and (true_parse[idx].split()[6] != parse[idx].split()[6] or true_parse[idx].split()[7] != parse[idx].split()[7]):
                base_parse_incor += 1
            elif (true_parse[idx].split()[6] != base_parse[idx].split()[6] or true_parse[idx].split()[7] != base_parse[idx].split()[7]) \
                    and true_parse[idx].split()[6] == parse[idx].split()[6] and true_parse[idx].split()[7] == parse[idx].split()[7]:
                base_incor_parse_cor += 1
            elif (true_parse[idx].split()[6] != parse[idx].split()[6] or true_parse[idx].split()[7] != parse[idx].split()[7]) \
                    and true_parse[idx].split()[6] == base_parse[idx].split()[6] and true_parse[idx].split()[7] == base_parse[idx].split()[7]:
                base_cor_parse_incor += 1
        else:
            print("something isn't aligned")
    else:
        count += 1

print(base_cor_parse_incor + base_incor_parse_cor + base_parse_incor + base_parse_cor)
print(count)

