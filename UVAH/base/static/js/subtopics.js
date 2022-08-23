console.log('js file run')

let topics_btns = Array.from(document.getElementsByClassName("subtopic"));
let topics = Array.from(document.getElementsByClassName("topic"));

topics_btns.forEach(element => {
    element.addEventListener("click", show_topic);
});

function show_topic(e) {
    console.log("button clicked")
    topics_btns.forEach(element => {
        element.classList.remove("active");
    });

    e.target.classList.add("active");
    topics.forEach(topic => {
        if(topic.getAttribute("data-name") == e.target.getAttribute("data-name")){
            topic.style.display = "block";
        }else {
            topic.style.display = "none";
        }
    });
}