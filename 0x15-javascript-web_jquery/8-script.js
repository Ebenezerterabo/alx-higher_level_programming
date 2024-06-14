// A javascript script that fetches and lists the titles of the movies
// from this URL: https://swapi-api.hbtn.io/api/films/?format=json
/* global $ */
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const movie of data.results) {
    $('ul#list_movies').append('<li>' + movie.title + '</li>');
  }
});
