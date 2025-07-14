from datetime import datetime
chat_log = []

def handler(request):
    global chat_log

    if request.method == "POST":
        data = request.json()
        username = data.get("user", "anon")
        msg = data.get("msg", "").strip()
        if msg:
            chat_log.append({
                "user": username,
                "msg": msg,
                "time": datetime.utcnow().isoformat()
            })
        return {"status": "ok"}

    elif request.method == "GET":
        last_n = int(request.query.get("n", 20))
        return chat_log[-last_n:]

    return {"error": "Invalid request"}
