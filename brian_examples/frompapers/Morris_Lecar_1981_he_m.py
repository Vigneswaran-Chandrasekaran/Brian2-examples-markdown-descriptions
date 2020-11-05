# modify cpp standalone

from brian2 import *
from brian2tools import mdexport
from brian2tools.mdexport import MdExpander
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--github_md', type=bool, default=False, help='Github md')
parser.add_argument('--filename', type=str, default='', help='File name')
parser.add_argument('--brian_verbose', type=bool, default=False,
                    help='Brian verbose')

args = parser.parse_args()

custom = MdExpander(brian_verbose=args.brian_verbose, github_md=args.github_md)
set_device('markdown', expander=custom, filename=args.filename)

'''
Morris-Lecar model

Reproduces Fig. 9 of:

Catherine Morris and Harold Lecar.
“Voltage Oscillations in the Barnacle Giant Muscle Fiber.”
Biophysical Journal 35, no. 1 (1981): 193–213.
'''
from brian2 import *
#set_device('cpp_standalone')
defaultclock.dt = 0.01*ms

g_L = 2*mS
g_Ca = 4*mS
g_K = 8*mS
V_L = -50*mV
V_Ca = 100*mV
V_K = -70*mV
lambda_n__max = 1.0/(15*ms)
V_1 = 10*mV
V_2 = 15*mV  # Note that Figure caption says -15 which seems to be a typo
V_3 = -1*mV
V_4 = 14.5*mV
C = 20*uF


# V,N-reduced system (Eq. 9 in article), note that the variables M and N (and lambda_N, etc.)
# have been renamed to m and n to better match the Hodgkin-Huxley convention, and because N has
# a reserved meaning in Brian (number of neurons)
eqs = '''
dV/dt = (-g_L*(V - V_L) - g_Ca*m_inf*(V - V_Ca) - g_K*n*(V - V_K) + I)/C : volt
dn/dt = lambda_n*(n_inf - n) : 1
m_inf = 0.5*(1 + tanh((V - V_1)/V_2)) : 1
n_inf = 0.5*(1 + tanh((V - V_3)/V_4)) : 1
lambda_n = lambda_n__max*cosh((V - V_3)/(2*V_4)) : Hz
I : amp
'''

neuron = NeuronGroup(17, eqs, method='exponential_euler')
neuron.I = (np.arange(17)*25+100)*uA
neuron.V = V_L
neuron.n = 'n_inf'
mon = StateMonitor(neuron, ['V', 'n'], record=True)

run_time = 220*ms
run(run_time)
