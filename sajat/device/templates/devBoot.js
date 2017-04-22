
var $btn = $('#request');
var $lfield = $('#lfield');
 
$btn.on('click', function() {
  $(this).hide();
  $lfield.load('/list.hgg', completeFunction);
});
 
function completeFunction(responseText, textStatus, request) {
  $lfield.css('border', '1px solid #e8e8e8');
  if(textStatus == 'error') {
      $lfield.text('An error occurred during your request: ' +  request.status + ' ' + request.statusText);
  } 
}