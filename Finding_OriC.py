import linecache
import itertools

'''Textbook problem 1A'''
def textbook_1A(text,pattern):
    count = 0
    text_len = len(str(text))
    pattern_len = len(str(pattern))
    for number in range(0,text_len):
        element = text[number:(number+pattern_len)]
        if element == pattern:
            count += 1

    return count

'''Textbook problem 1B'''
def textbook_1B(text, length):
    k_mer_list = []
    text_len = len(str(text))
    for number in range(0,text_len):
        element = text[number:(number+length)]
        if len(element) == length:
            k_mer_list.append(element)
    k_mer_dict = {}
    for element in k_mer_list:
        k_mer_dict[element] = k_mer_list.count(element)
    max_count = 0
    for key in k_mer_dict:
        if max_count < k_mer_dict[key]:
            max_count = k_mer_dict[key]
    longest_k_mers = []
    for key in k_mer_dict:
        if max_count == k_mer_dict[key]:
            longest_k_mers.append(key)
    return ' '.join(longest_k_mers)

'''Textbook problem 1C'''
def textbook_1C(DNA_string):
    complement_dict = {"A":"T", "C":"G", "T":"A", "G":"C"}
    DNA_string_reversed = DNA_string[::-1]
    reverse_complemantary_string = ""
    for nucleotide in DNA_string_reversed:
        reverse_complemantary_string += complement_dict[nucleotide]
    return reverse_complemantary_string

'''Textbook problem 1D'''
def textbook_1D(genome, pattern):
    indexes = []
    genome_len = len(genome)
    pattern_len = len(pattern)
    for number in range(0, genome_len):
        element = genome[number:(number+pattern_len)]
        if element == pattern:
            indexes.append(number)
    return ' '.join(str(e) for e in indexes)

'''Textbook problem 1E'''
def textbook_1E(genome, k, L, t):
    '''
    k - k-mer lenght
    L -  genome fragment length
    t - times repeated per L
    '''
    positive_k_mers = []
    for number in range(0, len(genome)):
        genome_element = genome[number:(number+L)]
        if len(genome_element) == L:
            #Working on one genome element
            k_mer_list = []
            for number in range(0, L):
                if len(genome_element[number:(number+k)]) == k:
                    k_mer_list.append(genome_element[number:(number+k)])
            k_mer_dict = {}
            for element in k_mer_list:
                if k_mer_list.count(element) >= t:
                    k_mer_dict[element] = k_mer_list.count(element)
                    positive_k_mers.append(element)

    #remove dublicates
    positive_no_dub = list(dict.fromkeys(positive_k_mers))
    return ' '.join(positive_no_dub)

'''Textbook problem 1F'''

def textbook_1F(sequence):
    skew_number = 0
    skew_list = [0]
    for nucleotide in sequence:
        if nucleotide == 'C':
            skew_number -= 1
            skew_list.append(skew_number)
        elif nucleotide == 'G':
            skew_number += 1
            skew_list.append(skew_number)
        else:
            skew_list.append(skew_number)
    lowest_value = min(skew_list)
    indices = []
    for idx, value in enumerate(skew_list):
        if value == lowest_value:
            indices.append(idx)

    return ' '.join(str(e) for e in indices)

'''Textbook task 1G'''
def textbook_1G(sequence1, sequnece2):
    hamming = 0
    for number in range(len(sequence1)):
        if sequence1[number] == sequnece2[number]:
            pass
        else:
            hamming += 1

    return hamming

'''Textbook task 1H'''
def textbook_1H(pattern, sequence, hamming_max):
    pattern_stripped = pattern.strip()
    sequence_len = len(sequence)
    starting_positions = []
    for number_seq in range(sequence_len):
        sequence_element = sequence[number_seq:(number_seq+len(pattern_stripped))]
        if len(sequence_element) == len(pattern_stripped):
            hamming = 0
            for number in range(len(pattern_stripped)):
                if sequence_element[number] == pattern_stripped[number]:
                    pass
                else:
                    hamming += 1
            if hamming <= int(hamming_max):
                starting_positions.append(number_seq)
    return ' '.join(str(e) for e in starting_positions)


