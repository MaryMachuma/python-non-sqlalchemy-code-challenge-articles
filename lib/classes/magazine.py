class Magazine:
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Set via setter
        self.category = category  # Set via setter
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):  # Initial set
            if not isinstance(value, str):
                raise ValueError("Name must be a string")
            if not 2 <= len(value) <= 16:
                raise ValueError("Name must be between 2 and 16 characters")
            self._name = value
        elif isinstance(value, str) and 2 <= len(value) <= 16:  # Subsequent valid set
            self._name = value
        # Silently ignore invalid subsequent attempts

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not hasattr(self, '_category'):  # Initial set
            if not isinstance(value, str):
                raise ValueError("Category must be a string")
            if len(value) == 0:
                raise ValueError("Category must be longer than 0 characters")
            self._category = value
        elif isinstance(value, str) and len(value) > 0:  # Subsequent valid set
            self._category = value
        # Silently ignore invalid subsequent attempts

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None