import os
import shutil

def listing_files(dir):

    all_files_path=[]
    text_files = []   

    for root, dirs, files in os.walk(dir):
        for f in files:
            path = os.path.join(root, f)
            all_files_path.append(path)

            name,ext = os.path.splitext(f)
            if ext == '.txt':
                text_files.append(f)

    return all_files_path, text_files 


BLOCKED_FILES ={
    ".exe", ".dll", ".sys", ".bat", ".sh", ".config",
}
def filter_files(dir):
    
    allowed_files= []
    disallowed_files = []

    paths, not_needed = listing_files(dir)

    for file_path in paths:
        name, ext = os.path.splitext(file_path)

        if "test" not in name or ext in BLOCKED_FILES:
            disallowed_files.append(file_path)
        else: 
            allowed_files.append(file_path)

    return allowed_files, disallowed_files



def backup_dir(dir):

    backup = dir + "_backup"
    print(backup)

    shutil.copytree(dir, backup, dirs_exist_ok=True)
    print(f'Successfully backed up {dir} to {backup}')


if __name__ == "__main__":

    test_dir = 'test_dir'
    listing_files(test_dir)
    backup_dir(test_dir)
