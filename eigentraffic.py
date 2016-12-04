import math
import matplotlib.pyplot as plt

p_c = 50
p_max = 200
q_c = .125

delta_x = 0.01
time_iterations = 100

def calculate_initial_densities(x_min, x_max, delta_x, time_iterations):
    max_with_step1 = int(1/delta_x)

    return [p_c * (1/math.exp(float(x)/float(max_with_step1))) for x in range(x_min*max_with_step1, x_max*max_with_step1+time_iterations)]

def calculate_initial_flows(x_min, x_max, delta_x, time_iterations):
    max_with_step1 = int(1/delta_x)

    return [q_c * (1/math.exp(float(x)/float(max_with_step1))) for x in range(x_min*max_with_step1, x_max*max_with_step1+(time_iterations * max_with_step1))]

def calculate_dq_dt(flow):
    return [(flow[x+1]-flow[x])/delta_x for x in range(len(flow)-1)]

def calculate_rho(p_t, dq_dt):
    return [p_t[x] - dq_dt[x] for x in range(len(dq_dt))]

def calculate_flow(p_t):
    return [(float(q_c)/p_c) * p_t[x] if p_t[x] < p_c else q_c * ((p_max-p_t[x])/(p_max-p_c)) for x in range(len(p_t))]

def calculate_times(densities):
    max_with_step1 = int(1/delta_x)

    return [float(x) / max_with_step1 for x in range(len(densities))]

densities = calculate_initial_densities(0, 5, delta_x, time_iterations)
flows = calculate_flow(densities)
dq_dt = calculate_dq_dt(flows)

for i in range(time_iterations):
    densities = calculate_rho(densities, dq_dt)
    flows = calculate_flow(densities)
    dq_dt = calculate_dq_dt(flows)


print len(calculate_times(densities))
print len(densities)

plt.plot(calculate_times(densities), densities)
plt.show()