import numpy as np
import matplotlib.pyplot as plt 


def task1():
    t=np.linspace(0, 10, 100)
    a=np.sin(t)

    plt.plot(t,a)
    plt.xlabel("t sec")
    plt.ylabel("A [m]")
    plt.title("Sinusoidal Function")
    plt.grid(True)
    plt.show()

def task2():
    bins=["A", "B", "C", "D"]
    values=[35, 23, 22, 45]
    plt.bar(bins, values)
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.title("Bar plot")
    plt.show()

def task3():
    data=np.random.normal(3, 0.5, 1000000)
    data2=np.random.normal(3, 0.5, 1000)
    fig, axs = plt.subplots(1, 2)
    axs[0].hist(data, bins=50)
    axs[1].hist(data2, bins=50)
    axs[0].set_xlabel("<A>")
    axs[1].set_xlabel("<A>")
    axs[0].set_ylabel("Entries")
    axs[1].set_ylabel("Entries")
    fig.suptitle("Histogram")
    plt.show()

def task4():
    x=np.arange(1,11)
    y=(10**6)/x**(2)
    y_err=y*0.1

    plt.errorbar(x, y, yerr=y_err, fmt="o", ecolor="red", capsize=5)
    plt.yscale("log")
    plt.show()

def task5():
    x = np.arange(1, 11)

    y = 1e6 / (x ** 2)
    # 10% uncertainty of y-values
    y_err = 0.1 * y

    # Plot with error bars and a logarithmic y-axis
    plt.errorbar(x, y, yerr=y_err, fmt="o", label="Data␣with␣uncertainty", ecolor
    ="red", capsize=5)

    plt.xlabel("x")
    plt.ylabel("x")
    plt.yscale("log") # Set y-axis to logarithmic scale
    plt.title("Box␣Plot␣with␣Statistical␣Uncertainty␣(Logarithmic␣y-axis)")
    plt.grid(True)
    plt.legend()
    plt.show()
''''
task1()
task2()
task3()
'''
task4()
task5()