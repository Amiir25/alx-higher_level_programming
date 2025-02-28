$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  method: 'GET',
  dataType: 'json',
  success: (data) => {
    const movies = data.results;
    movies.forEach(movie => {
      $('#list_movies').append(`<li>${movie.title}</li>`);
    });
  },
  error: (error) => {
    console.error('Error:', error);
  }
});
