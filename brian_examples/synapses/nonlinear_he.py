
from brian2 import *
import brian2tools

set_device('heexport', build_on_run=False)
#!/usr/bin/env python
"""
NMDA synapses.
"""
from brian2 import *

a = 1 / (10*ms)
b = 1 / (10*ms)
c = 1 / (10*ms)

input = NeuronGroup(2, 'dv/dt = 1/(10*ms) : 1', threshold='v>1', reset='v = 0',
                    method='euler')
neurons = NeuronGroup(1, """dv/dt = (g-v)/(10*ms) : 1
                            g : 1""", method='exact')
S = Synapses(input, neurons, '''
                dg_syn/dt = -a*g_syn+b*x*(1-g_syn) : 1 (clock-driven)
                g_post = g_syn : 1 (summed)
                dx/dt=-c*x : 1 (clock-driven)
                w : 1 # synaptic weight
             ''', on_pre='x += w') # NMDA synapses

S.connect()
S.w = [1., 10.]
input.v = [0., 0.5]

M = StateMonitor(S, 'g',
                 # If not using standalone mode, this could also simply be
                 # record=True
                 record=np.arange(len(input)*len(neurons)))
Mn = StateMonitor(neurons, 'g', record=0)

run(1000*ms)

device.build(debug=True)
