user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["id", "username", "email"]
}