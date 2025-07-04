import csv
from log_analyzer import LogEntry
import argparse

def commandLine():
    parser = argparse.ArgumentParser(description = 'Accept and display first and last name')
    parser.add_argument('--filename', required=True, help='File Name')
    parser.add_argument('--action', required=True, help='Action')
    parser.add_argument('--country', required=False, default="none", help='2-Letter Country Code')
    return parser.parse_args()

def print_head(a: list):
    weird = 0
    while weird<5:
        print(f"Action Number: {weird+1}")
        print(f"Event Time: {a[weird].event_time}")
        print(f"Action Taken: {a[weird].action}")
        print(f"Action Source IP Address: {a[weird].source_ip}")
        print(f"IPv4 Address Class: {a[weird].ipv4_class}")
        print(f"Action Source Country: {a[weird].country_name}\n")
        weird+=1

def deny_count(a: list):
    elder_Dragons = [monster for monster in a if monster.action=="Deny"]  
    return print(f"{len(elder_Dragons)} log entries were denied.") 

def country_count(a: list, c: str):
    region = [b for b in a if b.country==c]
    return print(f"{len(region)} log entries match this country: {c}.")

def main():
    args = commandLine()
    print(f"Retrieving data from {args.filename}...")

    monster_Hunter = []
    filename = args.filename

    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        dict_reader = csv.DictReader(f)
        monster_list = list(dict_reader)
        # 'k' refers to the 'key' and 'v' refers to the 'value'
        # Note that you retrieve the key:value pairs through the dictionary's `.items()` method
        for monster in monster_list:
            monster_Hunter.append(LogEntry(monster['event_time'],monster['internal_ip'],monster['port_number'],monster['protocol'],monster['action'],monster['rule_id'],monster['source_ip'],monster['country'],monster['country_name'],))

    if args.action=="head":
        print_head(monster_Hunter)
    if args.action=="Deny":
        deny_count(monster_Hunter)
    if args.country != "none":
        country_count(monster_Hunter, args.country)




if __name__ == "__main__":
    main()