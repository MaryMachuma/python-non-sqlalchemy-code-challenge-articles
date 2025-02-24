class Article:
    all = []

    def __init__(self, author, magazine, title):
        from .author import Author
        from .magazine import Magazine
        if not isinstance(author, Author):
            raise ValueError("Author must be an Author instance")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._author = author
        self._magazine = magazine
        # Validate title directly in __init__
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title  # Set directly, no setter for init
        magazine._articles.append(self)
        author._articles.append(self)  # Track in author
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not hasattr(self, '_title'):  # Only set if not initialized
            if not isinstance(value, str):
                raise ValueError("Title must be a string")
            if not 5 <= len(value) <= 50:
                raise ValueError("Title must be between 5 and 50 characters")
            self._title = value
        # Silently ignore subsequent attempts

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from .author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from .magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = value