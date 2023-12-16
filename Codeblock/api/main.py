from fastapi import FastAPI
from model_configuration.model_constructor import modelConstructor

app = FastAPI()
chain = None

@app.on_event("startup")
async def startup_event():
    global chain
    chain = modelConstructor().get_chain()



@app.get("/")
async def root():
    global chain
    response = chain.run(
    text="Can you describe me how can i deploy my Chatbot LLM model."
    )
    return response