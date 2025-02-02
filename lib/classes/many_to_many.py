class Article:
    # Class variable to store all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        # Initialize an Article instance with author, magazine, and title
        self.author = author
        self.magazine = magazine
        # Use a leading underscore to indicate a private attribute
        self._title = str(title)
        # Append the current instance to the all list
        Article.all.append(self)

    @property
    def title(self):
        # Getter method for the title attribute
        return self._title
    @title.setter
    def title(self, title):
        return self.title 
 # Title is immutable raising an AttributeError exception if tried to change it.
        raise AttributeError("Title is immutable")
   

class Author:
    def __init__(self, name):
        # Initialize an Author instance with a name
        self._name = name
        
    @property
    def name(self):
        # Getter method for the name attribute
        return self._name
    
    @name.setter
    def name(self, new_names):
        self.new_names = new_names
        return self._name
    
    def articles(self):
        # Method to retrieve all articles written by this author
        return [articles for articles in Article.all if articles.author == self]

    def magazines(self):
        # Method to retrieve all magazines this author has contributed to
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Method to add a new article written by this author
        articles = Article(self, magazine, title)
        return articles

    def topic_areas(self):
        # Method to retrieve all unique topics/categories this author has written about
        return list(set([article.magazine.category for article in self.articles()])) if self.articles() else None

    def contributing_authors(self):
        # Method to retrieve all authors who have contributed articles
        return [authors for authors in Author.all if len(authors.articles()) > 0]

class Magazine:
    def __init__(self, name, category):
        # Initialize a Magazine instance with name and category
        self._name = name
        self._category = category
    
    @property
    def name(self):
        # Getter method for the name attribute
        return self._name
    
    @property
    def category(self):
        # Getter method for the category attribute
        return self._category
    
    @name.setter
    def name(self, new_names):
        # Setter method for the name attribute
        # It updates the name attribute if the new name meets certain conditions
        if isinstance(new_names, str):
            if 2 <= len(new_names) <= 16:
                self._name = new_names
        return self._name
    
    @category.setter
    def category(self, new_categories):
        # Setter method for the category attribute
        # It updates the category attribute if the new category is a non-empty string
        if isinstance(new_categories, str):
            if len(new_categories) > 0:
                self._category = new_categories
        return self._category
    
    def articles(self):
        # Method to retrieve all articles published in this magazine
        return [articles for articles in Article.all if articles.magazine == self]

    def contributors(self):
        # Method to retrieve all authors who have contributed articles to this magazine
        return list(set([articles.author for articles in self.articles()]))

    def article_titles(self):
        # Method to retrieve titles of all articles published in this magazine
        titles = [articles.title for articles in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Method to retrieve authors who have contributed more than 2 articles to this magazine
        authors = {}
        for articles in self.articles():
            if articles.author in authors:
                authors[articles.author] += 1
            else:
                authors[articles.author] = 1
        contributing_authors = [author for author, count in authors.items() if count > 2]
        return contributing_authors if contributing_authors else None
