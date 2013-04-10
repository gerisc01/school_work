function syncLists()
{
  $.ajax({
    type:'get',
    url:'http://knuth.luther.edu/~gerisc01/sync.cgi',
    success:function(data) {
        alert(data);
    }
  });
}