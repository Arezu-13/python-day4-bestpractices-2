import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d

# Loading the data
exp_data = np.load("I_q_IPA_exp.npy")
mod_data = np.load("I_q_IPA_model.npy")

# Extracting q and I 
q_exp, I_exp = exp_data[:,0], exp_data[:,1]
q_mod, I_mod = mod_data[:,0], mod_data[:,1]

# Checking for NaN values
nan_exp = np.isnan(exp_data).any()
nan_mod = np.isnan(mod_data).any()

# Print the results
print(f"Experimental data contains NaN: {nan_exp}")
print(f"Model data contains NaN: {nan_mod}")

# Remove NaN values from experimental data
# Get indices where I_exp is NOT NaN
# Tilde is a bitwise NOT operator and inverts bolean values
# True = NaN, False=non-NaN
# idx is a mask that selects only the valid (non-NaN) values 
# from I_exp.
idx = ~np.isnan(I_exp)  
# Removing NaN values
q_exp_clean, I_exp_clean = q_exp[idx], I_exp[idx] 

# Interpolating the model data to match q_exp
interp_mod = interp1d(q_mod, I_mod, kind = "cubic", fill_value="extrapolate")

def er_func(scale):
    
    """Computing the sum of squared differences 
    between scaled model and experimental data."""
  
    I_mod_scale = interp_mod(q_exp_clean) * scale

    # Squared error
    return np.sum((I_mod_scale - I_exp_clean)**2)  

# Find the best scaling factor
result = minimize_scalar(er_func)

# Extract the optimal scaling factor
# x is an attribute of the optimization result
best_scale = result.x  
print(f"Best scaling factor: {best_scale}")

# Applying the best scaling factor to experimental data
I_mod_best = interp_mod(q_exp_clean) * best_scale

# Plotting both datasets
plt.scatter(q_exp_clean, I_exp_clean, label="Experimental Data", color="blue", s = 2)
plt.plot(q_exp_clean, I_mod_best, label="Scaled Model", color="red", linewidth = 2)
plt.xlabel("Scattering Vector")
plt.ylabel("Scattering Strength")
plt.legend()
plt.show()