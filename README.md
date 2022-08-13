# Python-JQ

Python-JQ is a jq library for Python that just works everywhere. It opts to download
the jq binary and there is little chance for failure with building. 

Python-JQ explicitly defines a function to download the binary, replacing the binary 
in site-packages with your own jq is upto you.

## Installation

Install the package with pip:

```sh
$ pip install git+https://github.com/sonnyksimon/python-jq.git
```

and grab the jq binary:

```sh
$ python -c "import python_jq; python_jq.download_binary()"
```

## Usage

To run with a file:

```python
from python_jq import run_with_file

out = run_with_file('.', 'test/test.json')

print(out)

# {'foo': 'bar'}
```

Or with a JSON dictionary object:

```python
from python_jq import run_with_dict

out = run_with_dict('.', { 'foo': 'bar' })

print(out)

# {'foo': 'bar'}
```

Or even with a string:

```python
from python_jq import run_with_string

out = run_with_string('.', '{ "foo": "bar" }')

print(out)

# {'foo': 'bar'}
```

For complete understanding, please refer to the [source code](https://github.com/sonnyksimon/python-jq).

Thanks!