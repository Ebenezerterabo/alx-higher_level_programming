// A javascript that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
/* global $ */
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  $('#character').text(data.name);
});
