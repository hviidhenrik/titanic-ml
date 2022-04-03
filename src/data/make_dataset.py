from pathlib import Path

import pandas as pd

from src.config import PATH_DATA_RAW, PATH_DATA_PROCESSED
from src.data.helpers import get_deck_letter, average_cabin_numbers, split_ticket_numbers

# load data
x = pd.read_csv(Path(PATH_DATA_RAW) / "train.csv")
x = x.convert_dtypes()
y = x["Survived"]

# do some feature engineering
x_copy = x.copy()
x_copy = get_deck_letter(x_copy)
x_copy = average_cabin_numbers(x_copy)
x_copy = split_ticket_numbers(x_copy)

x_copy = x_copy.drop(columns=["Cabin", "Ticket"])

x_copy.to_csv(PATH_DATA_PROCESSED / "train.csv")
