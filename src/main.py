import argparse
from pathlib import Path
from graph_generation import data_generator
from bruteforce import brute_force_manage


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", type=str, metavar="File_name", 
                       help="Generate graphs and save them to a file. " \
                       "Requires the file name without the file type. " \
                       "If the file already exists its contents will be overwritten.")
    group.add_argument("--run", nargs=2, metavar=("Algorithm_type", "File_name"), 
                       help="Run specific algorithm on the generated data from file. " \
                       "Possible algorithms: bruteforce, ")
    
    args = parser.parse_args()

    if args.generate:
        file_name = args.generate
        file_json = file_name + ".json"
        data_generator(file_json)
        print(f"Data has been generated and saved to the {file_name}.json.")
    elif args.run:
        algorithm, file = args.run
        folder = Path(__file__).resolve().parent.parent
        data_folder = folder / "data"
        file = file + ".json"

        if not data_folder.exists():
            raise FileNotFoundError("File with data doesn't exist.")
        
        data_file = data_folder / file

        if not data_file.exists():
            raise FileExistsError("File with data doesn't exist.")

        match (algorithm):
            case "bruteforce":
                brute_force_manage(data_file)
            case _:
                raise ValueError("Algorithm doesn't exists")




if __name__ == "__main__":
    main()