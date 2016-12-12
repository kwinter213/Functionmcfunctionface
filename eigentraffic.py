import math
import matplotlib.pyplot as plt

p_c = 40
p_max = 30
q_c = .125
v_max = .01

delta_x = .1
time_iterations = 100

# def calculate_initial_densities(x_min, x_max, delta_x, time_iterations):
#     max_with_step1 = int(1/delta_x)

#     return [p_c * (1/math.exp(float(x)/float(max_with_step1))) for x in range(x_min*max_with_step1, x_max*max_with_step1+time_iterations)]


def calculate_initial_densities(x_min, x_max, delta_x, time_iterations):
    max_with_step1 = int(1/delta_x)
    zero = (x_max-x_min)/2.0
    weight = 10

    return [-1 * weight * ((x_min+float(x)*delta_x)-zero)**2.0 + weight if -1 * weight * ((x_min+float(x)*delta_x)-zero)**2.0 + weight >= 0 else 0 for x in range(max_with_step1*(x_max-x_min))]

def calculate_dq_dt(flow):
    dq_dt_dict = {0:(flow[1]-flow[0])/delta_x, (len(flow)-1):(flow[len(flow)-1]-flow[len(flow)-2])/delta_x}
    return [dq_dt_dict.get(x) if x == 0 or x == len(flow)-1 else (flow[x+1]-flow[x-1])/(2*delta_x) for x in range(len(flow))]

def calculate_rho(p_t, dq_dt):
    return [p_t[x] - dq_dt[x] for x in range(len(dq_dt))]

def calculate_flow(p_t):
    #return [(float(q_c)/p_c) * p_t[x] if p_t[x] < p_c else q_c * ((p_max-p_t[x])/(p_max-p_c)) for x in range(len(p_t))]
    return [p_t[x] * (float(v_max)* (1 - float(p_t[x]/p_max))) for x in range(len(p_t))]

def calculate_times(densities):
    max_with_step1 = int(1/delta_x)

    return [delta_x*x for x in range(len(densities))]

densities = calculate_initial_densities(0, 5, delta_x, time_iterations)
flows = calculate_flow(densities)
dq_dt = calculate_dq_dt(flows)

flow_zero = []
flow_zero.append(flows[0])
den_zero = []
den_zero.append(densities[0])

for i in range(time_iterations):
    densities = calculate_rho(densities, dq_dt)
    flows = calculate_flow(densities)
    dq_dt = calculate_dq_dt(flows)
    flow_zero.append(flows[0])
    den_zero.append(densities[0])


print len(calculate_times(densities))
print len(densities)

print flows[0]
times = calculate_times(dq_dt)
d_times = calculate_times(densities)

nnd = [(d_times[x], densities[x]) for x in range(len(d_times)) if not math.isnan(densities[x]) ]
d_times = [d[0] for d in nnd]
densities = [d[1] for d in nnd]

print len(densities)

#plt.plot(den_zero, flow_zero)
#plt.plot(times, dq_dt, 'ro-')
plt.plot(d_times[:len(d_times)-5], densities[:len(densities)-5], 'bo-')
plt.show()