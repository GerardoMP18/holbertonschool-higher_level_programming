//  script that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.get(url, (data) => {
  $('DIV#character').text(data.name);
});
