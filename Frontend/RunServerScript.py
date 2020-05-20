import os

# Setting the option for https
is_https = "true"

# Apply cmd prompt command
command_prefix = "cmd /k"

# Run server command
command_suffix = '\"set HTTPS=' + is_https + '&&npm start\"'

# Execute command
os.system(command_prefix + " " + command_suffix)
