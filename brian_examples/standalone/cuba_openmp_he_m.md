# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Synapses defined:**
- 	From neurongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=we"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=we">: <img src="https://render.githubusercontent.com/render/math?math=1.62 mV">

- 	From neurongroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=gi">+=<img src="https://render.githubusercontent.com/render/math?math=wi"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=wi">: <img src="https://render.githubusercontent.com/render/math?math=-9. mV">


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **4000**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} gi">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{gi}{taui}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=gi"> is V and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge + gi - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V and unless refractory as flag(s) associated

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt Vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Vr">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vt">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=taui">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-49. mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=Vr + \left(- Vr + Vt\right).{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=Vr">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=Vt">: <img src="https://render.githubusercontent.com/render/math?math=-50. mV">



- Variable <img src="https://render.githubusercontent.com/render/math?math=ge"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0. V"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=gi"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0. V"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=i \lt 3200">, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=i \geq 3200">, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.02">

