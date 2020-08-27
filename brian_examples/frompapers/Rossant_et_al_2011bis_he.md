# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**PoissonInput(s)defined:**
- 	PoissonInput with size **4000** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=ge"> with rate <img src="https://render.githubusercontent.com/render/math?math=0.85 Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=1.79304785 mV">

- 	PoissonInput with size **4000** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=ge"> with rate <img src="https://render.githubusercontent.com/render/math?math=1. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=1.79304785 mV">

- 	PoissonInput with size **1** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=ge"> with rate <img src="https://render.githubusercontent.com/render/math?math=40. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=26.89571768 mV">

- 	PoissonInput with size **1000** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=gi"> with rate <img src="https://render.githubusercontent.com/render/math?math=1. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=-2.15165741 mV">

- 	PoissonInput with size **1000** gives input to variable <img src="https://render.githubusercontent.com/render/math?math=gi"> with rate <img src="https://render.githubusercontent.com/render/math?math=1. Hz"> and weight of <img src="https://render.githubusercontent.com/render/math?math=-2.15165741 mV">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge + gi - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} gi">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{gi}{taui}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=gi"> is V

	exact method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt \theta">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=El">, with refractory <img src="https://render.githubusercontent.com/render/math?math=5. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\theta">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=taui">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-65. mV">, <img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=3. ms">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=i">,<img src="https://render.githubusercontent.com/render/math?math=t"> of neurongroup. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-65. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=ge"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=gi"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0."> to all members 

