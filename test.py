connected = False
role = None

def Connect():
    if connected:
      raise ValueError("Already connected")

    connected = True
    role = "author"

def ChangeToAuthor():
    if not connected:
        raise ValueError("Not connected")

    if role != "author":
        role = "author"
    else:
        raise ValueError("Role is already author")
    
def ChangeToReviewer():
    if not connected:
        raise ValueError("Not connected")

    if role != "reviewer":
        role = "reviewer"
    else:
        raise ValueError("Role is already reviewer")

def EditPaper():
    if not connected:
        raise ValueError("Not connected")
    if role != "author":
        raise ValueError("Incorrect role: must be author")
    # Whatever code for editing paper

def EditReview():
    if not connected:
        raise ValueError("Not connected")
    if role != "reviewer":
        raise ValueError("Incorrect role: must be reviewer")
    # Whatever code for editing review

def Disconnect():
    if not connected:
        raise ValueError("Not connected")
    
    connected = False
    role = None