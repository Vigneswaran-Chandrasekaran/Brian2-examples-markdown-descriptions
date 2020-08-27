# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **4. s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_7. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_1_subgroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_4. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_5. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_6. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_3. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.

- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup_subgroup_2. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **800**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=I_{NMDA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{g_{NMDA E}.s_{NMDA tot}.\left(- V_{E} + v\right)}{0.280112044817927.Mg_{2}.e^{- \frac{0.062.v}{mV}} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{NMDA rec}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{AMPA rec E}.s_{AMPA}.\left(- V_{E} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{AMPA rec}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{GABA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{GABA}}{\tau_{GABA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{GABA}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=I_{syn}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext} + I_{AMPA rec} + I_{GABA rec} + I_{NMDA rec}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{syn}"> is A

	Parameter <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA tot}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA tot}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{AMPA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{AMPA}}{\tau_{AMPA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- I_{syn} - g_{m E}.\left(- V_{L} + v\right)}{C_{m E}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{AMPA ext E}.s_{AMPA ext}.\left(- V_{E} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{AMPA ext}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{AMPA ext}}{\tau_{AMPA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=I_{GABA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{GABA E}.s_{GABA}.\left(- V_{I} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{GABA rec}"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt V_{thr}">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=V_{reset}">, with refractory <img src="https://render.githubusercontent.com/render/math?math=2. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=g_{GABA E}">: <img src="https://render.githubusercontent.com/render/math?math=1.25 nS">, <img src="https://render.githubusercontent.com/render/math?math=V_{E}">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=g_{NMDA E}">: <img src="https://render.githubusercontent.com/render/math?math=0.327 nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{GABA}">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=g_{m E}">: <img src="https://render.githubusercontent.com/render/math?math=25. nS">, <img src="https://render.githubusercontent.com/render/math?math=Mg_{2}">: <img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=g_{AMPA ext E}">: <img src="https://render.githubusercontent.com/render/math?math=2.08 nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{AMPA}">: <img src="https://render.githubusercontent.com/render/math?math=2. ms">, <img src="https://render.githubusercontent.com/render/math?math=V_{thr}">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{L}">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{AMPA rec E}">: <img src="https://render.githubusercontent.com/render/math?math=104. pS">, <img src="https://render.githubusercontent.com/render/math?math=V_{reset}">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=C_{m E}">: <img src="https://render.githubusercontent.com/render/math?math=0.5 nF">, <img src="https://render.githubusercontent.com/render/math?math=V_{I}">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">

- Name **neurongroup\_1**, with                population size **200**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=I_{NMDA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{g_{NMDA I}.s_{NMDA tot}.\left(- V_{E} + v\right)}{0.280112044817927.Mg_{2}.e^{- \frac{0.062.v}{mV}} + 1}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{NMDA rec}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{AMPA rec I}.s_{AMPA}.\left(- V_{E} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{AMPA rec}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{GABA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{GABA}}{\tau_{GABA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{GABA}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=I_{syn}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext} + I_{AMPA rec} + I_{GABA rec} + I_{NMDA rec}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{syn}"> is A

	Parameter <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA tot}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA tot}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{AMPA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{AMPA}}{\tau_{AMPA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- I_{syn} - g_{m I}.\left(- V_{L} + v\right)}{C_{m I}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{AMPA ext I}.s_{AMPA ext}.\left(- V_{E} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{AMPA ext}"> is A

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{AMPA ext}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{s_{AMPA ext}}{\tau_{AMPA}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=I_{GABA rec}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=g_{GABA I}.s_{GABA}.\left(- V_{I} + v\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{GABA rec}"> is A

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt V_{thr}">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=V_{reset}">, with refractory <img src="https://render.githubusercontent.com/render/math?math=1. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=V_{E}">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=g_{m I}">: <img src="https://render.githubusercontent.com/render/math?math=20. nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{GABA}">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=C_{m I}">: <img src="https://render.githubusercontent.com/render/math?math=200. pF">, <img src="https://render.githubusercontent.com/render/math?math=g_{AMPA rec I}">: <img src="https://render.githubusercontent.com/render/math?math=81. pS">, <img src="https://render.githubusercontent.com/render/math?math=Mg_{2}">: <img src="https://render.githubusercontent.com/render/math?math=1.0">, <img src="https://render.githubusercontent.com/render/math?math=V_{thr}">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{AMPA ext I}">: <img src="https://render.githubusercontent.com/render/math?math=1.62 nS">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{AMPA}">: <img src="https://render.githubusercontent.com/render/math?math=2. ms">, <img src="https://render.githubusercontent.com/render/math?math=V_{L}">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{GABA I}">: <img src="https://render.githubusercontent.com/render/math?math=0.973 nS">, <img src="https://render.githubusercontent.com/render/math?math=V_{reset}">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=V_{I}">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=g_{NMDA I}">: <img src="https://render.githubusercontent.com/render/math?math=258. pS">


**PopulationRateMonitor(s) defined:**
- 	Monitors the population of neurongroup_1, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_8, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_13, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_12, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_11, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_10, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">

- 	Monitors the population of neurongroup_subgroup_9, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">


**Synapses defined:**
- 	From neurongroup to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{x}{\tau_{NMDA rise}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{NMDA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\alpha.x.\left(1 - s_{NMDA}\right) - \frac{s_{NMDA}}{\tau_{NMDA decay}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA}"> is rad and clock-driven as flag(s) associated

	euler method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA}">+=<img src="https://render.githubusercontent.com/render/math?math=w">, <img src="https://render.githubusercontent.com/render/math?math=x">+=<img src="https://render.githubusercontent.com/render/math?math=1">,  is executed

	**Summed variables: **

	Updates target group neurongroup with statement: <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA}.w">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{NMDA decay}">: <img src="https://render.githubusercontent.com/render/math?math=100. ms">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{NMDA rise}">: <img src="https://render.githubusercontent.com/render/math?math=2. ms">, <img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.5 kHz">

- 	From neurongroup to neurongroup_1

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{x}{\tau_{NMDA rise}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and clock-driven as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} s_{NMDA}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\alpha.x.\left(1 - s_{NMDA}\right) - \frac{s_{NMDA}}{\tau_{NMDA decay}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA}"> is rad and clock-driven as flag(s) associated

	euler method is used for integration

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA}">+=<img src="https://render.githubusercontent.com/render/math?math=w">, <img src="https://render.githubusercontent.com/render/math?math=x">+=<img src="https://render.githubusercontent.com/render/math?math=1">,  is executed

	**Summed variables: **

	Updates target group neurongroup_1 with statement: <img src="https://render.githubusercontent.com/render/math?math=s_{NMDA}.w">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{NMDA decay}">: <img src="https://render.githubusercontent.com/render/math?math=100. ms">, <img src="https://render.githubusercontent.com/render/math?math=\tau_{NMDA rise}">: <img src="https://render.githubusercontent.com/render/math?math=2. ms">, <img src="https://render.githubusercontent.com/render/math?math=\alpha">: <img src="https://render.githubusercontent.com/render/math?math=0.5 kHz">

- 	From neurongroup_1 to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=s_{GABA}">+=<img src="https://render.githubusercontent.com/render/math?math=1">,  is executed

- 	From neurongroup_1 to neurongroup_1

	**Pathways:**

	On **pre** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=s_{GABA}">+=<img src="https://render.githubusercontent.com/render/math?math=1">,  is executed


**PoissonInput(s)defined:**
- 	PoissonInput with size **80** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=25. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math={stimuli_{1}}{\left(t \right)}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=stimuli_{1}"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=0.025 s">

- 	PoissonInput with size **800** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=3. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=1">

- 	PoissonInput with size **800** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=3. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=1">

- 	PoissonInput with size **800** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=25. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math={stimuli_{reset}}{\left(t \right)}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=stimuli_{reset}"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=0.025 s">

- 	PoissonInput with size **80** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=25. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math={stimuli_{2}}{\left(t \right)}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=stimuli_{2}"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=0.025 s">

- 	PoissonInput with size **800** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=s_{AMPA ext}"> with rate <img src="https://render.githubusercontent.com/render/math?math=25. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math={stimuli_{reset}}{\left(t \right)}">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=stimuli_{reset}"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=0.025 s">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-70. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=-70. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=1."> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=i \neq j">

- Connection from neurongroup to neurongroup_1

- Connection from neurongroup_1 to neurongroup_1 with condition <img src="https://render.githubusercontent.com/render/math?math=i \neq j">

- Connection from neurongroup_1 to neurongroup

