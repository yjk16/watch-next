class Movie:
    """
    This is the Movie class.  It has instance variables 'title', 'description' and 'similarity'.
    It has the method get_title which will return the title.
    It has the method get_description which will return the description.
    It has the method get_similarity which will return the similarity compared to another movie.
    It has the repr method which will return a string representation of the object.
    """
    def __init__(self, title, description, similarity):
        self.title = title
        self.description = description
        self.similarity = similarity

    def get_title(self):
        """
        gets title of the movie

        :return: title of the movie
        """
        return self.title

    def get_description(self):
        """
        gets description of the movie

        :return: description of the movie
        """
        return self.description

    def get_similarity(self):
        """
        gets similarity of movie

        :return: similarity of movie
        """

        return float(self.similarity)

    def __repr__(self):
        """
        This is a string representation of the movie

        :return: The string representation of the movie including the title, description and current similarity result
        """
        return f"{self.title}: {self.description} This has a current similarity rate of {self.similarity}."
