# Bootcamp-Project-1-Python

## Movie Collection Organizer

This program creates an organized and well-structured movie library catalog that enhances your movie collection by providing additional details, including movie posters.

**Program Overview**

The program accomplishes the following tasks:

- **Collect Path to Movie Library**: It starts by collecting the path to your movie library directory.

- **List Movies**: Using the `os` and `re` modules, the program generates a list of all the movies found in the specified directory.

- **IMDb Lookup**: For each movie, the program queries the IMDb database using the `IMDb` package to gather information.

- **Movie Data Retrieval**: It retrieves essential movie data, such as posters, ratings, genres, release year, and plot summaries.

- **Markdown Catalog**: The program compiles a catalog of movies and their corresponding data in a markdown file named **My_Movies.md** within the movie library folder.

- **Embedded Posters**: To enhance the catalog, movie posters are encoded as base64 and seamlessly embedded in the markdown file.

A sample of the **My_Movies.md** file is provided with the code.





