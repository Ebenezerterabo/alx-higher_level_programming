// A javascript script that fetches from this URL:
// https://swapi-api.hbtn.io/api/films/?format=json
/* global $ */
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const hello = $('#Hello').val(data.hello);
  hello.append(data.hello);
});
