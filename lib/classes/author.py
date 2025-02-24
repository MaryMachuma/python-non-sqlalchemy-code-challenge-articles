class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not hasattr(self, '_name'):  # Only set on init
            if not isinstance(value, str):
                raise ValueError("Name must be a string")
            if len(value) == 0:
                raise ValueError("Name must be longer than 0 characters")
            self._name = value
        # Silently ignore subsequent attempts

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        from .article import Article
        article = Article(self, magazine, title)
        if article not in self._articles:  # Prevent duplicates
            self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(magazine.category for magazine in self.magazines()))