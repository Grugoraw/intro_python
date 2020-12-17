from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('--output', type=float)
parser.add_argument('--rate', type=float)
parser.add_argument('--premium', type=float)
args = parser.parse_args()
salary = args.output * args.rate + args.premium
print(salary)