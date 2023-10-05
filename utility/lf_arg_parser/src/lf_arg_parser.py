import sys


def get_argument_map(argument_list):
    argument_map = {}
    if argument_list is None:
        raise Exception("Invalid arguments.");
    for arg in argument_list[1:len(argument_list):1]:
        try:
            if arg is not None:
                kv = arg.split('=', 1)
                if len(kv) == 2: # '=' exists
                    key = kv[0]
                    if key is not None and len(key) > 0:
                        value = kv[1]
                        argument_map[key] = value
        except Exception as e:
            sys.stderr.write(f"Could not parse arguments: {str(e)}")
            raise e
    return argument_map
