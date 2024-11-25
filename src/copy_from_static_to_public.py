import os
import shutil

def setup_destination_dir(destination_dir):
    if os.path.exists(destination_dir):
        print(f"The '{destination_dir}' directory exists - deleting...")
        shutil.rmtree(destination_dir)

    print(f"(Re)creating the {destination_dir} directory in the root of the project.")    
    os.mkdir(destination_dir)

    print(f"Checking to ensure {destination_dir} exists at the root of the project...")
    if os.path.exists(destination_dir):
        print(f"The {destination_dir} directory exists.")
    else: 
        raise Exception(f"Something went wrong: the {destination_dir} directory does not exist in the root of the project.")
    
def copy_files(source_dir, destination_dir):
    entry_list = os.listdir(source_dir)

    if len(entry_list) == 0:
        print("There are no more files to copy. Terminating copy procedure.")
    else:
        for entry in os.listdir(source_dir):
            if os.path.isfile(f"{source_dir}/{entry}"):
                shutil.copy(f"{source_dir}/{entry}", f"{destination_dir}/{entry}")
                print(f"Successfully copied '{source_dir}/{entry}' to '{destination_dir}/{entry}'.")
            else: 
                print(f"Creating sub-directory '{entry}' in '{destination_dir}'.")
                os.mkdir(f"{destination_dir}/{entry}")
                copy_files(os.path.join(source_dir, entry), os.path.join(destination_dir, entry))

def copy_from_static_to_public(source_dir, destination_dir):
    setup_destination_dir(destination_dir)
    if os.path.exists(source_dir):
        copy_files(source_dir, destination_dir)
    else:
        raise Exception(f"There is no {source_dir} directory in the root of the project. A source directory and a destination directory are required to carry out the copy procedure.")
