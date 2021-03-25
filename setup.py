import os

os.system('cmd /c "python -m pip install grpcio --user"')
os.system('cmd /c "python -m pip install grpcio-tools googleapis-common-protos --user"')
os.system('cmd /k "cd src"')
os.system('cmd /c "python -m grpc_tools.protoc -I../ --python_out=. --grpc_python_out=. ../kv.proto"')