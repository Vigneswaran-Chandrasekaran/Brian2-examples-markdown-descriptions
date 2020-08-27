# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **5. s**

**NeuronGroup(s) defined:**
- Name **layer4**, with                population size **12100**.

	**Dynamics:**

	Parameter <img src="https://render.githubusercontent.com/render/math?math=stim_{start y}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=stim_{start y}"> is rad and shared as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=direction">, where unit of <img src="https://render.githubusercontent.com/render/math?math=direction"> is rad and shared as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=bar_{x}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=stim_{start x} + \frac{\left(- stim_{start time} + t\right).\cos{\left(direction \right)}}{5.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bar_{x}"> is rad and shared as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=barrel_{x}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=barrel_{x}"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=stim_{start time}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=stim_{start time}"> is s and shared as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=selectivity">, where unit of <img src="https://render.githubusercontent.com/render/math?math=selectivity"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=stim_{start x}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=stim_{start x}"> is rad and shared as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=bar_{y}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=stim_{start y} + \frac{\left(- stim_{start time} + t\right).\sin{\left(direction \right)}}{5.ms}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=bar_{y}"> is rad and shared as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=rate">&#8592;<img src="https://render.githubusercontent.com/render/math?math=Fmax.{clip}{\left(\cos{\left(direction - selectivity \right)},0,\infty \right)}.{int_{}}{\left(is_{active} \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=rate"> is Hz

	Parameter <img src="https://render.githubusercontent.com/render/math?math=barrel_{y}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=barrel_{y}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=is_{active}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\left|{\left(- bar_{x} + barrel_{x} + 0.5\right).\cos{\left(direction \right)} + \left(- bar_{y} + barrel_{y} + 0.5\right).\sin{\left(direction \right)}}\right| \lt 0.5">, where unit of <img src="https://render.githubusercontent.com/render/math?math=is_{active}"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math={rand}{\left(- \right)} \lt dt.rate">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=Fmax">: <img src="https://render.githubusercontent.com/render/math?math=100. Hz">, <img src="https://render.githubusercontent.com/render/math?math=stimradius">: <img src="https://render.githubusercontent.com/render/math?math=6.0">, <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">

	**Run regularly(s): **

	For every <img src="https://render.githubusercontent.com/render/math?math=60. ms"> code: , <img src="https://render.githubusercontent.com/render/math?math=direction">&#8592;<img src="https://render.githubusercontent.com/render/math?math=2.\pi.{rand}{\left(- \right)}">, <img src="https://render.githubusercontent.com/render/math?math=stim_{start x}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.5.barrelarraysize - stimradius.\cos{\left(direction \right)}">, <img src="https://render.githubusercontent.com/render/math?math=stim_{start y}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=0.5.barrelarraysize - stimradius.\sin{\left(direction \right)}">, <img src="https://render.githubusercontent.com/render/math?math=stim_{start time}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=t">,  will be executed

- Name **layer23**, with                population size **19225**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{El + ge + gi - v}{taum}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=v"> is V

	Parameter <img src="https://render.githubusercontent.com/render/math?math=y">, where unit of <img src="https://render.githubusercontent.com/render/math?math=y"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} ge">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{ge}{taue}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=ge"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} vt">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{Vt - vt}{tauvt}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=vt"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} gi">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{gi}{taui}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=gi"> is V

	Parameter <img src="https://render.githubusercontent.com/render/math?math=x">, where unit of <img src="https://render.githubusercontent.com/render/math?math=x"> is rad

	Parameter <img src="https://render.githubusercontent.com/render/math?math=barrel_{idx}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=barrel_{idx}"> is rad

	euler method is used for integration

	**Events:**

	Event **spike**, after <img src="https://render.githubusercontent.com/render/math?math=v \gt vt">, <img src="https://render.githubusercontent.com/render/math?math=v">&#8592;<img src="https://render.githubusercontent.com/render/math?math=El">, <img src="https://render.githubusercontent.com/render/math?math=vt">+=<img src="https://render.githubusercontent.com/render/math?math=vt_{inc}">, with refractory <img src="https://render.githubusercontent.com/render/math?math=2. ms">

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=tauvt">: <img src="https://render.githubusercontent.com/render/math?math=50. ms">, <img src="https://render.githubusercontent.com/render/math?math=taui">: <img src="https://render.githubusercontent.com/render/math?math=25. ms">, <img src="https://render.githubusercontent.com/render/math?math=vt_{inc}">: <img src="https://render.githubusercontent.com/render/math?math=2. mV">, <img src="https://render.githubusercontent.com/render/math?math=Vt">: <img src="https://render.githubusercontent.com/render/math?math=-55. mV">, <img src="https://render.githubusercontent.com/render/math?math=El">: <img src="https://render.githubusercontent.com/render/math?math=-70. mV">, <img src="https://render.githubusercontent.com/render/math?math=taue">: <img src="https://render.githubusercontent.com/render/math?math=2. ms">, <img src="https://render.githubusercontent.com/render/math?math=taum">: <img src="https://render.githubusercontent.com/render/math?math=10. ms">


**Synapses defined:**
- 	From layer4 to layer23_subgroup

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is V

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} A_{target}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{A_{target}}{taud}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=A_{target}"> is V and event-driven as flag(s) associated

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} A_{source}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{A_{source}}{taup}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=A_{source}"> is V and event-driven as flag(s) associated

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=w">, <img src="https://render.githubusercontent.com/render/math?math=A_{source}">+=<img src="https://render.githubusercontent.com/render/math?math=Ap">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(A_{target} + w,0,EPSC \right)}"> is executed

	On **post** of event spike statement(s): , <img src="https://render.githubusercontent.com/render/math?math=A_{target}">+=<img src="https://render.githubusercontent.com/render/math?math=Ad">, <img src="https://render.githubusercontent.com/render/math?math=w">&#8592;<img src="https://render.githubusercontent.com/render/math?math={clip}{\left(A_{source} + w,0,EPSC \right)}"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=taup">: <img src="https://render.githubusercontent.com/render/math?math=5. ms">, <img src="https://render.githubusercontent.com/render/math?math=Ad">: <img src="https://render.githubusercontent.com/render/math?math=-299.06975624 uV">, <img src="https://render.githubusercontent.com/render/math?math=taud">: <img src="https://render.githubusercontent.com/render/math?math=25. ms">, <img src="https://render.githubusercontent.com/render/math?math=EPSC">: <img src="https://render.githubusercontent.com/render/math?math=7.47674391 mV">, <img src="https://render.githubusercontent.com/render/math?math=Ap">: <img src="https://render.githubusercontent.com/render/math?math=0.3738372 mV">

- 	From layer23_subgroup to layer23

	**Dynamics:**

		Parameter <img src="https://render.githubusercontent.com/render/math?math=w">, where unit of <img src="https://render.githubusercontent.com/render/math?math=w"> is V

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=ge">+=<img src="https://render.githubusercontent.com/render/math?math=w"> is executed

- 	From layer23_subgroup_1 to layer23_subgroup

	**Pathways:**

	On **pre** of event spike statement(s): <img src="https://render.githubusercontent.com/render/math?math=gi">+=<img src="https://render.githubusercontent.com/render/math?math=IPSC"> is executed

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=IPSC">: <img src="https://render.githubusercontent.com/render/math?math=-1.84201575 mV">


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=barrel_{x}"> of layer4 initialized with <img src="https://render.githubusercontent.com/render/math?math=\left(\left\lfloor{\frac{i}{N_{4}}}\right\rfloor\bmod{barrelarraysize}\right) + 0.5"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">, <img src="https://render.githubusercontent.com/render/math?math=N_{4}">: <img src="https://render.githubusercontent.com/render/math?math=484">



- Variable <img src="https://render.githubusercontent.com/render/math?math=barrel_{y}"> of layer4 initialized with <img src="https://render.githubusercontent.com/render/math?math=\left\lfloor{\frac{i}{N_{4}.barrelarraysize}}\right\rfloor + 0.5"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">, <img src="https://render.githubusercontent.com/render/math?math=N_{4}">: <img src="https://render.githubusercontent.com/render/math?math=484">



- Variable <img src="https://render.githubusercontent.com/render/math?math=selectivity"> of layer4 initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{2.0.\pi.\left(i\bmod{N_{4}}\right)}{N_{4}}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{4}">: <img src="https://render.githubusercontent.com/render/math?math=484">



- Variable <img src="https://render.githubusercontent.com/render/math?math=v"> of layer23 initialized with <img src="https://render.githubusercontent.com/render/math?math=-70. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=vt"> of layer23 initialized with <img src="https://render.githubusercontent.com/render/math?math=-55. mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of layer23_subgroup initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left(i\bmod{M23exc.barrelarraysize}\right)}{M23exc}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=M23exc">: <img src="https://render.githubusercontent.com/render/math?math=25">, <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of layer23_subgroup initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left\lfloor{\frac{i}{M23exc.barrelarraysize}}\right\rfloor}{M23exc}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=M23exc">: <img src="https://render.githubusercontent.com/render/math?math=25">, <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=barrel_{idx}"> of layer23_subgroup initialized with <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize.\left\lfloor{y}\right\rfloor + \left\lfloor{x}\right\rfloor"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=x"> of layer23_subgroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left(i\bmod{M23inh.barrelarraysize}\right)}{M23inh}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=M23inh">: <img src="https://render.githubusercontent.com/render/math?math=12">, <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=y"> of layer23_subgroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=\frac{1.0.\left\lfloor{\frac{i}{M23inh.barrelarraysize}}\right\rfloor}{M23inh}"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=M23inh">: <img src="https://render.githubusercontent.com/render/math?math=12">, <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=barrel_{idx}"> of layer23_subgroup_1 initialized with <img src="https://render.githubusercontent.com/render/math?math=barrelarraysize.\left\lfloor{y}\right\rfloor + \left\lfloor{x}\right\rfloor"> to all members . Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of feedforward initialized with <img src="https://render.githubusercontent.com/render/math?math=3.73837195 mV"> to all members 

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of recurrent_exc initialized with <img src="https://render.githubusercontent.com/render/math?math=2.24302317.mvolt"> on condition j<Nbarrels*N23exc

- Variable <img src="https://render.githubusercontent.com/render/math?math=w"> of recurrent_exc initialized with <img src="https://render.githubusercontent.com/render/math?math=7.47674391.mvolt"> on condition j>=Nbarrels*N23exc


**Synaptic Connection(s) defined:**
- Connection from layer4 to layer23_subgroup with condition <img src="https://render.githubusercontent.com/render/math?math=barrel_{x pre} + barrel_{y pre}.barrelarraysize = barrel_{idx post}">, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.5">. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=barrelarraysize">: <img src="https://render.githubusercontent.com/render/math?math=5">



- Connection from layer23_subgroup to layer23, with probabilty <img src="https://render.githubusercontent.com/render/math?math=0.15.e^{- 3.125.\left(- x_{post} + x_{pre}\right)^{2} - 3.125.\left(- y_{post} + y_{pre}\right)^{2}}">

- Connection from layer23_subgroup_1 to layer23_subgroup, with probabilty <img src="https://render.githubusercontent.com/render/math?math=e^{- 12.5.\left(- x_{post} + x_{pre}\right)^{2} - 12.5.\left(- y_{post} + y_{pre}\right)^{2}}">

