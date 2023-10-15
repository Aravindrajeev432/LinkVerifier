
# import openpyxl

# # Create a Workbook object
# wb = openpyxl.Workbook()

# # Create a worksheet in the workbook
# ws = wb.create_sheet('Sheet1')

# # Write some data to the worksheet
# ws.cell(row=1, column=1).value = 'Name'
# ws.cell(row=1, column=2).value = 'Age'
# ws.cell(row=2, column=1).value = 'Alice'
# ws.cell(row=2, column=2).value = 25

# # Save the workbook
# wb.save('data.xlsx')

from pprint import pprint
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://coinmarketcap.com/'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
# headers = {
#   'Accepts': 'application/json',
#   'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',
# }

session = Session()
# session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  print(response.status_code)
  
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  