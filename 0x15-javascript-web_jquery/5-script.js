// A javascript script that adds <li> elements to the list
// when the user clicks on the tag DIV#add_item
/* global $ */
$('#add_item').click(function () {
  $('ul.my_list').append('<li>Item</li>');
});
