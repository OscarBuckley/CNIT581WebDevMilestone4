from .data import ANNOTATIONS, CHAT

def get_annotations(request):
    return {"annotations": ANNOTATIONS}

def get_chats(request):
    return {"chats": CHAT}