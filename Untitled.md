# Network details
The Network consists of **2**                            simulation runs
_______________________________________________________________________________
### Run 1 details
Duration of simulation is **100. s**

**NeuronGroup(s) defined:**
- Name **neurongroup**, with                population size **4000**.

	**Dynamics:**

	$\frac{d}{d t} v$&#8592;$\frac{1}{Cm} \left(- g_{kd} n^{4} \left(- EK + v\right) - g_{na} h m^{3} \left(- ENa + v\right) + ge \left(Ee - v\right) + gi \left(Ei - v\right) + gl \left(El - v\right)\right)$, where unit of $v$ is V

	$\alpha_{n}$&#8592;$\frac{0.16}{ms \operatorname{exprel}{\left(\frac{1}{5 mV} \left(VT + 15 mV - v\right) \right)}}$, where unit of $\alpha_{n}$ is Hz

	$\alpha_{h}$&#8592;$\frac{0.128}{ms} e^{\frac{1}{18 mV} \left(VT + 17 mV - v\right)}$, where unit of $\alpha_{h}$ is Hz

	$\frac{d}{d t} n$&#8592;$\alpha_{n} \left(1 - n\right) - \beta_{n} n$, where unit of $n$ is rad

	$\beta_{m}$&#8592;$\frac{1.4}{ms \operatorname{exprel}{\left(\frac{1}{5 mV} \left(- VT - 40 mV + v\right) \right)}}$, where unit of $\beta_{m}$ is Hz

	$\alpha_{m}$&#8592;$\frac{1.28}{ms \operatorname{exprel}{\left(\frac{1}{4 mV} \left(VT + 13 mV - v\right) \right)}}$, where unit of $\alpha_{m}$ is Hz

	$\beta_{n}$&#8592;$\frac{0.5}{ms} e^{\frac{1}{40 mV} \left(VT + 10 mV - v\right)}$, where unit of $\beta_{n}$ is Hz

	$\frac{d}{d t} h$&#8592;$\alpha_{h} \left(1 - h\right) - \beta_{h} h$, where unit of $h$ is rad

	$\frac{d}{d t} gi$&#8592;$- \frac{1.0}{taui} gi$, where unit of $gi$ is S

	$\frac{d}{d t} m$&#8592;$\alpha_{m} \left(1 - m\right) - \beta_{m} m$, where unit of $m$ is rad

	$\frac{d}{d t} ge$&#8592;$- \frac{1.0}{taue} ge$, where unit of $ge$ is S

	$\beta_{h}$&#8592;$\frac{4.0}{ms \left(e^{\frac{1}{5 mV} \left(VT + 40 mV - v\right)} + 1\right)}$, where unit of $\beta_{h}$ is Hz

	exponential_euler method is used for integration

	**Events:**

	Event **spike**, after $v \gt - 20 mV$, with refractory $3. ms$

	**Properties:**

	$El$: $-60. mV$, $EK$: $-90. mV$, $Cm$: $200. pF$, $VT$: $-63. mV$, $taui$: $10. ms$, $Ee$: $0. V$, $g_{kd}$: $6. uS$, $taue$: $5. ms$, $g_{na}$: $20. uS$, $gl$: $10. nS$, $Ei$: $-80. mV$, $ENa$: $50. mV$


**Synapses defined:**
- 	From neurongroup_subgroup_1 to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): $gi$+=$wi$ is executed

	**Properties:**

	$wi$: $67. nS$

- 	From neurongroup_subgroup to neurongroup

	**Pathways:**

	On **pre** of event spike statement(s): $ge$+=$we$ is executed

	**Properties:**

	$we$: $6. nS$


**Initializer(s) defined:**
- Variable $v$ of neurongroup initialized with $El + mV \left(5 \operatorname{randn}{\left(_placeholder_{arg} \right)} - 5\right)$ to all members . Identifier(s) associated: 	$El$: $-60. mV$



- Variable $ge$ of neurongroup initialized with $nS \left(15.0 \operatorname{randn}{\left(_placeholder_{arg} \right)} + 40.0\right)$ to all members 

- Variable $gi$ of neurongroup initialized with $nS \left(120.0 \operatorname{randn}{\left(_placeholder_{arg} \right)} + 200.0\right)$ to all members 


**Synaptic Connection(s) defined:**
- Connection from neurongroup_subgroup to neurongroup, with probabilty $0.02$

- Connection from neurongroup_subgroup_1 to neurongroup, with probabilty $0.02$

