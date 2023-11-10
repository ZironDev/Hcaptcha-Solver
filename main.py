import httpx
import requests
import tls_client
from solver import hcep


lola = hcep.solve(sitekey="", siteurl="")
print(f"{lola}")
