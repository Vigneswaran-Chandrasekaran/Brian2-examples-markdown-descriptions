# modified line 22, 23, 24
from brian2 import *
import brian2tools

set_device('heexport', build_on_run=False)

'''
Set state variable values with a string (using code generation).
'''

from brian2 import *

G = NeuronGroup(100, 'v:volt', threshold='v>-50*mV')
G.v = '(sin(2*pi*i/N) - 70 + 0.25*randn()) * mV'
S = Synapses(G, G, 'w : volt', on_pre='v += w')
S.connect()

space_constant = 200.0
S.w['i > j'] = 'exp(-(i - j)**2/space_constant) * mV'

# Generate a matrix for display
#w_matrix = np.zeros((len(G), len(G)))
#w_matrix[S.i[:], S.j[:]] = S.w[:]
run(1*ms)
device.build(debug=True)
