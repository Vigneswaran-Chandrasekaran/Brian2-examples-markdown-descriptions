# Network details
The Network consists of **2**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **10000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{gaba}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{gaba}}{\tau_{gaba}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}"> is S

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{bgcurrent - g_{ampa}.v - g_{gaba}.\left(- er + v\right) - gl.\left(- el + v\right)}{memc}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{ampa}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{ampa}}{\tau_{ampa}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{ampa}"> is S

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=el">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=10. nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{ampa}">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=vt">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{gaba}">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=memc">: <img src="https://render.githubusercontent.com/render/math?math=200. pF">, <img src="https://render.githubusercontent.com/render/math?math=bgcurrent">: <img src="https://render.githubusercontent.com/render/math?math=200. pA">, <img src="https://render.githubusercontent.com/render/math?math=el">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=er">: <img src="https://render.githubusercontent.com/render/math?math=-80. mV">


**Synapses defined:**
- 	From neurongroup_subgroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=g_{ampa}">+=<img src="https://render.githubusercontent.com/render/math?math=0.3.nS"> is executed

- 	From neurongroup_subgroup_1 to neurongroup_subgroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apre">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apre}{\tau_{stdp}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apre"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apost">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apost}{\tau_{stdp}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apost"> is rad and event-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apre">+=<img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(\eta.\left(Apost - \alpha\right) + w,0,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}">+=<img src="https://render.githubusercontent.com/render/math?math=nS.w"> is executed

	On **post** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apost">+=<img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.\eta + w,0,gmax \right)}">,  is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{stdp}">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=100">, <img src="https://render.githubusercontent.com/render/math?math=\eta">: <img src="https://render.githubusercontent.com/render/math?math=0">, <img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.12">

- 	From neurongroup_subgroup_1 to neurongroup_subgroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}">+=<img src="https://render.githubusercontent.com/render/math?math=3.nS"> is executed


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_subgroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses_2 initialized with <img src="https://render.githubusercontent.com/render/math?math=1.e-10"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup_subgroup to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

- Connection from neurongroup_subgroup_1 to neurongroup_subgroup_1, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

- Connection from neurongroup_subgroup_1 to neurongroup_subgroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

### Run 2 details
Duration of simulation is **9. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **10000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{gaba}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{gaba}}{\tau_{gaba}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}"> is S

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{bgcurrent - g_{ampa}.v - g_{gaba}.\left(- er + v\right) - gl.\left(- el + v\right)}{memc}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} g_{ampa}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{g_{ampa}}{\tau_{ampa}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=g_{ampa}"> is S

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=el">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=gl">: <img src="https://render.githubusercontent.com/render/math?math=10. nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{ampa}">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=vt">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{gaba}">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=memc">: <img src="https://render.githubusercontent.com/render/math?math=200. pF">, <img src="https://render.githubusercontent.com/render/math?math=bgcurrent">: <img src="https://render.githubusercontent.com/render/math?math=200. pA">, <img src="https://render.githubusercontent.com/render/math?math=el">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=er">: <img src="https://render.githubusercontent.com/render/math?math=-80. mV">


**Synapses defined:**
- 	From neurongroup_subgroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=g_{ampa}">+=<img src="https://render.githubusercontent.com/render/math?math=0.3.nS"> is executed

- 	From neurongroup_subgroup_1 to neurongroup_subgroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apre">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apre}{\tau_{stdp}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apre"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apost">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apost}{\tau_{stdp}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apost"> is rad and event-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apre">+=<img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(\eta.\left(Apost - \alpha\right) + w,0,gmax \right)}">, <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}">+=<img src="https://render.githubusercontent.com/render/math?math=nS.w"> is executed

	On **post** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apost">+=<img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre.\eta + w,0,gmax \right)}">,  is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{stdp}">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=100">, <img src="https://render.githubusercontent.com/render/math?math=\eta">: <img src="https://render.githubusercontent.com/render/math?math=0.01">, <img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.12">

- 	From neurongroup_subgroup_1 to neurongroup_subgroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=g_{gaba}">+=<img src="https://render.githubusercontent.com/render/math?math=3.nS"> is executed


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_subgroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


