from datetime import datetime
import re
import pytz


class LogEntry():
    def __init__(self, event_time, internal_ip, port_number, protocol, action, rule_id, source_ip, country, country_name):
        format_yo = "%Y-%m-%d %H:%M:%S %Z"
        east = pytz.timezone("US/Eastern")
        initialdt = datetime.strptime(event_time, format_yo)
        fixeddt = east.localize(initialdt)

        self.event_time = fixeddt
        self.internal_ip = internal_ip
        self.port_number = port_number
        self.protocol = protocol
        self.action = action
        self.rule_id = rule_id
        self.source_ip = source_ip
        self.country = country
        self.country_name = country_name

    @property
    def ipv4_class(self):
        a = self.source_ip
        if re.search("^([0-9]|[1-9][0-9]|1[01][0-9]|12[0-7])\D", a):
            return "A"
        if re.search("^(12[89]|1[3-8][0-9]|19[01])\D", a):
            return "B"
        if re.search("^(19[2-9]|2[0-1][0-9]|22[0-3])\D", a):
            return "C"
        if re.search("^(22[4-9]|23[0-9])\D", a):
            return "D"
        else:
            print("Failure to parse.")


