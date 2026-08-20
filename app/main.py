import argparse
from crypt import gen_key, encrypt_file, decrypt_file
from files import backup_dir, filter_files
from dry_run import dry_run
import logging
import os 



def setup_logging():
    logging.basicConfig(
            filename='audit.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logging.info("=== Simulation Started ===")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Ransomware Simulator')

    parser.add_argument("directory", nargs="?", metavar="", default="test_dir", help="Directory to encrypt its files")
    parser.add_argument("--dry-run", action="store_true", help="Dry run: simulating encryption")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt all files")
    args = parser.parse_args()


    setup_logging()

    if not os.path.exists(args.directory):

        logging.error(f"Target directory '{args.directory}' does not exist.")

    if args.dry_run:
        dry_run(args.directory)

    elif args.decrypt:
        files, _ = filter_files(args.directory)
        for f in files:
            decrypt_file(f)
            logging.info(f"{f} hase been decrypted")

    else:
        allowed_files, disallowed_files= filter_files(args.directory)

        for f in allowed_files:
            
            logging.info(f"{f} hase been encrypted")


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

            backup_dir(args.directory)
            if not os.path.exists('key'):
                gen_key()
                logging.info("New encryption key generated.")


            for f in allowed_files:
                print(f"Encrypting {f}....")
                encrypt_file(f)


            print("Encryption finished, the key to decrypt is found in the key file ")

        else: 
            logging.info("User cancelled operation")
            print("Operation cancelled")