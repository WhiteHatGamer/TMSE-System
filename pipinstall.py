import subprocess
import urllib.request

def connect(host='https://www.google.co.in/'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
 
 
def main(module_name):
    subprocess.run('python -m pip install --upgrade pip')
    p = subprocess.run('pip3 install '+module_name)
    if(p.returncode == 1 and connect() == False):
        print("error!! occurred check\nInternet connection")
    elif(p.returncode == 0):
        print("It worked", module_name, " is installed")
    elif(p.returncode == 1 and connect() == True):
        print("error!! occurred check\nName of module")


module_name = input("Enter the module name: ")
main(module_name)
