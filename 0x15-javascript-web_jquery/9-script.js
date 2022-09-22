// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays
// the value of hello from that fetch in the HTML tag DIV#hello
$(document).ready(() => {
  const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';
  $.get(url, (data) => {
    $('DIV#hello').text(data.hello);
  });
});
