import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run model training")
    parser.add_argument("--data-path", type=str)
    parser.add_argument("--print-results", default=False, action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    """
    Your code for model prediction goes here...

    """
    print(f"\nModel predicting on data in {args.data_path}.")
    if args.print_results:
        print(f"\nPredictions:")
        """
        Code to show model predictions...
        """


if __name__ == "__main__":
    main()

    #  run this file and print results from the terminal using:
    #  python importname/models/predict_model.py --data-path=data/processed/exampledata.csv --print-results
