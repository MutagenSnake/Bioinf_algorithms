import matplotlib.pyplot as plt
import itertools

# Making a skew diagram
def line_plot(numbers):
    plt.plot(numbers)
    plt.ylabel('Skew')
    plt.xlabel('Nucleotide')
    plt.show()

def graph_from_fasta(fasta):
    with open(fasta, 'r') as fasta_file:
        all_lines_list = fasta_file.readlines()
        indices = []
        skew_number = 0
        for number in range(1, len(all_lines_list)):
            line = all_lines_list[number]
            for nucleotide in line:
                if nucleotide == 'C':
                    skew_number -= 1
                    indices.append(skew_number)
                elif nucleotide == 'G':
                    skew_number += 1
                    indices.append(skew_number)
                else:
                    indices.append(skew_number)
        line_plot(indices)

def get_all_possible_sequences(lenght):
    sequences = []
    for string in map(''.join, itertools.product('ATGC', repeat=lenght)):
        sequences.append(string)
    return sequences

def get_reverse_complementary(DNA_string):
    complement_dict = {"A":"T", "C":"G", "T":"A", "G":"C"}
    DNA_string_reversed = DNA_string[::-1]
    reverse_complemantary_string = ""
    for nucleotide in DNA_string_reversed:
        reverse_complemantary_string += complement_dict[nucleotide]
    return reverse_complemantary_string

def k_mer_finder(genome, k_mer_length, max_hamming_distance):
    ''' Includes the reverse complements'''
    all_elements = get_all_possible_sequences(k_mer_length)
    all_elements_dict = {}
    for element in all_elements:
        fitting_elements = []
        for number in range(len(genome)):
            sequence_element = genome[number:(number + k_mer_length)].strip()
            if len(sequence_element) == k_mer_length:
                hamming = 0
                for number in range(k_mer_length):
                    if sequence_element[number] == element[number]:
                        pass
                    else:
                        hamming += 1
                if hamming <= int(max_hamming_distance):
                    fitting_elements.append(sequence_element)
                # same for reverse complementary
                hamming_reverse = 0
                for number in range(k_mer_length):
                    if sequence_element[number] == get_reverse_complementary(element)[number]:
                        pass
                    else:
                        hamming_reverse += 1
                if hamming_reverse <= int(max_hamming_distance):
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


def sequence_extractor(fasta, start, end):
    with open(fasta, 'r') as fasta_file:
        all_lines_list = fasta_file.readlines()
        one_list = []
        for number in range(1, len(all_lines_list)):
            for nucleotide in all_lines_list[number]:
                one_list.append(nucleotide)
        genome_element = ''
        for number in range(start,end):
            genome_element += one_list[number]
        return genome_element




sequence = sequence_extractor('Salmonella enterica.fasta', 0, 500)

print(k_mer_finder(sequence, 5, 1))