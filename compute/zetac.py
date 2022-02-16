from argparse import ArgumentParser
from scipy.special import zetac


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        required=True,
        help="argument for ζ(s)"
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print(zetac(float(args.s)))

if __name__ == '__main__':
    main()
