# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **2.1 s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **3**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} y">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{c - d.x^{2} - y}{time_{unit}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is rad and constant as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{I - a.x^{3} + b.x^{2} + y - z}{time_{unit}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} z">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{r.\left(s.\left(x - x_{1}\right) - z\right)}{time_{unit}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=z"> is rad

	rk4 method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=s">: <img src="https://render.githubusercontent.com/render/math?math=4">, <img src="https://render.githubusercontent.com/render/math?math=r">: <img src="https://render.githubusercontent.com/render/math?math=0.001">, <img src="https://render.githubusercontent.com/render/math?math=time_{unit}">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=x_{1}">: <img src="https://render.githubusercontent.com/render/math?math=-1.6">, <img src="https://render.githubusercontent.com/render/math?math=c">: <img src="https://render.githubusercontent.com/render/math?math=1">, <img src="https://render.githubusercontent.com/render/math?math=b">: <img src="https://render.githubusercontent.com/render/math?math=3">, <img src="https://render.githubusercontent.com/render/math?math=d">: <img src="https://render.githubusercontent.com/render/math?math=5">, <img src="https://render.githubusercontent.com/render/math?math=a">: <img src="https://render.githubusercontent.com/render/math?math=1">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=100. us">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=-1.6"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=c - d.x^{2}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=d">: <img src="https://render.githubusercontent.com/render/math?math=5">, <img src="https://render.githubusercontent.com/render/math?math=c">: <img src="https://render.githubusercontent.com/render/math?math=1">



- Variable <img src="https://render.githubusercontent.com/render/math?math=z"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=r.s.\left(x - x_{1}\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=s">: <img src="https://render.githubusercontent.com/render/math?math=4">, <img src="https://render.githubusercontent.com/render/math?math=x_{1}">: <img src="https://render.githubusercontent.com/render/math?math=-1.6">, <img src="https://render.githubusercontent.com/render/math?math=r">: <img src="https://render.githubusercontent.com/render/math?math=0.001">



- Variable <img src="https://render.githubusercontent.com/render/math?math=I"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=[0.4 2.  4. ]"> to all members 

