import math
import matplotlib.pyplot as plt

p_c = 100
p_max = 10000
q_c = -.5 

delta_x = 0.02
time_iterations = 1000

def calculate_initial_densities(x_min, x_max, delta_x, time_iterations):
    max_with_step1 = int(1/delta_x)
    print max_with_step1

    return [p_c * (1/math.exp(float(x)/float(max_with_step1))) for x in range(x_min*max_with_step1, x_max*max_with_step1+time_iterations)]

def calculate_initial_flows(x_min, x_max, delta_x, time_iterations):
    max_with_step1 = int(1/delta_x)

    return [q_c * (1/math.exp(float(x)/float(max_with_step1))) for x in range(x_min*max_with_step1, x_max*max_with_step1+(time_iterations * max_with_step1))]

def calculate_dq_dt(flow):
    return [float(flow[x+1]-flow[x])/delta_x for x in range(len(flow)-1)]

def calculate_rho(p_t, dq_dt):
    return [p_t[x] - dq_dt[x] for x in range(1, len(dq_dt))]

def calculate_flow(p_t):
    return [(float(q_c)/p_c) * p_t[x] if p_t[x] < p_c else q_c * ((p_max-p_t[x])/(p_max-p_c)) for x in range(len(p_t))]

def calculate_times(densities):
    max_with_step1 = int(1/delta_x)

    return [float(x) / max_with_step1 for x in range(len(densities))]

densities = calculate_initial_densities(0, 5, delta_x, time_iterations)
flows = calculate_flow(densities)
dq_dt = calculate_dq_dt(flows)

test_x = 0

first_flow = [flows[test_x]]
first_density = [densities[test_x]]

print len(densities)

for i in range(time_iterations):
    densities = calculate_rho(densities, dq_dt)
    flows = calculate_flow(densities)
    dq_dt = calculate_dq_dt(flows)

    #first_flow.append(flows[test_x])
    #first_density.append(densities[test_x])


times = calculate_times(flows)
density_times = calculate_times(densities)

print len(times)
# print len(dq_dt)

# print times[0]
# print dq_dt[0]

plt.plot(times, flows, 'bo-')
#plt.plot(density_times, densities, 'ro-')

#plt.plot([x for x in range(len(first_flow))], first_flow, 'ro-')
#plt.plot([x for x in range(len(first_density))], first_density, 'bo-')
plt.show()
