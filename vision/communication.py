from ttgLib.TextToGcode import ttg
import matplotlib.pyplot as plt

a = ttg("Hello there", 10, 0, "visualize", 500).toGcode("ON COMMAND", "OFF COMMAND", "FAST COMMAND", "SLOW COMMAND")
plt.plot(a)