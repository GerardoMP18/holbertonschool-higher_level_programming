// script that fetches and prints how to say “Hello” depending on the language
document.addEventListener('DOMContentLoaded', () => {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=';
  $('INPUT#btn_translate').click(() => {
    const language = $('INPUT#language_code').val();
    const endpoint = url + language;
    $.get(endpoint, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
