# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **0.5 s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup_1. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=20. us"> when event **spike** is triggered.


**NeuronGroup(s) defined:**
- Name **neurongroup\_1**, with                population size **300**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma.\xi.\left(\frac{1}{\tau}\right)^{0.5} - \frac{v}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=0.1">

- Name **neurongroup**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=frequency">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Hz.\left(200.Hz.t + 200\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=frequency"> is Hz

	<img src="https://render.githubusercontent.com/render/math?math=sound">&#8592;<img src="https://render.githubusercontent.com/render/math?math=5.\sin^{3}{\left(2.\pi.frequency.t \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=sound"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.14142135623731.\xi.\left(\frac{1}{\tau_{ear}}\right)^{0.5} + \frac{sound - x}{\tau_{ear}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and unless refractory as flag(s) associated

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=x \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, with refractory <img src="https://render.githubusercontent.com/render/math?math=2. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{ear}">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">


**Synapses defined:**
- 	From neurongroup to neurongroup_1

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=0.5"> is executed


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=delay"> of synapses_pre initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.Hz.i.second.e^{- \frac{1.0.j.\log{\left(\frac{max_{freq}}{min_{freq}} \right)}}{num_{neurons} - 1}}}{min_{freq}}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=max_{freq}">: <img src="https://render.githubusercontent.com/render/math?math=1. kHz">, <img src="https://render.githubusercontent.com/render/math?math=num_{neurons}">: <img src="https://render.githubusercontent.com/render/math?math=300">, <img src="https://render.githubusercontent.com/render/math?math=min_{freq}">: <img src="https://render.githubusercontent.com/render/math?math=50. Hz">




**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup_1

