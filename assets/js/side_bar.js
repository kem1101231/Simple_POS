
    var open_side_bar = false


    $('#button_open').on('click', function (e){
      if (open_side_bar) {
         closeNav()
         open_side_bar = false
      }
      else{
        openNav()
        open_side_bar = true
      }
    });
		
		function openNav() {
		  document.getElementById("mySidebar").style.width = "250px";
		  document.getElementById("main").style.marginLeft = "250px";
		}

		/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
		function closeNav() {
		  document.getElementById("mySidebar").style.width = "0";
		  document.getElementById("main").style.marginLeft = "0";
		}
