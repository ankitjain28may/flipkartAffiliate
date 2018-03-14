# Flipkart Affiliate
> Fetch the Products data from Flipkart through Flipkart Affiliate

## Installation

1- Install python 3.5 from [Python.org](https://www.python.org)

2- `sudo apt-get install python3-pip` (For Ubuntu Users)

3- Install all these package `requests `, `csv`, `json`, `os`

4- Add your [Flipkart Affiliate](https://affiliate.flipkart.com/api/api-token) Keys in the file `main.py`

```python
    fkAffiliateId = 'affiliateId'
    fkAffiliateToken = 'affiliateToken'
```

5- After the installation, open terminal at the root folder--
    Run `python3 main.py` or `python main.py`

## Some Useful Installation Tips

If you have already installed python 2.7 install python 3 as well but it may be the problem that the packages installed with respect to python 2.7 and shows error for the python 3 packages,

So you need to install virtual Environment for the python 3 to install python3 packages.

```
    virtualenv -p /usr/bin/python3 py3env
    source py3env/bin/activate
    pip install package-name
```

After setting virtual environment install packages listed above and Enjoy.

P.S For more python scripts Go To -> [pythonResources](https://github.com/ankitjain28may/pythonResources)
