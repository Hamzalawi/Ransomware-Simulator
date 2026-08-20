import os
import shutil

def listing_files(dir):

    all_files=[]
    text_files = []   
    print(f'Inside the {dir} directory there is the following files')

    for root, dirs, files in os.walk(dir):
        for f in files:

            all_files.append(f)

            name,ext = os.path.splitext(f)
            if ext == '.txt':
                text_files.append(f)

            print(f'{os.path.join(root, f)}    ext: {ext}')

        print(f'directory {root} contains {len(files)}')
        print('_'*30)

    print(f"There are {len(all_files)} files found.")
    print("these are the text files:")
    for x in text_files:
        print(text_files)




def backup_dir(dir):

    backup = dir + "_backup"
    print(backup)

    shutil.copytree(dir, backup, dirs_exist_ok=True)
    print(f'Successfully backed up {dir} to {backup}')


if __name__ == "__main__":

    test_dir = 'test_dir'
    listing_files(test_dir)
    backup_dir(test_dir)
