$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  method: 'GET',
  dataType: 'json',
  success: (data) => {
    $('#hello').text(data.hello);
  },
  error: (error) => {
    console.error('Error:', error);
  }
});
