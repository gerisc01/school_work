function validateForm()
{
var title=document.forms["new_item"]["title"].value;
var description=document.forms["new_item"]["description"].value;
var month=document.forms["new_item"]["month"].value;
var day=document.forms["new_item"]["day"].value;
var year=document.forms["new_item"]["year"].value;
if (title == "")
  {
  alert("Invalid Title");
  return false;
  }
if (description == "")
  {
  alert("Invalid Description");
  return false;
  }
if (month == "")
  {
  alert("Invalid Date: Enter Valid Month");
  return false;
  }
if (day == "")
  {
  alert("Invalid Date: Enter Valid Day");
  return false;
  }
if (year == "")
  {
  alert("Invalid Date: Enter Valid Year");
  return false;
  }
return true;	
}
