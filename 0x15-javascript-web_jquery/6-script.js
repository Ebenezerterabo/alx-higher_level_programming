// A javascript script that updates the text color of the <header> element
// to New Header!!! when the user clicks on the tag DIV#update_header
/* global $ */
$('#update_header').click(function () {
  $('header').text('New Header!!!');
});
