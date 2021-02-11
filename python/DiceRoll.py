
# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from Random import Random

# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default single dice-roll probability
    prob = np.full(6, 1/6.)

    # default number of dice rolls
    NSample = 1

    # output file defaults
    doOutputFile = False

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-prob' in sys.argv:
        p = sys.argv.index('-prob')
        ptemp = float(sys.argv[p+1])
        prob = np.asarray(ptemp)
    if '-NSample' in sys.argv:
        p = sys.argv.index('-NSample')
        Nt = int(sys.argv[p+1])
        if Nt > 0:
            NSample = Nt
    if '-output' in sys.argv:
        p = sys.argv.index('-output')
        OutputFileName = sys.argv[p+1]
        doOutputFile = True

    # class instance of our Random class using seed
    random = Random(seed)
    dice = random.Dice(NSample, p =prob)
    
    # create histogram of our data
    counts, bins = np.histogram(dice, bins=6)
    plt.bar([1,2,3,4,5,6], counts/NSample)

    # plot formating options
    plt.xlabel('value')
    plt.ylabel('Probability')
    plt.title('random dice roll')

    plt.savefig('diceroll.png')

    # show figure 
    plt.show()
    

    if doOutputFile:   
        np.save(OutputFileName,dice)
        
    else:
        print(dice)
   
