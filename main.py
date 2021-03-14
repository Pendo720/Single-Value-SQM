import random
import singleValueSqm

def main():
    vals = [random.uniform(0, 4) for x in range(4)]
    svsqm = singleValueSqm.singleValueSqm(vals)
    svsqm.plotValues()

if __name__ == "__main__":
    main()