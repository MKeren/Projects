#import sys; 
import os
import jdk
#print(os.environ['PATH'])

java_path = 'C:\\Program Files\\Java\\jre-1.8\\bin'
if java_path not in os.environ['PATH']:
    os.environ['PATH'] += os.pathsep + java_path

jdk.install('1.1.0',jre=True)


#print(sys.path)