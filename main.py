import matplotlib.pyplot as plt
import numpy as np

def plot_sine_wave():
    """
    Generates and plots a sine wave.
    """
    # Generate data for the sine wave
    x = np.arange(0, 4 * np.pi, 0.1)
    y = np.sin(x)

    # Create the plot
    plt.plot(x, y)
    plt.title("Sine Wave")
    plt.xlabel("Angle [rad]")
    plt.ylabel("sin(x)")
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    
    # Display the plot
    plt.show()


if __name__ == "__main__":
    plot_sine_wave()
