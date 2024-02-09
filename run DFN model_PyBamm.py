import pybamm

#loading the Doyle-Fuller-Newman (DFN) model 
model = pybamm.lithium_ion.DFN()     

#We now use this model to create a PyBaMM Simulation, which is used to process and solve the model:
sim = pybamm.Simulation(model)

#We can then call 'solve' on our simulation object to solve the model, passing the window of time to solve for in seconds (here 1 hour):
solveSim = sim.solve([0, 3600])
print(solveSim)

#Finally, we can call 'plot' to generate a dynamic plot of the key variables:
sim.plot()
