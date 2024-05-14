import os
import shutil

chosen_dir = '/path/to/your/directory'

def organize_files():
    
    files = os.listdir(chosen_dir)
    
    for file_name in files:
        
        # Skip directories
        if os.path.isdir(os.path.join(chosen_dir, file_name)):
            continue
        
        # Get the file extension
        _, file_extension = os.path.splitext(file_name)
        
        # Create a directory for that file type if it doesn't already exist
        file_type_dir = os.path.join(chosen_dir, file_extension[1:].lower())
        if not os.path.exists(file_type_dir):
            os.makedirs(file_type_dir)
           
        # Move the file to its own directory 
        shutil.move(os.path.join(chosen_dir, file_name), os.path.join(file_type_dir), file_name)
    
if __name__ == "__main__":
    organize_files()