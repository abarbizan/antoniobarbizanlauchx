Last login: Sat Feb 19 08:33:07 on console
MacBook-Air-de-antonio-2:~ readsound$ python3 -m venv env
MacBook-Air-de-antonio-2:~ readsound$ source env/bin/activate
(env) MacBook-Air-de-antonio-2:~ readsound$ pip freeze
(env) MacBook-Air-de-antonio-2:~ readsound$ pip install
ERROR: You must give at least one requirement to install (see "pip help install")
WARNING: You are using pip version 21.2.4; however, version 22.0.3 is available.
You should consider upgrading via the '/Users/readsound/env/bin/python3 -m pip install --upgrade pip' command.
(env) MacBook-Air-de-antonio-2:~ readsound$ pip install python-dateutil
Collecting python-dateutil
  Using cached python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting six>=1.5
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: six, python-dateutil
Successfully installed python-dateutil-2.8.2 six-1.16.0
WARNING: You are using pip version 21.2.4; however, version 22.0.3 is available.
You should consider upgrading via the '/Users/readsound/env/bin/python3 -m pip install --upgrade pip' command.
(env) MacBook-Air-de-antonio-2:~ readsound$ pip install python3-dateutil
ERROR: Could not find a version that satisfies the requirement python3-dateutil (from versions: none)
ERROR: No matching distribution found for python3-dateutil
WARNING: You are using pip version 21.2.4; however, version 22.0.3 is available.
You should consider upgrading via the '/Users/readsound/env/bin/python3 -m pip install --upgrade pip' command.
(env) MacBook-Air-de-antonio-2:~ readsound$ pippip freeze
-bash: pippip: command not found
(env) MacBook-Air-de-antonio-2:~ readsound$ pip freeze
python-dateutil==2.8.2
six==1.16.0
(env) MacBook-Air-de-antonio-2:~ readsound$ pip freeze
python-dateutil==2.8.2
six==1.16.0
(env) MacBook-Air-de-antonio-2:~ readsound$ deactivate
MacBook-Air-de-antonio-2:~ readsound$ 
