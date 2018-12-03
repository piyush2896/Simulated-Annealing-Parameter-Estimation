# Parameter Estimation of SRGM using Simulated Annealing
Software Reliability Growth Model (SRGM) is a way to generate a mapping of number of days of a software to its failure frequency. 

**Model Used: Goel-Okumoto (G-O) model **

![Goel-Okumoto Model](https://latex.codecogs.com/gif.latex?$$&space;\mu(x)&space;=&space;a(1&space;-&space;e&space;^{-bt})&space;$$)

where,<br/>
![MU](https://latex.codecogs.com/gif.latex?$\mu(x)&space;=&space;\text{current&space;predicted&space;defects,&space;using&space;Goel&space;–&space;Okumoto&space;Model.}$)<br/>
![a](https://latex.codecogs.com/gif.latex?$a&space;=&space;\text{Determines&space;scale&space;of&space;values}$)<br/>
![b](https://latex.codecogs.com/gif.latex?$b&space;=&space;\text{Determines&space;shape&space;of&space;mean&space;value&space;function}$)

## Usage 
Run [simulated_annealing.py](https://github.com/piyush2896/Simulated-Annealing-Parameter-Estimation/blob/master/simulated_annealing.py) to see the output

## Results
![Results of Parameter Estimations on Different Datasets](/all_datasets.png)
