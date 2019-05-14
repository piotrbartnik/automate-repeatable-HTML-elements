import os
import csv
import glob
from jinja2 import Environment, FileSystemLoader
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

my_list = []

with open('input.csv') as f:
  csvRead = f.readlines()  


c = 0
while c<len(csvRead):
  csvRead[c] = csvRead[c].split(",")
  c += 1

# Create the jinja2 environment.
current_directory = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_directory))

# Find all files with the j2 extension in the current directory
templates = glob.glob('*.j2') 

i = 0
output = ''
while i < len(csvRead): 
  def render_template(filename):
      return env.get_template(filename).render(
          name=csvRead[i][0],
          country=csvRead[i][1],
          desc=csvRead[i][3],
          imageUrl=csvRead[i][2]
      )
      rendered_string = render_template(f)
      output += rendered_string  


  for f in templates:
      rendered_string = render_template(f)
      output += rendered_string

  i += 1

Html_file= open("output.html","w")
Html_file.write(output)
Html_file.close()

print('That tedious work of adding new HTML elements has been finished')