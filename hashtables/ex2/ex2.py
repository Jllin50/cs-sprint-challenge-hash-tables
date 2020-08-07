
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    cache = {}

    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    
    route.append(cache["NONE"])

    for ticket in tickets:
        t_next = route[-1]
        route.append(cache[t_next])
        if route[-1] == "NONE":
            return route
