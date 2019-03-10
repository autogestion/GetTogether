## PubGate Blog
Extension for [PubGate](https://github.com/autogestion/pubgate), adoption of [GetTogether](https://github.com/GetTogetherComm/GetTogether)


Requires PubGate >= 0.2.7
### Run

 - Install PubGate
 - Install gettogether
 ```
 pip install git+https://github.com/autogestion/pg-GetTogether.git

```
 - Update conf.cfg with
```
EXTENSIONS = [..., "gettogether"]
TITLE = 'open source event manager for local communities'
```
 - run
```
python run_api.py

```
