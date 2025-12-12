import argparse




def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", action="store_true", help="Graph generation")
    group.add_argument("--run", action="store_true", help="Run algorithms on the generated graphs")
    
    args = parser.parse_args()

    if args.generate:
        print("Graph generate")
    elif args.run:
        print("Run algorithms")

    





if __name__ == "__main__":
    main()