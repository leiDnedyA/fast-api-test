from fastapi import FastAPI
import random

app = FastAPI()

words = ["dogs", "cats", "electric", "gamer"]

@app.get("/{index}")
async def check_word(index:int):
	if index >= len(words):
		return "Index out of range :("
	return words[index]

@app.get("/")
async def root():
	return words[random.randrange(len(words))]

