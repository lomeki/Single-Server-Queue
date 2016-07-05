# File: Olivia_ssq.py
# Author: Olivia Scott
# Date: 7/4/2016
# Description: Simulates a single server queue of a grocery store
#   given a set of arrival times and service times of customers
#   Prints ID, Queue Arrival Time, Server Arrival Time, Home Arrival Time

# Define Customer class
class Customer:
#   Initiate  class
    def __init__(self,id,queue_arrival,service_time):
        self.id = id
        self.location = 'HOME'
        self.queue_arrival = queue_arrival
        self.service_time = service_time
        self.server_arrival = 0
        self.home_arrival = 0

# get_time
# input: Customer class/instance
# output: Returns the time the customer arrived in the queue
def get_time(cust):
    return cust.queue_arrival


# Create lists of arrival times and service times
arrival_times = [7.470,0.128,0.516,6.506,6.211,2.567,6.671,1.863,3.011,7.477]
service_times = [2.1605,0.345,1.467,0.360,0.957,1.427,0.087,0.8812,1.9959,0.785]

def main(arrival_times,service_times):

    # Create a list of customers and order them into the queue ('line') by arrival time
    # The 'line' is separate from the 'list of customers' because customers will leave the line
    customers = []
    line = []
    total_cust = len(arrival_times)
    for i in range(total_cust):
        cust = Customer(i+1,arrival_times[i],service_times[i])
        customers.append(cust)
        line.append(cust)
    customers.sort(key=get_time)
    line = sorted(line,key=get_time)

    # Reassign ID numbers by order of arrival
    for i in range(total_cust):
        customers[i].id = i+1
        line[i].id = i+1

    # Create final destination (home) and start time at 0
    home = []
    current_time = 0

    # For every customer, find and print their times they arrived at
    # the server (cashier) and home
    print '*' * 60
    print ' ' * 16,'Customer Time Stamps'
    print '- ' * 30
    print 'ID#   Queue Arrival    Server Arrival    Home Arrival'
    for k in range(total_cust):

        # If the next customer hasn't arrived at the current time,
        # update the current time to when they arrive
        if line:
            if current_time < line[0].queue_arrival:
                current_time = line[0].queue_arrival

        # Bring next customer to cashier when they arrive
        at_cashier = line.pop(0)

        # Update server arrival time
        customers[k].server_arrival = current_time
        # Add service time
        current_time += at_cashier.service_time
        # Update home list and home arrival time
        home.append(at_cashier)
        customers[k].home_arrival = current_time

        # Print ID, arrival at
        ID = at_cashier.id
        queue_arrival = at_cashier.queue_arrival
        server_arrival = at_cashier.server_arrival
        home_arrival = at_cashier.home_arrival
        service_time = at_cashier.service_time
        print '%2.d %12.4f %16.4f %16.4f' %(ID,queue_arrival,server_arrival,home_arrival)
    print '*' * 60

main(arrival_times,service_times)