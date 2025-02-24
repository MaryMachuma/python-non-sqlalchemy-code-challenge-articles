from .author import Author
from .magazine import Magazine
from .article import Article

class ManyToManyDemo:
    def __init__(self):
        self.author1 = Author("Anna Wintour")
        self.author2 = Author("Hamish Bowles")
        self.author3 = Author("Grace Coddington")
        self.mag1 = Magazine("Vogue", "Fashion")
        self.mag2 = Magazine("GQ", "Men's Fashion")
        self.mag3 = Magazine("Elle", "Fashion")

        self.author1.add_article(self.mag1, "Spring Fashion Trends 2025")
        self.author1.add_article(self.mag3, "Summer Style Essentials")
        self.author2.add_article(self.mag1, "The Art of Haute Couture")
        self.author2.add_article(self.mag1, "Sustainable Fashion Futures")
        self.author2.add_article(self.mag2, "Best Dressed Men of the Year")
        self.author3.add_article(self.mag1, "Iconic Fashion Photography")

    def demonstrate_relationships(self):
        print(f"{self.author1.name}'s magazines: {[mag.name for mag in self.author1.magazines()]}")
        print(f"{self.mag1.name}'s contributors: {[author.name for author in self.mag1.contributors()]}")
        print(f"{self.mag1.name}'s contributing authors: "
              f"{[author.name for author in self.mag1.contributing_authors() or []]}")

if __name__ == "__main__":
    demo = ManyToManyDemo()
    demo.demonstrate_relationships()