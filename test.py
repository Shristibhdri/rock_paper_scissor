
import requests

server_url = "http://127.0.0.1:8000"  

response = requests.get(f"{server_url}/api/start_session")
print(response.json())

session_id = response.json()["sessionId"]
response = requests.get(f"{server_url}/api/join_session", params={"sessionId": session_id, "username":"user1"})
print(response.json())

response = requests.get(f"{server_url}/api/join_session", params={"sessionId": session_id, "username":"user2"})
print(response.json())

#response = requests.get(f"{server_url}/api/join_session", params={"sessionId": session_id, "username":"user3"})
#print(response.json())

response = requests.get(server_url+"/api/session_info", params={"sessionId": session_id})
print(response)
