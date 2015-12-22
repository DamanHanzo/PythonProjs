import string

def print_index(f_obj):
    fd = open("mainWords.txt")
    MAIN_WORDS = get_words(fd)
    index_dict = {}
    line_no = 0
    for line in f_obj:
        line_no += 1
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            if word and word in MAIN_WORDS:
                if word in index_dict:
                    index_dict[word].add(line_no)
                else:
                    index_dict[word] = {line_no}
    pretty_print_dict(index_dict)

def pretty_print_dict(index_dict):
    index_lst = [item for item in index_dict.items()]
    index_lst.sort()
    for word, line_set in index_lst:
        line_lst = [l for l in line_set]
        line_lst.sort()
        line_str = str(line_lst[0])
        for line_no in line_lst[1:]:
            line_str += ", {}".format(line_no)
        print("{:12s}:".format(word), line_str)

def get_words(file_obj):
    result_set = set()
    for line in file_obj:
        line = line.strip()
        word_lst = line.split()
        word_lst = [w.lower().strip(string.punctuation) for w in word_lst]
        for w in word_lst:
            if w:
                result_set.add(w)
    return result_set

def compare_files(file1, file2):
    f1_words, f2_words = get_words(file1), get_words(file2)
    total_words = len(f1_words | f2_words)
    total_common = len(f1_words & f2_words)
    print("The number of total words:", total_words)
    print("The number of words in common:", total_common)

def main():
    # test the index function
    print("Test of print_index:")
    file_obj1 = open("gettysBurg.txt")
    print_index(file_obj1)
    file_obj1.close()
    print()

    # test the compare_files function
    print("Test of compare_files")
    f1 = open("gettysBurg.txt")
    f2 = open("declarationOfInd.txt")
    compare_files(f1,f2)
    f1.close()
    f2.close()
