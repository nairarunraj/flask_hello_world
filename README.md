# flask_hello_world
First Python Flask Application

## Setup

### Virtual Python environment

```console
# Create the virtual env named virtualenv
$ python3 -m venv virtualenv

# Activate the venv
$ source venv/bin/activate
```

### Installing flask

```console
(virtualenv) $ pip3 install flask
```

#### Verifying flask installation

```console
(virtualenv) $ python
>>> import flask
>>>
```

## Running the application

### hello_world

```console
(virtualenv) $ export FLASK_APP=hello_world/hello.py
(virtualenv) $ flask run
```

OR,

```python
# Ensure that the following lines is added to hello.py-
#!/usr/bin/env python

if __name__ == '__main__':
    app.run()
```

```console
(virtualenv) $ chmod +x 1_hello_world/hello.py
(virtualenv) $ ./1_hello_world/hello.py
```
