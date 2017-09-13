import numpy as np
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import seaborn as sns

def hypothesis(a, b, x):
	return a * (1 - np.exp(-b * x))

def mse_loss(a, b, x, y):
    preds = hypothesis(a, b, x)
    return np.sum((preds - y) ** 2) / x.shape[0]

def simulated_annealing(temp, cooling_rate, x, y, seed=None, start_vals=None):
    def acceptance_probability(energy, new_energy, temp):
        if new_energy < energy:
            return 1.0

        return np.exp((energy - new_energy) / temp)

    if seed:
        random.seed(seed)

    if start_vals:
        current_a, current_b = start_vals
    else:
        current_a, current_b = random.uniform(-100, 1000), random.uniform(-100, 1000)

    best_a, best_b, minimal_loss = current_a, current_b, \
                 mse_loss(current_a, current_b, x, y)

    current_loss = minimal_loss

    while temp > 1:
        a, b = random.uniform(current_a-3, current_a+3), random.uniform(current_b-3, current_b+3)
        #a, b = random.uniform(-100, 1000), random.uniform(-100, 1000)

        curr_energy = current_loss
        neigh_energy = mse_loss(a, b, x, y)

        if(acceptance_probability(curr_energy, neigh_energy, temp) > random.random()):
            current_loss = neigh_energy
            current_a, current_b = a, b

        if current_loss < minimal_loss:
            minimal_loss = current_loss
            best_a, best_b = current_a, current_b

        temp *= 1-cooling_rate

    print('-'*70)
    print('Final Loss: ', minimal_loss)
    print('Best Params: ', best_a, best_b)
    print('Cooling Rate: ', cooling_rate)
    
    return best_a, best_b


if __name__ == '__main__':
    def run_simulated_annealing(file):    
        df = pd.read_excel(file)
        x, y = np.array(df["W"]), np.array(df["CF"])
        vals = None
        a = []
        b = []
        cooling_rate = 1e-2
        for i in range(200):
            print("Run ", i+1)
            vals = simulated_annealing(1e30, cooling_rate, x, y, seed=i, 
                                       start_vals=vals)
            a.append(vals[0])
            b.append(vals[1])
            cooling_rate -= 1e-5
        result = {
            'Run': list(range(1, 201)),
            'a': a,
            'b': b
        }
        
        file_name = file.split('/')[2].split('.')[0] + '_result.xlsx'
        dest = './results/'
        
        df = pd.DataFrame.from_dict(result)
        df.to_excel(dest+file_name, index=False)
        return x, y, vals

    path = './datasets/'
    x_F, y_F, vals_FC40 = run_simulated_annealing(path+"FC40.xlsx")
    x_1, y_1, vals_DS1 = run_simulated_annealing(path+"DS1.xlsx")
    x_2, y_2, vals_DS2 = run_simulated_annealing(path+"DS2.xlsx")
    x_3, y_3, vals_DS3 = run_simulated_annealing(path+"DS3.xlsx")
    x_4, y_4, vals_DS4 = run_simulated_annealing(path+"DS4.xlsx")
    
    sns.set_style("darkgrid")
    
    plt.figure(0, figsize=(10, 6))
    plt.subplot(321)
    plt.title("FC40")
    plt.scatter(x_F, y_F, color='red')
    plt.plot(x_F, hypothesis(vals_FC40[0], vals_FC40[1], x_F), color='blue')
    plt.subplot(322)
    plt.title("DS1")
    plt.scatter(x_1, y_1, color='red')
    plt.plot(x_1, hypothesis(vals_DS1[0], vals_DS1[1], x_1), color='blue')
    plt.subplot(323)
    plt.title("DS2")
    plt.scatter(x_2, y_2, color='red')
    plt.plot(x_2, hypothesis(vals_DS2[0], vals_DS2[1], x_2), color='blue')
    plt.subplot(324)
    plt.title("DS3")
    plt.scatter(x_3, y_3, color='red')
    plt.plot(x_3, hypothesis(vals_DS3[0], vals_DS3[1], x_3), color='blue')
    plt.subplot(325)
    plt.title("DS4")
    plt.scatter(x_4, y_4, color='red')
    plt.plot(x_4, hypothesis(vals_DS4[0], vals_DS4[1], x_4), color='blue')
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=0.5)
    plt.show()