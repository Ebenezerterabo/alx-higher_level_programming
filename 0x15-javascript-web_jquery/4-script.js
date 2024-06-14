// A javascript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#red_header
/* global $ */
$('#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
