# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **1. s**

**NeuronGroup(s) defined:**
- Name **ears**, with                population size **2**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma_{ear}.\xi.\left(\frac{1}{\tau_{ear}}\right)^{0.5} + \frac{- x + {sound}{\left(- delay + t \right)}}{\tau_{ear}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad and unless refractory as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} \theta">&#8592;<img src="https://render.githubusercontent.com/render/math?math=angular_{speed}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\theta"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=delay">&#8592;<img src="https://render.githubusercontent.com/render/math?math=distance.\sin{\left(\theta \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=delay"> is s

	Parameter <img src="https://render.githubusercontent.com/render/math?math=distance">, where unit of <img src="https://render.githubusercontent.com/render/math?math=distance"> is s

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=x \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=x">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">, with refractory <img src="https://render.githubusercontent.com/render/math?math=2.5 ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{ear}">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">, <img src="https://render.githubusercontent.com/render/math?math=angular_{speed}">: <img src="https://render.githubusercontent.com/render/math?math=6.28318531 Hz">, <img src="https://render.githubusercontent.com/render/math?math=\sigma_{ear}">: <img src="https://render.githubusercontent.com/render/math?math=0.1">, <img src="https://render.githubusercontent.com/render/math?math=sound"> of type timedarray with dimentsion <img src="https://render.githubusercontent.com/render/math?math=1"> and dt as <img src="https://render.githubusercontent.com/render/math?math=2.e-05 s">

- Name **neurons**, with                population size **30**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=1.4142135623731.\sigma.\xi.\left(\frac{1}{\tau}\right)^{0.5} - \frac{v}{\tau}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt 1">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=\sigma">: <img src="https://render.githubusercontent.com/render/math?math=0.1">, <img src="https://render.githubusercontent.com/render/math?math=\tau">: <img src="https://render.githubusercontent.com/render/math?math=1. ms">


**Synapses defined:**
- 	From ears to neurons

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=v">+=<img src="https://render.githubusercontent.com/render/math?math=0.5"> is executed


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=delay"> of ears for all members with time step <img src="https://render.githubusercontent.com/render/math?math=20. us">.


**SpikeMonitor(s)defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=t">,<img src="https://render.githubusercontent.com/render/math?math=i"> of neurons. for all members with time step <img src="https://render.githubusercontent.com/render/math?math=20. us"> when event **spike** is triggered.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=distance"> of ears initialized with <img src="https://render.githubusercontent.com/render/math?math=[-0.33333333  0.33333333] ms"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=delay"> of synapses_pre initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.1.j.max_{delay}}{num_{neurons} - 1}"> on condition i==0. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=max_{delay}">: <img src="https://render.githubusercontent.com/render/math?math=0.66666667 ms">, <img src="https://render.githubusercontent.com/render/math?math=num_{neurons}">: <img src="https://render.githubusercontent.com/render/math?math=30">



- Variable <img src="https://render.githubusercontent.com/render/math?math=delay"> of synapses_pre initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.1.max_{delay}.\left(- 1.0.j + 1.0.num_{neurons} - 1.0\right)}{num_{neurons} - 1}"> on condition i==1. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=max_{delay}">: <img src="https://render.githubusercontent.com/render/math?math=0.66666667 ms">, <img src="https://render.githubusercontent.com/render/math?math=num_{neurons}">: <img src="https://render.githubusercontent.com/render/math?math=30">




**Synaptic Connection(s) defined:**
- Connection from ears to neurons

