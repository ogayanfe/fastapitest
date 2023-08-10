from typing import Any


class PostDatbase:

    _db: list[dict[str, Any]] = []
    _current_id = 1

    @classmethod
    def add_post(cls, title: str, content: str) -> dict: 
        if not isinstance(title, str):
            raise TypeError(f"{title} is not a string instance")

        elif not isinstance(content, str):
            raise TypeError(f"{content} is not a string instance")

        cls._db.append({
            'id': cls._current_id, 
            'title': title, 
            'content': content
        })
        cls._current_id += 1
        return cls._db[-1]
    
    @classmethod
    def update_post(cls, id: int, title: str | None = None, content: str | None = None) -> dict[str, str|int] | None:
        index = None 
        
        for i, v in enumerate(cls._db): 
            if id == v.get('id'):
                index = i
        if index is None: 
            return None
        
        field_content = cls._db[index]
        cls._db[index] = {
            "id": field_content.get("id"), 
            "title": title if title else field_content.get("title"), 
            "content": content if content else field_content.get("content")
        }
        
        return cls._db[index]

    @classmethod
    def delete_post(cls, id: int):
        lnt = len(cls._db)
        cls._db = list(filter(lambda x: x.get("id") != id, cls._db))

        if len(cls._db) < lnt:  # Something was deleted
            return True 
        return False
    
    @classmethod
    def retrieve_post(cls, id: int) -> dict[str, Any] | None:
        match = list(filter(lambda x: x.get("id") == id, cls._db))
        if len(match) == 0:
            return None
        return match[0]
    
    @classmethod
    def all_post(cls):
        return cls._db