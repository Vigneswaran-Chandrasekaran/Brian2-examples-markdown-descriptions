# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **10. ms**

**Synapses defined:**
- 	From neurongroup to neurongroup

- 	From neurongroup to neurongroup


**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **400**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is m

	Parameter <img src="https://render.githubusercontent.com/render/math?math=y">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is m


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.grid_{dist}.rows + grid_{dist}.\left\lfloor{\frac{i}{rows}}\right\rfloor"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=rows">: <img src="https://render.githubusercontent.com/render/math?math=20">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=25. um">



- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=- 0.5.cols.grid_{dist} + \left(grid_{dist}.\left(i\bmod{rows}\right)\right)"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=rows">: <img src="https://render.githubusercontent.com/render/math?math=20">, <img src="https://render.githubusercontent.com/render/math?math=grid_{dist}">: <img src="https://render.githubusercontent.com/render/math?math=25. um">, <img src="https://render.githubusercontent.com/render/math?math=cols">: <img src="https://render.githubusercontent.com/render/math?math=20">




**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=\sqrt{\left(\left(- x_{post} + x_{pre}\right)^{2} + \left(- y_{post} + y_{pre}\right)^{2} \right)} \lt distance">. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=distance">: <img src="https://render.githubusercontent.com/render/math?math=120. um">



- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=i \neq j">, with probabilty <img src="https://render.githubusercontent.com/render/math?math=1.5.e^{\frac{- \left(- x_{post} + x_{pre}\right)^{2} - \left(- y_{post} + y_{pre}\right)^{2}}{7200.umeter^{2}}}">

