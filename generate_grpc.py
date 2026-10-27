import subprocess
import sys

subprocess.run([
    sys.executable, "-m", "grpc_tools.protoc",
    "-I", "src/grpc",
    "--python_out=src/grpc",
    "--grpc_python_out=src/grpc",
    "src/grpc/inventory.proto"
], check=True)
