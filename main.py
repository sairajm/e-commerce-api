import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

import uvicorn
from interface.api.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) 