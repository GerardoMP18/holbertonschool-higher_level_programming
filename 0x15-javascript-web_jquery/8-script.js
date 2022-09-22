// script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.hbtn.io/api/films/?format=json
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, (data) => {
  const result = data.results;
  $.each(result, (indexInArray, valueOfElement) => {
    $('UL#list_movies').append('<li>' + valueOfElement.title + '</li>');
  });
});
