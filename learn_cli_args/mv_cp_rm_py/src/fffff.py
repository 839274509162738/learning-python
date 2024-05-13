import argparse
import os
import shutil

from colorama import Fore, init

INPUT_NOT_PROVIDED = "Error: Src/Dst input not provided"
EXISTING_FILE = "Error: You are attempting to copy a file/directory to itself"
UNEXISTING_FILE = "Error: File/Directory does not exist"

init()


def copy(src, dst):
    if src and dst:
        src = os.path.abspath(src)
        dst = os.path.abspath(dst)
        successful = f"""
{Fore.LIGHTGREEN_EX}***Successful***: 
{Fore.LIGHTBLUE_EX}{src} {Fore.LIGHTGREEN_EX}==> {Fore.LIGHTBLUE_EX}{dst} {Fore.LIGHTYELLOW_EX}
***[OP: Copy]***
        """
        if os.path.exists(src):
            if src == dst:
                raise FileExistsError(EXISTING_FILE)
            if os.path.isdir(src):
                shutil.copytree(src, dst)
                return successful
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                return successful
        else:
            return UNEXISTING_FILE
    else:
        return INPUT_NOT_PROVIDED


def move(src, dst):
    if src and dst:
        if os.path.exists(src):
            src = os.path.abspath(src)
            dst = os.path.abspath(dst)
            if src == dst:
                raise FileExistsError(EXISTING_FILE)
            shutil.move(src, dst)
            return f"""
{Fore.LIGHTGREEN_EX}***Successful***: 
{Fore.LIGHTBLUE_EX}{src} {Fore.LIGHTGREEN_EX}==> {Fore.LIGHTBLUE_EX}{dst} {Fore.LIGHTYELLOW_EX}
***[OP: Move]***
        """
        else:
            return UNEXISTING_FILE
    else:
        return INPUT_NOT_PROVIDED


def remove(src):
    if src:
        if os.path.exists(src):
            src = os.path.abspath(src)
            if os.path.isdir(src):
                shutil.rmtree(src)
                return f"{Fore.LIGHTGREEN_EX}Successful: {Fore.LIGHTBLUE_EX}{src} {Fore.LIGHTGREEN_EX}x {Fore.LIGHTYELLOW_EX}[OP: Remove]"
            if os.path.isfile(src):
                os.remove(src)
                return f"{Fore.LIGHTGREEN_EX}Successful: {Fore.LIGHTBLUE_EX}{src} {Fore.LIGHTGREEN_EX}x {Fore.LIGHTYELLOW_EX}[OP: Remove]"
        else:
            return UNEXISTING_FILE
    else:
        return INPUT_NOT_PROVIDED


def main():
    parser = argparse.ArgumentParser(
        description="A simple program that allows you to emulate cp, mv, and rm"
    )
    parser.add_argument(
        "-cp",
        "--copy",
        nargs=2,
        type=str,
        metavar=("src", "dst"),
        help="python file.py -cp <src_file> <dst_file>",
    )
    parser.add_argument(
        "-mv",
        "--move",
        nargs=2,
        type=str,
        metavar=("src", "dst"),
        help="python file.py -mv <src_file> <dst_file>",
    )
    parser.add_argument(
        "-rm",
        "--remove",
        nargs=1,
        type=str,
        metavar="src",
        help="python file.py -rm <src_file>",
    )
    args = parser.parse_args()

    if args.copy:
        src, dst = args.copy
        print(copy(src, dst))
    elif args.move:
        src, dst = args.move
        print(move(src, dst))
    elif args.remove:
        src = args.remove[0]
        print(remove(src))


if __name__ == "__main__":
    main()
