# This script appends txt files to the master text file

# First we import the tkinter tools for opening file dialogues
from tkinter import filedialog
from tkinter import Tk

# Then we import OS to work with file names and file sizes
import os

#import shutil to move files around
import shutil

# Import datetime to work with dates
from datetime import datetime
today = datetime.now()

# Create a Tkinter root object for working with file selection
root = Tk()
root.withdraw() 

# Open a dialog for file selection
file_paths = filedialog.askopenfilenames(title="Select book text file(s)")

# Convert the returned tuple of file paths to a list
file_paths = list(file_paths)

# Create a for loop to work through the file paths and append the values to the 
for index, file in enumerate(file_paths,start=1):
    
    # Read in the files that the user chose
    with open(file, 'r', encoding='utf-8') as source_file:
        content = source_file.read()
    
    # Open the destination file and append the content of the source file
    with open('AllText\TrainingText.txt', 'a', encoding='utf-8') as dest_file:
        dest_file.write(content)
        
    # Rename the file with an easier to read basename   
    file = os.path.basename(file)
    
    #print out the results as they finish appending
    print(f'{index}. {file} is done')

# Read the total training text file and get a word count and character count
with open('AllText\TrainingText.txt', 'r', encoding='utf-8') as training_text:
    training_text=training_text.read()
    training_text_word_count = len(training_text.split())
    training_text_character_count = len(training_text)
    training_text_size = os.path.getsize('AllText\TrainingText.txt')

# Create variables to update the word count and the character count in the readme summary file
new_character_count = (f'Current Character Count: {training_text_character_count:,}')
new_word_count = (f'Current Word Count: {training_text_word_count:,}')
new_file_size = (f'Current File Size: {training_text_size} bytes')
last_modified = (f'Latest data added: {today}')

# Insert the new character count
read_me_file=(f'FreeLLMText: A repository that stores high quality, copyright-free text for LLM training \n \n \n {new_character_count} \n {new_word_count} \n {new_file_size} \n {last_modified}')

# Write the changes to the file
with open('README.md', 'w', encoding='utf-8') as file:
    file.write(read_me_file)

print(f'Data loaded, README updated')
print(f'New size is {training_text_size} bytes')
print(f'New Word Count: {training_text_word_count:,} words')

## TODO
# Find a way to check for duplicate data
# Delete prevention
# List the files that have been written
# Create Metadata
# Move the appended files to a new folder
