
# Testing in Python using Pytest and unittest



## Commands for the pytest
``` 
1. pytest <filename> -v -m  <mark_name>  -Mark the function using @pytest.mark.<mark_name> above the function 
2. pytest <filename> -v -k "<function_attr>" -finds the function having the attribute and only runs that particular function
```

### Run the test in parallel 
```
- pip install pytest-xdist (install the pytest-xdist package)
- pytest -n <num> runs the test by using multiple workers in parallel

```
