import os
from exa_py import Exa

exa = os.environ(api_key="EXA_API_KEY")

result = exa.search_and_contents(
  "le chant des baleines",
  type="auto",
  num_results=10,
  text=True,
  livecrawl="always",
  summary=True
)
