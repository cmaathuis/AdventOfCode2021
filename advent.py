#!/usr/bin/python3
import argparse
import os


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Enter a day: ")
    parser.add_argument("-d", "--day", type=int, choices=range(1, 26))
    args = parser.parse_args()
    validate_args(parser, args)
    return args


def validate_args(parser: argparse.ArgumentParser, args: argparse.Namespace):
    my_path = get_path(args.day)
    if not os.path.isfile(my_path):
        parser.error(f"File does not exist. {my_path}")


def get_path(day: int) -> str:
    filename = f"day{day}_input.txt"
    return os.path.join(os.path.dirname(__file__), "inputs", filename)


def read_input_file(day: int) -> str:
    my_path = get_path(day)
    with open(my_path, "r") as input_file:
        text = input_file.read()
    return text


def execute_day(day: int, input_text: str):
    dayname = f"day{day}"
    exec(f"import {dayname}")
    eval(f"{dayname}.{dayname}(input_text)")


def main():
    args = parse_args()
    input_text = read_input_file(args.day).strip()
    execute_day(args.day, input_text)


if __name__ == "__main__":
    main()
