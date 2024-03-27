from fastapi import FastAPI, HTTPException
import random

app = FastAPI()

sessions = {}

def determine_winner(outcome):
    rules = {'rock': 'scissors', 'scissors':'paper', 'paper': 'rock'}
    if len(set(outcome)) == 1:
        return "It's a tie"
    for a in range(len(outcome)):
        if rules[outcome[a]] == outcome[(a+1)%len(outcome)]:
            return f"User {a+1} wins"
        return "No winner"

@app.get("/api/start_session")
def start_session():
    session_id = str(random.randint(100, 999))
    sessions[session_id] = {'users': [], 'outcomes': {}}
    return {
        "status": 1,
        "message": f"Session {session_id} was created successfully.",
        "sessionId": session_id
    }


@app.get("/api/join_session")
def join_session(sessionId: str, username: str):
    if sessionId not in sessions:
        raise HTTPException({

    "status": 0,

    "message": "Cannot join a session - Session with this ID does not exist."
}

)
    if len(sessions[sessionId]['users']) >= 2:
         raise HTTPException({

    "status": 0,

    "message": "Cannot join a session - Session with this ID does not exist."
}

)
    
    if username in sessions[sessionId]['users']:
         raise HTTPException({

    "status": 0,

    "message": "Cannot join a session - Session with this ID does not exist."
}

)
    sessions[sessionId]['users'].append(username)
    outcome = random.choice(["rock", "paper", "scissors"])
    sessions[sessionId]['outcomes'][username] = outcome
    
    return {

    "status": 1,

    "message": "Session 515122 joined successfully.",

    "sessionId": sessionId,

    "username": username,

    "outcome": outcome

}


@app.get("/api/session_info")
def session_info(sessionId: str):
    try:
        sessionId in sessions
        session = session[sessionId]
        users = list(session['outcomes'].keys())  
        outcomes = list(session.values())
        winner = determine_winner(outcomes)
    
    #users = sessions[sessionId]['users']
    #outcomes = sessions[sessionId]['outcomes']
    #winner = determine_winner(outcomes)
    
        return {
        "status": 1,
        "message": "Session information got successfully.",
        "sessionId": sessionId,
        "users": users,
        "outcomes": outcomes,
        "winner" : winner
    }

    except ValueError as e:
        return{
            "status" : 0,
            "message" : f'error {e}'
        }

    except KeyError as e:
        return {
            "status": 0,
            "message": f"KeyError: {e}"
        }