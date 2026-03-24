from fastapi import FastAPI

app = FastAPI()

users = []


@app.get("/square/{num}")
def get_square(num: int):
    return {"number": num, "square": num * num}


@app.post("/add-user")
def add_user(name: str):
    user = {"id": len(users) + 1, "name": name}
    users.append(user)
    return {"message": "user added", "user": user}


@app.put("/update-user/{id}")
def update_user(id: int, name: str):
    for user in users:
        if user["id"] == id:
            user["name"] = name
            return {"message": "user upated", "user": user}
    return {"message": "user  not found"}
