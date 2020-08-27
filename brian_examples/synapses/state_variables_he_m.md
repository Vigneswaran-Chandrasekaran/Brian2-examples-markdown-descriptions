# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. ms**

**Synapses defined:**
- 	From neurongroup to neurongroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is V

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=w"> is executed


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **100**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=v">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt - 50.mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=mV.\left(0.25.{randn}{\left(- \right)} + \sin{\left(\frac{2.\pi.i}{N} \right)} - 70\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N">: <img src="https://render.githubusercontent.com/render/math?math=100">



- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of synapses initialized with <img src="https://render.githubusercontent.com/render/math?math=mV.e^{- \frac{\left(i - j\right)^{2}}{space_{constant}}}"> on condition i > j. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=space_{constant}">: <img src="https://render.githubusercontent.com/render/math?math=200.0">




**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup

