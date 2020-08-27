# Network details
The Network consists of **1**                            simulation run
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **4. ks**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **50**.

	**Dynamics:**

	<img src="https://render.githubusercontent.com/render/math?math=\tau_{h}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{1}{O_{2}.\left(C + Q_{2}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\tau_{h}"> is s

	<img src="https://render.githubusercontent.com/render/math?math=J_{3K}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{4}.I.O_{3K}}{\left(C^{4} + K_{D}^{4}\right).\left(I + K_{3K}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{3K}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} C">&#8592;<img src="https://render.githubusercontent.com/render/math?math=J_{l} - J_{p} + J_{r}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=C"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{p}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{P}}{C^{2} + K_{P}^{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{p}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{l}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{l}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=Q_{2}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{d_{2}.\left(I + d_{1}\right)}{I + d_{3}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=Q_{2}"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=J_{r}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}.h^{3}.m_{inf}^{3}.\left(- C.\left(\rho_{A} + 1\right) + C_{T}\right)">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{r}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} h">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{- h + h_{inf}}{\tau_{h}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=\frac{d}{d t} I">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- J_{3K} - J_{5P} + J_{coupling} + J_{\delta} + J_{ex}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I"> is mM

	<img src="https://render.githubusercontent.com/render/math?math=m_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C.I}{\left(C + d_{5}\right).\left(I + d_{1}\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=m_{inf}"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=stimulus">&#8592;<img src="https://render.githubusercontent.com/render/math?math={int_{}}{\left(t\bmod{50.second} \lt 20.second \right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=stimulus"> is rad

	<img src="https://render.githubusercontent.com/render/math?math=J_{5P}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I.\Omega_{5P}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{5P}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=\delta_{I bias}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I - I_{bias}.stimulus">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\delta_{I bias}"> is mM

	Parameter <img src="https://render.githubusercontent.com/render/math?math=I_{bias}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=I_{bias}"> is mM and constant as flag(s) associated

	Parameter <img src="https://render.githubusercontent.com/render/math?math=J_{coupling}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{coupling}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{ex}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=- \frac{F_{ex}.\left(\tanh{\left(\frac{- I_{\Theta} + \left|{\delta_{I bias}}\right|}{\omega_{I}} \right)} + 1\right).{sign}{\left(\delta_{I bias} \right)}}{2}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{ex}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=J_{\delta}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{C^{2}.O_{\delta}}{\left(C^{2} + K_{\delta}^{2}\right).\left(\frac{I}{\kappa_{\delta}} + 1\right)}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=J_{\delta}"> is mM/s

	<img src="https://render.githubusercontent.com/render/math?math=h_{inf}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=\frac{Q_{2}}{C + Q_{2}}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=h_{inf}"> is rad

	rk4 method is used for integration

	**Properties:**

	<img src="https://render.githubusercontent.com/render/math?math=C_{T}">: <img src="https://render.githubusercontent.com/render/math?math=2. uM">, <img src="https://render.githubusercontent.com/render/math?math=K_{P}">: <img src="https://render.githubusercontent.com/render/math?math=50. nM">, <img src="https://render.githubusercontent.com/render/math?math=\kappa_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=1.5 uM">, <img src="https://render.githubusercontent.com/render/math?math=d_{1}">: <img src="https://render.githubusercontent.com/render/math?math=130. nM">, <img src="https://render.githubusercontent.com/render/math?math=d_{5}">: <img src="https://render.githubusercontent.com/render/math?math=80. nM">, <img src="https://render.githubusercontent.com/render/math?math=O_{P}">: <img src="https://render.githubusercontent.com/render/math?math=0.0009 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=\omega_{I}">: <img src="https://render.githubusercontent.com/render/math?math=50. nM">, <img src="https://render.githubusercontent.com/render/math?math=d_{2}">: <img src="https://render.githubusercontent.com/render/math?math=1.05 uM">, <img src="https://render.githubusercontent.com/render/math?math=F_{ex}">: <img src="https://render.githubusercontent.com/render/math?math=9.e-05 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=K_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=100. nM">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{5P}">: <img src="https://render.githubusercontent.com/render/math?math=50. mHz">, <img src="https://render.githubusercontent.com/render/math?math=K_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=1. uM">, <img src="https://render.githubusercontent.com/render/math?math=O_{2}">: <img src="https://render.githubusercontent.com/render/math?math=200. m^3 s^-1 mol^-1">, <img src="https://render.githubusercontent.com/render/math?math=O_{\delta}">: <img src="https://render.githubusercontent.com/render/math?math=0.0006 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=d_{3}">: <img src="https://render.githubusercontent.com/render/math?math=0.9434 uM">, <img src="https://render.githubusercontent.com/render/math?math=I_{\Theta}">: <img src="https://render.githubusercontent.com/render/math?math=300. nM">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{C}">: <img src="https://render.githubusercontent.com/render/math?math=6. Hz">, <img src="https://render.githubusercontent.com/render/math?math=K_{D}">: <img src="https://render.githubusercontent.com/render/math?math=0.7 uM">, <img src="https://render.githubusercontent.com/render/math?math=\rho_{A}">: <img src="https://render.githubusercontent.com/render/math?math=0.18">, <img src="https://render.githubusercontent.com/render/math?math=O_{3K}">: <img src="https://render.githubusercontent.com/render/math?math=0.0045 mM/s">, <img src="https://render.githubusercontent.com/render/math?math=\Omega_{L}">: <img src="https://render.githubusercontent.com/render/math?math=100. mHz">


**Synapses defined:**
- 	From neurongroup to neurongroup

	**Dynamics:**

		<img src="https://render.githubusercontent.com/render/math?math=\delta_{I}">&#8592;<img src="https://render.githubusercontent.com/render/math?math=I_{post} - I_{pre}">, where unit of <img src="https://render.githubusercontent.com/render/math?math=\delta_{I}"> is mM

	**Summed variables: **

	Updates target group neurongroup with statement: <img src="https://render.githubusercontent.com/render/math?math=- \frac{F.\left(\tanh{\left(\frac{- I_{\Theta} + \left|{\delta_{I}}\right|}{\omega_{I}} \right)} + 1\right).{sign}{\left(\delta_{I} \right)}}{2}">


**StateMonitor(s) defined:**
- 	Monitors variable(s): <img src="https://render.githubusercontent.com/render/math?math=C"> of neurongroup for all members with time step <img src="https://render.githubusercontent.com/render/math?math=50. ms">.


**Initializer(s) defined:**
- Variable <img src="https://render.githubusercontent.com/render/math?math=I_{bias}"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=1. uM"> to member(s) 25

- Variable <img src="https://render.githubusercontent.com/render/math?math=h"> of neurongroup initialized with <img src="https://render.githubusercontent.com/render/math?math=0.9"> to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup to neurongroup with condition <img src="https://render.githubusercontent.com/render/math?math=j = \left(i - 1\right)\bmod{N_{pre}} \vee j = \left(i + 1\right)\bmod{N_{pre}}">. Identifier(s) associated: 	<img src="https://render.githubusercontent.com/render/math?math=N_{pre}">: <img src="https://render.githubusercontent.com/render/math?math=50">



