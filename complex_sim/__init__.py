r'''Complex looking output for testing regression'''

import numpy as np
import scipy.stats as st

__all__ = ['cmplx_five']
__version__ = '0.1.0'

norm4 = st.norm(loc=0.0, scale=4.0)

def cmplx_five(alpha,beta,gamma,delta,epsilon):
    '''Complex Five Factor Function
        Let everything vary 0->10
        '''
    coeffs = [0.25, 2.0, 1.0, 1.0, 0.1, -1.0]
    result = 0.0 #intercept
    result += coeffs[0] * alpha
    result += coeffs[1] * beta*beta + beta**(1/3)
    result += coeffs[2] * np.sin(gamma/np.pi)
    result += coeffs[3] * norm4.cdf(delta)
    result += coeffs[4] * -(epsilon-4)**2+5*epsilon
    # Cross Terms
    result += coeffs[5] * delta**2 * alpha
    return result

def cmplx_four(alpha,beta,gamma,delta):
    result = alpha+beta+gamma+delta+epsilon
    return result

if __name__ == '__main__':
    print('Direct Execution')

