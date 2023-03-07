rightOuter = document.querySelector(".nav .rightOuter .hamburger");
options = document.querySelector(".nav .rightOuter .right .options");

rightOuter.addEventListener(
    "click",
    function() {
        menu = document.querySelector(".nav .rightOuter .right");
        console.log(menu.style.display)
        if (menu.style.display != "flex") {

            menu.style.cssText = `
				display:flex;
				flex-direction:column;
				width:100%;

				left:0;
				align-items:center;
				z-index: 1000;
				background-color: rgba(255, 255, 255, 0.356);
				backdrop-filter: blur(5px);
				justify-content:space-evenly;
				height:50vh;
				margin-top:3em;
				border-radius:0 0 1em 1em;
				border:1px solid black;
				box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;

    		`

            document.querySelector(".rightOuter .hamburger img").src = closeurl;


        } else {
            menu.style.cssText = `
        		display:none;
    		`
            document.querySelector(".rightOuter .hamburger img").src = openurl;
            options.querySelector(".dropdown-menu").style.display = "none"
        }
    }
)


options.addEventListener(
    "click",
    function() {
        if (window.matchMedia("(max-width: 40em)").matches) {
            if (options.querySelector(".dropdown-menu").style.display != "flex") {
                options.querySelector(".dropdown-menu").style.cssText = `
			display: flex;
			flex-direction: column;
			position: absolute;
			// background-color: rgb(223, 223, 223);
			width:100%;
			left:0;
			align-items:center;
			z-index: 1000;
			background-color: rgba(255, 255, 255, 0.8);
			backdrop-filter: blur(2em);
			border-radius:1em;
			border:1px solid black;
			gap:1em;
		`
                document.querySelector(".rightOuter .right .options .opticontext img").src = dropupurl;

            } else {
                document.querySelector(".rightOuter .right .options .opticontext img").src = dropdownurl;

                options.querySelector(".dropdown-menu").style.display = "none"
            }
        } else {
            if (options.querySelector(".dropdown-menu").style.display != "flex") {
                options.querySelector(".dropdown-menu").style.cssText = `
			display: flex;
			flex-direction: column;
			position: absolute;
			// background-color: rgb(223, 223, 223);
			transform: translate(-25%,10%);
			align-items:center;
			z-index: 1000;
			background-color: rgba(255, 255, 255, 0.8);
			backdrop-filter: blur(2em);
			border-radius:1em;
			border:1px solid black;
			gap:1em;
		`
                document.querySelector(".rightOuter .right .options .opticontext img").src = dropupurl;

            } else {
                document.querySelector(".rightOuter .right .options .opticontext img").src = dropdownurl;

                options.querySelector(".dropdown-menu").style.display = "none"
            }
        }
    }
)