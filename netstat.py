class netstat:

    def __init__(self, proto, local_address, foreign_address, state, pid):
        self.proto = proto
        self.local_address = local_address
        self.foreign_address = foreign_address
        self.state = state
        self.pid = pid

    def __str__(self):
        return "[netstat] " + "[proto=" + self.proto + ", local_address=" + self.local_address + ", foreign_address=" \
               + self.foreign_address + ", state=" + self.state + ", pid=" + self.pid + "]"
