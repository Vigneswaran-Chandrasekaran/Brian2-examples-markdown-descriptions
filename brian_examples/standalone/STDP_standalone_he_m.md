# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **100. s**

**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses, for member(s): 0,1 with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of poissongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Synapses defined:**
- 	From poissongroup to neurongroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apre">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apre}{taupre}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apre"> is rad and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} Apost">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{Apost}{taupost}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Apost"> is rad and event-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=w">, <img src="https://render.githubusercontent.com/render/math?math=Apre">+=<img src="https://render.githubusercontent.com/render/math?math=dApre">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apost + w,0,gmax \right)}"> is executed

	On **post** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=Apost">+=<img src="https://render.githubusercontent.com/render/math?math=dApost">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(Apre + w,0,gmax \right)}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=0.01">, <img src="https://render.githubusercontent.com/render/math?math=taupre">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">, <img src="https://render.githubusercontent.com/render/math?math=dApre">: <img src="https://render.githubusercontent.com/render/math?math=0.0001">, <img src="https://render.githubusercontent.com/render/math?math=dApost">: <img src="https://render.githubusercontent.com/render/math?math=-0.000105">, <img src="https://render.githubusercontent.com/render/math?math=taupost">: <img src="https://render.githubusercontent.com/render/math?math=20. ms">


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **1**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge.\left(Ee - v\right) - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=vr">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=Ee">: <img src="https://render.githubusercontent.com/render/math?math=0. V">, <img src="https://render.githubusercontent.com/render/math?math=vr">: <img src="https://render.githubusercontent.com/render/math?math=-60. mV">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=vt">: <img src="https://render.githubusercontent.com/render/math?math=-54. mV">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-74. mV">


**PoissonGroup(s) defined:**
- 	Name **poissongroup**, with                population size **1000** and rate as <img src="https://render.githubusercontent.com/render/math?math=15. Hz">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=rates"> of poissongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=15. Hz"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=gmax.{rand}{\left(- \right)}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=gmax">: <img src="https://render.githubusercontent.com/render/math?math=0.01">




**Synaptic Connection(s) defined:**
- Connection from poissongroup to neurongroup

