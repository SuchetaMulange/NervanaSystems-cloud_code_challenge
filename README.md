# NervanaSystems-cloud_code_challenge
A server that processes valid bash command strings

def get_valid_commands(queue, fi)

In this function the commands are read from fi. Initially the valid commands are stored in a Hash Map. Followed by this the commands are compared with the hash map to check if they are valid. If they are, a count is incremented associated with the command in the Hash Map. Next the valid commands are processed

def process_command_output(queue)

In this function the valid commands are processed and output is stored in a Sqlite database

main.py

  def get_command_output()
  
In this function the commands are queried to the Sqlite database and results are returned in a JSON format
  
