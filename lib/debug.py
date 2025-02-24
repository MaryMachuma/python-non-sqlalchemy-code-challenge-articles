from classes.many_to_many import Author, Magazine, Article

author1 = Author("Anna Wintour")
author2 = Author("Hamish Bowles")
mag1 = Magazine("Vogue", "Fashion")
mag2 = Magazine("GQ", "Men's Fashion")

author1.add_article(mag1, "Spring Fashion Trends 2025")
author2.add_article(mag1, "The Art of Haute Couture")
author2.add_article(mag1, "Sustainable Fashion Futures")
author2.add_article(mag2, "Best Dressed Men of the Year")

import ipdb; ipdb.set_trace()