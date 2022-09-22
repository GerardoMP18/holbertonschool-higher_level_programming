// script that fetches and prints how to say “Hello” depending on the language
// click button And press ENTER in input
document.addEventListener('DOMContentLoaded', () => {
  const resultApi = () => {
    const language = $('INPUT#language_code').val();
    const endpoint = url + language;
    $.get(endpoint, (data) => {
      $('DIV#hello').text(data.hello);
    });
  };
  const url = 'https://stefanbohacek.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(() => {
    resultApi();
  });
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      resultApi();
    }
  });
});
