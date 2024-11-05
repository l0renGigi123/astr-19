import sys
import numpy as np
from scipy.special import erf

#compute probability of event of magnitude
#x of greate from gaussian distribution
def event_prob(x,mu=0.0,s=1.0):
    #x is value of event
    #mu is gaussian mean
    #s is SD
    z = np.fabs((x-mu)/s)
    def zfunc(z):
        return 0.5*(1.0+erf(z/2**0.5))
    
    #return probability of getting event where magnitude >= x
    return 1.0-(zfunc(z)-zfunc(-1*z))

#def main
def main():
    x = 3.0 #away from mean (default 3*sigma)
    #if another number in command line, reset x
    if(len(sys.argv)>1):
        x = float(sys.argv[1])
        
    #get even probability
    prob = event_prob(x)
    
    print(f"The Gaussian probability of events larger than |{x}| is {prob*100:6.4f}%.")
    print(f"The Gaussian probability of events smaller than |{x}| is {(1-prob)*100:6.4f}%.")    
    
#run program
if __name__=="__main__":
    main()