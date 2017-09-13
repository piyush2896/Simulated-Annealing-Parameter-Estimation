# Parameter Estimation of SRGM using Simulated Annealing
Software Reliability Growth Model (SRGM) is a way to generate a mapping of number of days of a software to its failure frequency. 

**Model Used: Goel-Okumoto (G-O) model **

$$
\mu(x) = a(1 - e ^(-bt))
$$

where,<br/>
$\mu(x) = \text{current predicted defects, using Goel – Okumoto Model.}$<br/>
$a = \text{Determines scale of values}$<br/>
$b = \text{Determines shape of mean value function}$

## Usage 
Run [simulated_annealing.py](https://github.com/piyush2896/Simulated-Annealing-Parameter-Estimation/blob/master/simulated_annealing.py) to see the output

## Results
![Results of Parameter Estimations on Different Datasets](https://github.com/piyush2896/Simulated-Annealing-Parameter-Estimation/blob/master/all_datasets.png)