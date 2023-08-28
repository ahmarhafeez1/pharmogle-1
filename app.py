from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def redirect_to_url():
    return RedirectResponse(url="https://utilspy-72upwnyzkbmg2yvgfa2zs4.streamlit.app/")
