GitHub Copilot: Certainly! Here's an updated `README.md` file for the `template` package:

# template

`template` is a Python package that provides a template for creating Python scripts that can be run on remote agent.

[`mirror.py`](./src/mirror.py) is a simple module that returns the input arguments as output parameters.

## Usage

To use `template`, create a new Python script and import the `YourScriptMethod` function from the `mirror` module:

### Command Line Interface

To use `template` from the command line, you can run the `launcher.py` script with the following arguments:

- `key1=val1`: An input parameter for the script.
- `key2=val2`: An input parameter for the script.
- `key3=val3`: An input parameter for the script.

Here's an example command to run the `YourScriptMethod` function with input parameters `{"key1": "val1", "key2": "val2", "key3": "val3"}`:

```
python launcher.py key1=val1 key2=val2 key3=val3

key1:val1
key2:val2
key3:val3
```

This will print the output parameters to the console in the format `key1:val1`, `key2:val2`, `key3:val3`.

Any text written to `sys.stdout` in the format `key:value` will be parsed as an output parameter by the remote agent worker.

## License

`template` is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for more information.
