import time 
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#path to the folder
ROOT_FOLDER = Path(__file__).parent
#path of edgedrive
EDGE_DRIVER_PATH = ROOT_FOLDER / 'driver' / 'edgedrive.exe'

#Function initialize the automation in browser
def make_edge_browser(*options: str) -> webdriver.edge:
  edge_options = webdriver.EdgeOptions()

  # edge_options.add_argument('--headless')
  
  for option in options:
    edge_options.add_argument(option)

  edge_service = Service(
    executable_path=str(EDGE_DRIVER_PATH),
    )

  browser = webdriver.Edge(
    options=edge_options,
    service=edge_service,
  )

  return browser


if __name__ == '__main__':
    # Options is the configs when init the browser
    # options = '--headless', '--disable-gpu',
    options = ()
    
    #init the browser with options in param
    browser = make_edge_browser(*options)

    #Req in browser to url devjack.vercel.app
    browser.get('https://devjack.vercel.app/')

    #Make the window up for 10 sec
    time.sleep(10)
