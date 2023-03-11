from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        required=True,
        help="argument for ζ(s)",
        type=complex,
    )
    parser.add_argument(
        "-n",
        default=10,
        help="number of elements in series",
        type=int,
    )
    return parser.parse_args()

## Very incorrect for `s`` close to 1.
def main():
    args = parse_args()
    c = complex(0)
    for i in range(1, args.n + 1):
        c += 1 / pow(i, args.s)
    print(f"{c:.5}")

if __name__ == '__main__':
    main()
