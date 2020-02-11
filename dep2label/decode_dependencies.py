from dep2label.labeling import Encoding
# import dep2label.eval_dep.eval_dep.conll18_ud_eval as conll18
from argparse import ArgumentParser
import subprocess as sp


def split_label(multitag, multitask_char):
    multitag_dep = multitag.split(multitask_char)
    return multitag_dep[0:3]


def split_label_combined(multitag, multitask_char):
    labels = []
    multitag = multitag.split(multitask_char)
    m = multitag[0].split("@")
    labels.append(m[0])
    labels.append(multitag[1])
    labels.append(m[1])
    return labels


def decode(output_from_nn, path_output):
    words_with_dependencies = []
    sent_with_depend = {}
    sent_nb = 1
    count_words = 1
    enc = Encoding()

    for line in output_from_nn:

        if line != "\n":
            word, postag, label_raw = line.strip().split("\t")[0], line.strip().split("\t")[
                1], line.strip().split("\t")[-1]

            if not word == "-BOS-" and not word == "-EOS-":
                # information about rel.position and word's head (f.ex. +1@V)
                # is combined into one task and dependency relation as the
                # second task
                if "@" in label_raw and "{}" in label_raw:
                    label_dependency = split_label_combined(label_raw, "{}")

                # a label will be treated as single task where its components
                # are separated by a symbol "@"
                elif "@" in label_raw:

                    label_dependency = split_label(label_raw, "@")
                else:
                    # information in the label separated by "{}" will be
                    # treated as a separate task
                    label_dependency = split_label(label_raw, "{}")
                if label_dependency is not None:
                    label_dependency.insert(0, postag)
                    label_dependency.insert(0, word)
                    words_with_dependencies.append(label_dependency)
                    count_words += 1

        else:
            count_words = 1
            sent_with_depend.update({sent_nb: words_with_dependencies})
            sent_nb += 1
            words_with_dependencies = []

    enc.decode(sent_with_depend, path_output)


def decode_combined_tasks(output_from_nn, path_output, split_char):
    words_with_dependencies = []
    sent_with_depend = {}
    sent_nb = 1
    count_words = 1
    enc = Encoding()
    for line in output_from_nn:
        if line != "\n":
            word, postag, label_raw = line.strip().split("\t")[0], line.strip().split("\t")[1], \
                                      line.strip().split("\t")[-1]

            if not word == "-BOS-" and not word == "-EOS-":
                label_dependency = split_label_combined(label_raw, split_char)
                if label_dependency is not None:
                    label_dependency.insert(0, postag)
                    label_dependency.insert(0, word)
                    words_with_dependencies.append(label_dependency)
                    count_words += 1

        else:
            count_words = 1
            sent_with_depend.update({sent_nb: words_with_dependencies})
            sent_nb += 1
            words_with_dependencies = []

    enc.decode(sent_with_depend, path_output)


def evaluate_dependencies(gold, path_output):
    # EVALUATE on conllu
    """
    subparser = ArgumentParser()
    subparser.add_argument("gold_file", type=str,
                           help="Name of the CoNLL-U file with the gold data.")
    subparser.add_argument("system_file", type=str,
                           help="Name of the CoNLL-U file with the predicted data.")
    subparser.add_argument("--verbose", "-v", default=False, action="store_true",
                           help="Print all metrics.")
    subparser.add_argument("--counts", "-c", default=False, action="store_true",
                           help="Print raw counts of correct/gold/system/aligned words instead of prec/rec/F1 for all metrics.")

    subargs = subparser.parse_args([gold, path_output])

    # Evaluate
    evaluation = conll18.evaluate_wrapper(subargs)

    uas = 100 * evaluation["UAS"].f1
    las = 100 * evaluation["LAS"].f1

    print("UAS: "+repr(uas)+" LAS: "+repr(las))
    return las


    """
    '''
    with open(path_output, "r") as f:
        lins = f.read()
    with open("dev.conllu", 'w') as f:
        f.write(lins)
    '''
    output = sp.check_output(
        "perl dep2label/eval_dep/eval-spmrl.pl -p -q -g " + gold + " -s " + path_output, shell=True)

    lines = output.decode().split('\n')

    las = float(lines[0].split()[9])
    uas = float(lines[1].split()[9])
    print("UAS: " + repr(uas) + " LAS: " + repr(las))

    return las
