import argparse
from graph_generation import data_generator


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", type=str, metavar="File_name", 
                       help="Generate graphs and save them to a file. " \
                       "Requires the file name without the file type. " \
                       "If the file already exists its contents will be overwritten.")
    group.add_argument("--run", action="store_true", help="Run algorithms on the generated graphs")
    
    args = parser.parse_args()

    if args.generate:
        file_name = args.generate
        file_json = file_name + ".json"
        data_generator(file_json)
        print(f"Data has been generated and saved to the {file_name}.json.")
    elif args.run:
        print("Run algorithms")

    





if __name__ == "__main__":
    main()