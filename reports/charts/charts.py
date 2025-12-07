import matplotlib.pyplot as plt


def plot_data(x, y, title="Sample Chart", xlabel="X-axis", ylabel="Y-axis"):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.show()