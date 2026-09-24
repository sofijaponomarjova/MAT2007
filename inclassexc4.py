import numpy as np

def population_growth(N, R, t):
    return N*np.exp(R*t)

def task1():
    initial_population=100
    time=24
    population_size=100

    population_A=np.zeros(population_size)
    population_B=np.zeros(population_size)
    for i in range (population_size):
        population_A[i]=population_growth(initial_population, np.random.normal(0.3, 0.05), time)
        population_B[i]=population_growth(initial_population, np.random.normal(0.32, 0.04), time)

    subsamples_A=np.split(population_A, 10)
    subsamples_B=np.split(population_B, 10)
    means_A=[]
    means_B=[]
    for index, value in enumerate(subsamples_A):
        means_A.append(value.mean())
    A_mean=np.average(means_A)
    for index, value in enumerate(subsamples_B):
        means_B.append(value.mean())
    B_mean=np.average(means_B)
    uncertainty_A=np.std(means_A)
    uncertainty_B=np.std(means_B)
    print(f"Population A mean  = {A_mean} ± {uncertainty_A}")
    print(f"Population B mean  = {B_mean} ± {uncertainty_B}")
    if abs(A_mean-B_mean)<=2*(uncertainty_A+uncertainty_B):
        print("Samples are consistent")
    else:
        print("Samples are not consistent")

#task1()

patient_number=50
initial_symptoms=100
time=10

def drug_response(s, time, lam):
    return s*np.exp(-lam*time)


def pseudo_data(mean, standart_deviation):
    decay_constant=np.random.normal(mean, standart_deviation)
    symptom_reduction=drug_response(initial_symptoms, time, decay_constant)
    return symptom_reduction

def create_population(mean, standart_deviation):
    population=[]
    for i in range (patient_number):
        population.append(pseudo_data(mean, standart_deviation))
    population=np.split(np.array(population), 5)
    return population

def calculations(population):
    mean=[]
    for i in population:
        mean.append(np.average(i))
    mean=np.array(mean)
    return np.average(mean), np.std(mean)

meanA, stdA=calculations(create_population(0.2, 0.02))
meanB, stdB=calculations(create_population(0.05, 0.02))

if abs(meanA-meanB)<=3*np.sqrt(stdA**2+stdB**2):
    print("consistent")
else:
    print("not consistent")

print(f"Mean A: {meanA} std A: {stdA}")
print(f"Mean B: {meanB} std B: {stdB}")