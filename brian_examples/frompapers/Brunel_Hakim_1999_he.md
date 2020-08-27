# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **100. ms**

**PopulationRateMonitor(s) defined:**
- 	Monitors the population of neurongroup, with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">


**Synapses defined:**
- 	From neurongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=V">+=<img src="https://render.githubusercontent.com/render/math?math=- J"> is executed, with synaptic delay of <img src="https://render.githubusercontent.com/render/math?math=2. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=J">: <img src="https://render.githubusercontent.com/render/math?math=100. uV">


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **5000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} V">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- V + muext + sigmaext.\xi.\sqrt{\left(\tau \right)}}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=V"> is V

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=V \gt \theta">, <img src="https://render.githubusercontent.com/render/math?math=V">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, with refractory <img src="https://render.githubusercontent.com/render/math?math=2. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\theta">: <img src="https://render.githubusercontent.com/render/math?math=20. mV">, <img src="https://render.githubusercontent.com/render/math?math=sigmaext">: <img src="https://render.githubusercontent.com/render/math?math=1. mV">, <img src="https://render.githubusercontent.com/render/math?math=muext">: <img src="https://render.githubusercontent.com/render/math?math=25. mV">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=10. mV">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=V"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=10. mV"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.2">

