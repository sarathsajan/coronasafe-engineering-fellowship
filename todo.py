import argparse
import sys
import os
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("--add", type=str, help='Add a new todo')
parser.add_argument("--del", type=int, help="Delete a todo", dest='delete')
parser.add_argument("--done", type=int, help="Complete a todo")
parser.add_argument("--ls", action="store_true", help="Show remaining todos")
parser.add_argument("--report", action="store_true", help="Show statistics")
if len(sys.argv) == 1:
    parser.print_help()
    parser.exit()
args = parser.parse_args()

def add_entry(todo_entry, filename):
    with open(filename, "a+") as f:
        f.seek(0)
        data = f.read()
        if data == '':
            f.write(todo_entry)
            f.close()
        else:
            f.close()
            with open(filename, "a+") as f:
                f.write('\n' + todo_entry)
                f.close()

if type(args.add) == str:
    add_entry(args.add, "todo.txt")
    print (f'Added todo: "{args.add}"')

if args.ls:
    try:
        with open("todo.txt", 'r') as f:
            entries = f.read().split('\n')
            entries.reverse()
            n = len(entries)
            for i in range(n):
                output = '[' + str(n - i) +'] ' + entries[i]
                sys.stdout.buffer.write(output.encode('utf8'))
                print ('')
                #print (output)
    except IOError as e:
        print ("There are no pending todos!")


if type(args.delete) == int:
    try:
        with open("todo.txt", 'r') as f:
            entries = f.read().split('\n')
            if args.delete in range(1, len(entries) + 1):
                entries.pop(args.delete - 1)
                f.close()
                os.remove("todo.txt")
                for entry in entries:
                    add_entry(entry, "todo.txt")
                print (f"Deleted todo #{args.delete}")
            else: print (f"Error: todo #{args.delete} does not exist. Nothing deleted.")
    except IOError as e:
        print (e, "\nAdd some todo entries first.")

if type(args.done) == int:
    try:
        with open("todo.txt", 'r') as f:
            entries = f.read().split('\n')
            if args.done in range(1, len(entries) + 1):
                todo_done_entry = entries.pop(args.done - 1)
                f.close()
                os.remove("todo.txt")
                for entry in entries:
                    add_entry(entry, "todo.txt")
                add_entry('x ' + datetime.now().strftime("%Y-%m-%d") + ' ' + todo_done_entry, "done.txt")
                print (f"Marked todo #{args.done} as done.", end='')
            else: print (f"Error: todo #{args.done} does not exist.")
    except IOError as e:
        print (e, "\nAdd some todo entries first.")


if args.report:
    try:
        with open("todo.txt", 'r') as p:
            pending = p.read().split('\n')
            pending_count = len(pending)
            p.close()
    except IOError as e:
        pending_count = 0

    try:
        with open("done.txt", 'r') as c:
            completed = c.read().split('\n')
            completed_count = len(completed)
            c.close()
    except IOError as e:
        completed_count = 0
    
    print (datetime.now().strftime("%Y-%m-%d") + f' Pending : {pending_count} Completed : {completed_count}')