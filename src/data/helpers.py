import re

import numpy as np


def get_deck_letter(df):
    df_copy = df.copy()
    df_copy["Deck"] = np.nan
    for i, row in df_copy.iterrows():
        cabin_string = row["Cabin"]
        if isinstance(cabin_string, str):  # only proceed if the cabin was not NA
            deck = cabin_string[:1]
            df_copy.loc[i, "Deck"] = deck
    return df_copy


def average_cabin_numbers(df):
    df_copy = df.copy()
    df_copy["Cabin_number"] = np.nan
    for i, row in df_copy.iterrows():
        cabin_string = row["Cabin"]
        if isinstance(cabin_string, str):  # only proceed if the cabin was not NA
            numbers = [int(i) for i in re.findall(r'\d+', cabin_string)]
            if len(numbers) > 0:
                number = np.median(numbers)
                df_copy.loc[i, "Cabin_number"] = number
    return df_copy


def split_ticket_numbers(df):
    df_copy = df.copy()
    df_copy["Ticket_prenumber"] = np.nan
    df_copy["Ticket_number"] = np.nan
    for i, row in df_copy.iterrows():
        ticket_string = row["Ticket"]
        if isinstance(ticket_string, str):  # only proceed if the cabin was not NA
            ticket_substrings = ticket_string.split(" ")
            pre_number = ticket_substrings[0] if len(ticket_substrings) > 1 else "blank"
            ticket_string_split = ticket_string.split(" ")[-1]
            if ticket_string_split == "LINE":
                df_copy.loc[i, "Ticket_prenumber"] = "LINE"
                df_copy.loc[i, "Ticket_number"] = "LINE"
                continue
            number = re.findall(r'\d+', ticket_string_split)[0]
            if len(number) > 0:
                df_copy.loc[i, "Ticket_prenumber"] = pre_number
                df_copy.loc[i, "Ticket_number"] = number
    return df_copy
