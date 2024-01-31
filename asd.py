import os

input_file_path = '/home/pranjal/Downloads/Attention-Was-All-I-Needed/en-ne.txt'
english_output_path = '/home/pranjal/Downloads/Attention-Was-All-I-Needed/english.txt'
nepali_output_path = '/home/pranjal/Downloads/Attention-Was-All-I-Needed/nepali.txt'

# Ensure that the output files are created if they don't exist
os.makedirs(os.path.dirname(english_output_path), exist_ok=True)
os.makedirs(os.path.dirname(nepali_output_path), exist_ok=True)

with open(input_file_path, 'r', encoding='utf-8') as input_file, \
     open(english_output_path, 'w', encoding='utf-8') as english_output_file, \
     open(nepali_output_path, 'w', encoding='utf-8') as nepali_output_file:

    for line in input_file:
        # Assuming that each line contains an English sentence followed by its Nepali translation
        english, nepali = line.strip().split('\t')  # Adjust the delimiter if necessary

        # Write to the respective output files
        english_output_file.write(english + '\n')
        nepali_output_file.write(nepali + '\n')
