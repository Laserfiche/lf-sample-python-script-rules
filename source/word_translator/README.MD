GitHub Copilot: Certainly! Here's an updated `README.md` file with instructions on how to use `launcher.py`:

# translator

`translator` is a Python module that provides a simple interface for translating sentences into different languages using the `translate` module.

## Usage

### Command Line Interface

To use `translator` from the command line, you can run the `launcher.py` script with the following arguments:

- `Sentence`: The sentence to translate.
- `LanguageCode`: The language code to translate the sentence into.

Here's an example command to translate the sentence "Hello, how are you?" into Spanish:

```
python launcher.py Sentence="Hello, how are you?" LanguageCode=es
```

This will print the translated sentence to the console in the format `translated : <translated sentence>`.

### Module Interface

To use `translator` as a module in your Python code, you can import the `translate` function from the `translator` module:

```python
from translator import translate

translated_sentence = translate("Hello, how are you?", "es")
print(translated_sentence)  # "Hola, ¿cómo estás?"
```

## Supported Languages

`translator` supports all languages that are supported by the `translate` module. See the [list of ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) for valid language codes.

## License

`translator` is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for more information.
