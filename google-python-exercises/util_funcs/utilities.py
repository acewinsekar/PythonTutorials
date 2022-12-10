from urllib.request import urlopen
import sys
import re

## Given a url, try to retrieve it. If it's text/html,
## print its base url and its text.
def wget(url):
  ufile = urlopen(url)  ## get file-like object for url
  info = ufile.info()   ## meta-info about the url content
  print(info)
  domain_name = re.search('https?://([A-Za-z_0-9-.]+).*', url)
  #domain_name = re.search(r'https:\\\\(\w+)\.com', url)
  if domain_name:
      print('domain name extracted ' + domain_name.group(1))
  else:
      print('regex didnt work')

  if info.get_content_type() == 'text/html':
    print('base url:' + ufile.geturl())
    text = ufile.read()  ## read all its text
    #text2 = text.decode() # to convert to string didn't work and returned a decoding error
    text2 = str(text) #convert to string
    print(type(text))
    dm_name = domain_name.group(1)
    outf = open(dm_name + '.txt', 'w')
    outf.write((text2))
    outf.close()


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: enter url in https://www.url.com format")
    sys.exit(1)

  for url in args:
      wget(url)

  # +++your code here+++
  # Call your functions


if __name__ == '__main__':
    main()
