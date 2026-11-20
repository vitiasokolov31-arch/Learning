import json
servers = {}
drop_server = []
status = ["online", "offline", "maintenance"]
with open("Files/servers.json") as f:
    loaded_data = json.load(f)
    for key, value in loaded_data.items():
        if value in status:
            servers[value] = servers.get(value, 0) + 1
            if value == 'offline':
                drop_server.append(key)
for key, value in servers.items():
    print(f"В состоянии {key} находится {value} серверов")
print(f"Упавшие сервера: {drop_server}")