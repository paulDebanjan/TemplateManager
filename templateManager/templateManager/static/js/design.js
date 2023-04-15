let homeData = JSON.parse(document.getElementById('my-data').getAttribute('data-my-data'));

function background(){
myURl = "/media/" + homeData.backbroundImage;
document.body.style.backgroundImage = 'url('+myURl+')';
document.body.style.backgroundSize= "cover";
document.body.style.backgroundPosition= "center";
document.body.style.backgroundRepeat= "no-repeat";
document.body.style.height="100vh";
}
if (window.location.href.indexOf("home") > -1) {
background();
}

const logoOne = document.getElementById("logo-style-one");
const logoTwo = document.getElementById("logo-style-two");


logoOne.innerText = homeData.webSiteName;
logoOne.style.color = "#" + homeData.logoColor;  
logoOne.style.fontSize = homeData.webSiteNameSize + "px"; 

logoTwo.innerText = homeData.webSiteCommit;
logoTwo.style.fontSize = homeData.webSiteCommitSize + "px";  
logoTwo.style.color = "#" + homeData.logoColor;  