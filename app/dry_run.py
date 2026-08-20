from files import listing_files, filter_files
import os
import logging


def dry_run(dir):



    allowed_files, disallowed_files = filter_files(dir)
   
    print("Starting dry run")
    print("___________________________________________________________________________")
    print(f"\n📁 Files to be affected: {len(allowed_files)}")
    print(f"Files skipped (blocked or missing 'test'): {len(disallowed_files)}")
    print("___________________________________________________________________________")
    print("This operation will encrypt files !")
    print("Type 'YES I UNDERSTAND' to continue, or anything else to cancel:")

    answer = input("> ").strip()

    if answer  == "YES I UNDERSTAND":
        logging.info("User confirmed operation")
        print("File Encryption has started")

        for f in allowed_files:
            logging.info(f"simulating encrption for: {f}")
            print(f"Encrypting {f}....")

        print("Encryption finished, the key to decrypt is found in the key file ")

    else: 
        logging.info("User cancelled operation")
        print("Operation cancelled")

        
if __name__ == "__main__":
    
    testing_directory = "test_dir"
    print("\n" + "="*60)
    print("⚠️  RANSOMWARE SIMULATOR - EDUCATIONAL TOOL ONLY")
    print("="*60)
    dry_run(testing_directory)