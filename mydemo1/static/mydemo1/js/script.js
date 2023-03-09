imageCont = document.querySelector(".notePicMain")
selectedCont = document.querySelector(".selectedPic")
selectedCont = document.querySelector(".image")
selectdImg = selectedCont.getElementsByTagName("img")
let angle = 0
    // imageSel = document.querySelector(".notePicOuter .selectedPic .image img")

images = imageCont.querySelectorAll(".item")

images.forEach(element => {
    element.addEventListener(
        "click",
        function() {
            imgsrc = element.getElementsByTagName("img")

            selectdImg[0].src = imgsrc[0].src;
            title = document.querySelector(".notePicOuter .selectedPic .topic h2");

            title.innerHTML = "Topic: " + element.dataset.title;
            selectdImg[0].style.removeProperty('transform');
            angle = 0;
            selectdImg[0].style.zIndex = -10000;

        }
    )
});

controls = document.querySelector(".notePicOuter")
controls = controls.querySelector(".selectedPic")
controls = controls.querySelector(".controls")
controls = controls.querySelectorAll(".contBut")


controls.forEach(element => {
    element.addEventListener(
        "click",
        function() {
            if (this.id == "rotateClock") {
                angle = angle + 90;
                reqHeight = document.querySelector("#selImgConMain").offsetHeight

                ratio = selectdImg[0].offsetWidth / selectdImg[0].offsetHeight
                if (angle % 180 == 0) {
                    selectdImg[0].style.transform = `rotate(${(angle)%360}deg)` + 'scale(1)'
                } else {
                    selectdImg[0].style.transform = `rotate(${(angle)%360}deg)` + `scale(${1/ratio})`;
                }


            } else {
                angle = angle - 90;
                reqHeight = document.querySelector("#selImgConMain").offsetHeight

                ratio = selectdImg[0].offsetWidth / selectdImg[0].offsetHeight
                if (angle % 180 == 0) {
                    selectdImg[0].style.transform = `rotate(${(angle)%360}deg)` + 'scale(1)'
                } else {
                    selectdImg[0].style.transform = `rotate(${(angle)%360}deg)` + `scale(${1/ratio})`
                }
            }
            selectdImg[0].style.zIndex = -1000;

        })
})



function scrollleft() {

    let myDiv = document.querySelector(".notePicOuter .notePicMain");
    myDiv.scrollLeft -= 100; // change this value to adjust scroll amount
}

function scrollright() {
    let myDiv = document.querySelector(".notePicOuter .notePicMain");
    myDiv.scrollLeft += 100; // change this value to adjust scroll amount
}


// imageSel = document.querySelector(".notePicOuter .selectedPic .image img")
// console.log(imageSel)


// function toggleFullscreen() {
//     console.log("HELLO")
//     if (!document.fullscreenElement) {
//         document.querySelector(".notePicOuter .selectedPic .image img").requestFullscreen();
//     } else {
//         document.exitFullscreen();
//     }
// }

// document.querySelector(".notePicOuter .selectedPic .image img").addEventListener('click', toggleFullscreen);