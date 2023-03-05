rightOuter = document.querySelector(".nav .rightOuter");

rightOuter.addEventListener(
    "click",
    function() {
        menu = document.querySelector(".nav .rightOuter .right");
        if (menu.style.display == "none") {

            menu.style.cssText = `
      display:flex;
      flex-direction:column;
    //   outline:2px solid red;
      width:100vw;
      left:0;
      align-items:center;
      z-index: 1000;
      background-color: rgba(255, 255, 255, 0.356);
      backdrop-filter: blur(5px);
	justify-content:space-evenly;
	height:50vh;
	margin-top:3em;
    `
        } else {
            menu.style.cssText = `
        display:none;
    `
        }
    }
)