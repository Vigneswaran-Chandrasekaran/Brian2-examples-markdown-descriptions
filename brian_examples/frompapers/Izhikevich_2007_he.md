# Network details
The Network consists of **2**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **3. s**

**Synapses defined:**
- 	From neurongroup to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} d">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{d}{taud}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=d"> is rad and clock-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} c">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{c}{tauc}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=c"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=mode">, where unit of <img src="https://render.githubusercontent.com/render/math?math=mode"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{c.d.mode}{taus}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s"> is rad and clock-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apost">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apost}{taupost}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apost"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apre">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apre}{taupre}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apre"> is rad and event-driven as flag(s) associated

	euler method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=s">, <img src="https://render.githubusercontent.com/render/math?math=Apre">+=<img src="https://render.githubusercontent.com/render/math?math=dApre">, <img src="https://render.githubusercontent.com/render/math?math=c">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apost.mode + c,- gmax,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=s">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apost.\left(1 - mode\right) + s,- gmax,gmax \right)}">,  is executed

	On **post** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apost">+=<img src="https://render.githubusercontent.com/render/math?math=dApost">, <img src="https://render.githubusercontent.com/render/math?math=c">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.mode + c,- gmax,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=s">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.\left(1 - mode\right) + s,- gmax,gmax \right)}">,  is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taud">: <img src="https://render.githubusercontent.com/render/math?math=200. ms">, <img src="https://render.githubusercontent.com/render/math?math=taus">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=taupost">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=dApre">: <img src="https://render.githubusercontent.com/render/math?math=0.0001">, <img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=0.01">, <img src="https://render.githubusercontent.com/render/math?math=taupre">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=tauc">: <img src="https://render.githubusercontent.com/render/math?math=1. s">, <img src="https://render.githubusercontent.com/render/math?math=dApost">: <img src="https://render.githubusercontent.com/render/math?math=-0.000105">

- 	From spikegeneratorgroup to neurongroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=s">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s"> is V

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=s"> is executed

- 	From spikegeneratorgroup_1 to synapses_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=d_{post}">+=<img src="https://render.githubusercontent.com/render/math?math=\epsilon_{dopa}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\epsilon_{dopa}">: <img src="https://render.githubusercontent.com/render/math?math=0.005">


**SpikeGeneratorGroup(s) defined:**
- 	Name **spikegeneratorgroup\_1**, with population size **1**, has neuron(s) 0, 0, 0 that spike at times 3.52, 4.0200000000000005, 4.5200000000000005, with period 0. s.

- 	Name **spikegeneratorgroup**, with population size **2**, has neuron(s) 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0 that spike at times 0.5, 0.55, 1.0, 1.01, 1.5, 1.51, 3.5, 3.5500000000000003, 4.0, 4.01, 4.5, 4.51, with period 0. s.


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=s">,<img src="https://render.githubusercontent.com/render/math?math=c">,<img src="https://render.githubusercontent.com/render/math?math=d"> of synapses_1, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge.\left(Ee - vr\right) - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=vr">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=Ee">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=vr">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=vt">: <img src="https://render.githubusercontent.com/render/math?math=-54. mV">, <img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-74. mV">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of spikegeneratorgroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-60. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=s"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=100. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=mode"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=s"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1.e-10"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=c"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1.e-10"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=d"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=mode"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 


**Synaptic Connection(s) defined:**
- Connection from spikegeneratorgroup to neurongroup. From source group indices: 0, 1 to target group indices: 0, 1

- Connection from neurongroup to neurongroup. From source group indices: 0 to target group indices: 1

- Connection from spikegeneratorgroup_1 to synapses_1

### Run 2 details
Duration of simulation is **3. s**

**Synapses defined:**
- 	From neurongroup to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} d">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{d}{taud}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=d"> is rad and clock-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} c">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{c}{tauc}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=c"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=mode">, where unit of <img src="https://render.githubusercontent.com/render/math?math=mode"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{c.d.mode}{taus}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s"> is rad and clock-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apost">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apost}{taupost}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apost"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apre">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apre}{taupre}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apre"> is rad and event-driven as flag(s) associated

	euler method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=s">, <img src="https://render.githubusercontent.com/render/math?math=Apre">+=<img src="https://render.githubusercontent.com/render/math?math=dApre">, <img src="https://render.githubusercontent.com/render/math?math=c">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apost.mode + c,- gmax,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=s">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apost.\left(1 - mode\right) + s,- gmax,gmax \right)}">,  is executed

	On **post** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apost">+=<img src="https://render.githubusercontent.com/render/math?math=dApost">, <img src="https://render.githubusercontent.com/render/math?math=c">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.mode + c,- gmax,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=s">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.\left(1 - mode\right) + s,- gmax,gmax \right)}">,  is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taud">: <img src="https://render.githubusercontent.com/render/math?math=200. ms">, <img src="https://render.githubusercontent.com/render/math?math=taus">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=taupost">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=dApre">: <img src="https://render.githubusercontent.com/render/math?math=0.0001">, <img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=0.01">, <img src="https://render.githubusercontent.com/render/math?math=taupre">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=tauc">: <img src="https://render.githubusercontent.com/render/math?math=1. s">, <img src="https://render.githubusercontent.com/render/math?math=dApost">: <img src="https://render.githubusercontent.com/render/math?math=-0.000105">

- 	From spikegeneratorgroup to neurongroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=s">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s"> is V

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=s"> is executed

- 	From spikegeneratorgroup_1 to synapses_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=d_{post}">+=<img src="https://render.githubusercontent.com/render/math?math=\epsilon_{dopa}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\epsilon_{dopa}">: <img src="https://render.githubusercontent.com/render/math?math=0.005">


**SpikeGeneratorGroup(s) defined:**
- 	Name **spikegeneratorgroup\_1**, with population size **1**, has neuron(s) 0, 0, 0 that spike at times 3.52, 4.0200000000000005, 4.5200000000000005, with period 0. s.

- 	Name **spikegeneratorgroup**, with population size **2**, has neuron(s) 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0 that spike at times 0.5, 0.55, 1.0, 1.01, 1.5, 1.51, 3.5, 3.5500000000000003, 4.0, 4.01, 4.5, 4.51, with period 0. s.


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=s">,<img src="https://render.githubusercontent.com/render/math?math=c">,<img src="https://render.githubusercontent.com/render/math?math=d"> of synapses_1, for member(s): 0 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge.\left(Ee - vr\right) - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=vr">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=Ee">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=vr">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=vt">: <img src="https://render.githubusercontent.com/render/math?math=-54. mV">, <img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-74. mV">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of spikegeneratorgroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=mode"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 

