import assistant

def output(o):
    if o is None:
        o=str(o)
    
    assistant_name = assistant.name if assistant.name else "Assistant"
    print(f"{assistant_name}: {o}")
    print()
