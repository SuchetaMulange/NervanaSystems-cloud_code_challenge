"""
Handles the work of validating and processing command input.
"""

from multiprocessing import Process, Queue
import os
import time
import subprocess
from threading import Timer
import sqlite3


def get_valid_commands(queue, fi):
    # TODO: efficiently evaluate commands
	f=open(fi,'r');
	flag=True;
	commands=[]
	valid_commands={}
	for line in f:
		line=line[:-1]
		if line=='[COMMAND LIST]':
			continue;
		if line=='[VALID COMMANDS]':
			flag=False
			continue;
		if flag:
			commands.append(line);
		if flag==False:
			valid_commands[line]=0;
	f.close();

	for command in commands:
		if command in valid_commands.keys():
			valid_commands[command]+=1;

	for command in valid_commands.keys():
		if valid_commands[command]>0:
		    queue.put(command)

	#print(commands)



def process_command_output(queue):
    # TODO: run the command and put its data in the db

	conn = sqlite3.connect('commands.db')
	while not queue.empty():
		command_actual=queue.get();
		command=command_actual.replace("\"","").split()
		start=time.time();
		print (command)
		try:
			proc = subprocess.Popen(command, stdout=subprocess.PIPE)#, shell=True)
			(out, err) = proc.communicate()
		except Exception:
			out="Error executing the command"
		end=time.time()-start;
		if end>60:
			end=0
		if end<1:
			end=1
		conn.execute("INSERT INTO COMMANDS (Command,Command_Length,Time_to_complete,Output) VALUES (command_actual, len(command_actual), end, out );");


