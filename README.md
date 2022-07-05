# VS Code Remote
This is a small helper that allows connecting to a remote server from *its* command line. It runs a small flask server on the host with VS Code and its CLI tools installed with a singular route, `/open-vscode`, which listens for a json payload containing the path you want to open.

## Running the flask server
This should be ran on the machine where you have VS Code and its CLI tools installed. Only requirement is to have `flask` installed, `pip3 install flask`.
```
FLASK_DEBUG=1 FLASK_APP=vscode_remote_listener.py python3 -m flask run --host=0.0.0.0 --port=8080
```

## Remote server shell script
Add the contents of `code.sh` or source it in your remote server's shell rc file. Make sure to edit the envars with your ip address of the machine running the flask server.

```
export CODE_CLIENT_IP="192.168.0.28"
export CODE_CLIENT_PORT="8080"
```

Once it is added and envars are set, call `code $path_to_dir`. This will then open a VS Code window on your local machine which will then connect to the remote server at that directory. Individual files will currently open the directory they reside in, instead of the singular file. I'm still working on figuring out how to allow for a singular file.
