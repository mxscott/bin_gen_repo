from bin_generator import BinGenerator
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--gap', '-g', type=int, default=None)
    parser.add_argument('--size', '-s', type=int, default=None)
    parser.add_argument('bedfile', type=str)
    args = parser.parse_args()

    bin = BinGenerator(args.bedfile, args.gap, args.size)

    for b in bin:
        print b