'''Textbook task 1I'''
def textbook_1I(genome, k_integer, d_integer):
    all_elements = []
    all_elements_nested = []
    final_elements = []
    for number in range(len(genome)):
        sequence_element = genome[number:(number+k_integer)]
        if len(sequence_element) == k_integer:
            all_elements.append(sequence_element)
    for element in all_elements:
        nested_elements = []
        for number in range(len(genome)):
            sequence_element = genome[number:(number + k_integer)]
            if len(sequence_element) == k_integer:
                nested_elements.append(element)
                hamming = 0
                for number in range(k_integer):
                    if sequence_element[number] == element[number]:
                        pass
                    else:
                        hamming += 1
                if hamming <= int(d_integer):
                    nested_elements.append(sequence_element)
        all_elements_nested.append(nested_elements)
    longest = len(max(all_elements_nested, key=len))
    for element in all_elements_nested:
        if len(element) == longest:
            final_elements.append(element[0])
    return ' '.join(str(e) for e in final_elements)


def get_all_possible_sequences(lenght):
    sequences = []
    for string in map(''.join, itertools.product('ATGC', repeat=lenght)):
        sequences.append(string)
    return sequences

def textbook_1I_restart(genome, k_integer, d_integer):
    all_elements = get_all_possible_sequences(k_integer)
    all_elements_dict = {}
    for element in all_elements:
        fitting_elements = []
        for number in range(len(genome)):
            sequence_element = genome[number:(number + k_integer)].strip()
            if len(sequence_element) == k_integer:
                hamming = 0
                for number in range(k_integer):
                    if sequence_element[number] == element[number]:
                        pass
                    else:
                        hamming += 1
                if hamming <= int(d_integer):
                    fitting_elements.append(sequence_element)
        all_elements_dict[element] = fitting_elements

    only_valid_dict = {}
    longest = 0
    for key in all_elements_dict:
        if len(all_elements_dict[key]) > longest:
            longest = len(all_elements_dict[key])
    for key in all_elements_dict:
        if len(all_elements_dict[key]) == longest:
            only_valid_dict[key] = all_elements_dict[key]
    final_list = []
    for key in only_valid_dict:
        final_list.append(key)
    return ' '.join(str(e) for e in final_list)


def textbook_1J(genome, k_integer, d_integer):
    all_elements = get_all_possible_sequences(k_integer)
    all_elements_dict = {}
    for element in all_elements:
        fitting_elements = []
        for number in range(len(genome)):
            sequence_element = genome[number:(number + k_integer)].strip()
            if len(sequence_element) == k_integer:
                hamming = 0
                for number in range(k_integer):
                    if sequence_element[number] == element[number]:
                        pass
                    else:
                        hamming += 1
                if hamming <= int(d_integer):
                    fitting_elements.append(sequence_element)
                #same for reverse complementary
                hamming_reverse = 0
                for number in range(k_integer):
                    if sequence_element[number] == textbook_1C(element)[number]:
                        pass
                    else:
                        hamming_reverse += 1
                if hamming_reverse <= int(d_integer):
                    fitting_elements.append(sequence_element)
        all_elements_dict[element] = fitting_elements

    only_valid_dict = {}
    longest = 0
    for key in all_elements_dict:
        if len(all_elements_dict[key]) > longest:
            longest = len(all_elements_dict[key])
    for key in all_elements_dict:
        if len(all_elements_dict[key]) == longest:
            only_valid_dict[key] = all_elements_dict[key]
    final_list = []
    for key in only_valid_dict:
        final_list.append(key)
    return ' '.join(str(e) for e in final_list)

pattern = linecache.getline('rosalind_ba1j.txt', 1)
second_line = linecache.getline('rosalind_ba1j.txt', 2).split(' ')
k_value = int(second_line[0])
d_value = int(second_line[1])

print(textbook_1J(pattern, k_value, d_value))