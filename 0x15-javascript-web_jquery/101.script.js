$(document).ready(() => {
  $('#add_item').click(() => {
    $('.my_list').append('<list>Item</list>');
  });

  $('#remove_item').click(() => {
    $('.my_list li').last().remove();
  });

  $('#clear_item').click(() => {
    $('.my_list').empty();
  });
});
