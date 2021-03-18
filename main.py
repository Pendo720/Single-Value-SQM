import random
import singleValueSqm as svsqm

def main():
    vals = [random.uniform(0, 4) for x in range(4)]
    vals = [3.8,2.7, 3.2, 3.0]
    state = svsqm.singleValueSqm(vals)
    state.showMap()

if __name__ == "__main__":
    main()