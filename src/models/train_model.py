import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run model training")
    parser.add_argument("--epochs", default=30, type=int)
    parser.add_argument("--val-split", default=0.1, type=float)
    parser.add_argument("--stop-early", default=False, action="store_true")
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    """
    Your code for model training goes here...
    
    """
    print(f"Model started training: {args.epochs} epochs remaining.")
    print(f"Using validation split of {100 * args.val_split:.0f} %.")
    if args.stop_early:
        print(f"Early stopping enabled!")


if __name__ == "__main__":
    main()

    #  run this file from the terminal with e.g. 20 epochs, val-split of 0.2 and early stopping using:
    #  python importname/models/train_model.py --epochs=20 --val-split=0.2 --stop-early
