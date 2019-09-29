window.onload = init;
window.onresize = position_items;


/**
 * Called when response from server with a character's
 * translation of text is received
 * @param {event} event: callback for POST request
 */
function got_translate_response(event) {
    console.log("GOt new text" + event.currentTarget.response);
    document.getElementById("output_text").innerHTML = event.currentTarget.response;
}


/**
 * Send a request to translate "text" into character's speak
 * @param {string} character: e.g. 'pirate', 'emoji, etc.
 * @param {string} text: string to be translated to character speak
 */
function send_translate_request(character, text) {
    const TRANSLATE_URL = "http://localhost:47290";
    let data = {'character': character, 'text': text};
    let xhr = new XMLHttpRequest();
    xhr.onload = got_translate_response;
    xhr.open("POST", TRANSLATE_URL, true);  // true for async
    xhr.setRequestHeader('Content-Type', 'application/json; charset=UTF-8');
    xhr.send(JSON.stringify(data));
}


/**
 * Send the text area's text to the server to be translated
 * to the clicked character's speaking style
 * @param {event} event: mouse click
 */
function character_click(event) {
    let in_txt_area = document.getElementById("input_text");
    console.log("clicked on " + event.currentTarget.id);
    send_translate_request(event.currentTarget.id, in_txt_area.value);
    
    let audio_id = event.currentTarget.id + "_sound";
    let audio_elem = document.getElementById(audio_id);
    audio_elem.play();
}


/**
 * Position all characters above the input text area
 */
function position_items() {
    const CHR_SIZE = 100;  // px width and height of a character image
    // get coordinates of input text area
    let in_txt = document.getElementById("input_text");
    let rect = in_txt.getBoundingClientRect();
    // position the characters around the text area
    let characters_div = document.getElementById("characters_div");
    let num_images = characters_div.childNodes.length;
    console.log("num images = " + num_images)
    let counter = 0;
    for (let chr_img=characters_div.firstChild; chr_img!=null; chr_img=chr_img.nextSibling) {
        let left_offset = counter * 100 + rect.left - 23;
        let top_offset = rect.top - CHR_SIZE;
        chr_img.style.left = left_offset.toString() + 'px';
        chr_img.style.top = top_offset.toString() + 'px';
        counter += 1;
    }
}


/**
 * Load and display all characters from characters.json
 * Position the characters near the input text area
 */
function init() {
    let clear_bttn = document.getElementById("clear_bttn");
    clear_bttn.onclick = () => {
        document.getElementById("input_text").value = "";
        document.getElementById("output_text").innerHTML = "";
    };
    
    let characters_div = document.getElementById("characters_div");
    let sounds_div = document.getElementById("sounds_div");
	for (let i=0; i<characters.length; i++) {
		let img_obj = document.createElement("img");
		let img_src = "media/" + characters[i]['image'];
        img_obj.id = characters[i]['name'];
        img_obj.className = 'character_img';
        img_obj.onclick = character_click;
		img_obj.setAttribute("src", img_src);
		characters_div.appendChild(img_obj);
        
        // add audio elements: one per character
        let audio_elem = document.createElement("audio");
        let audio_src = "media/" + characters[i]['sound'];
        let id_value = characters[i]['name'] + "_sound";
        audio_elem.setAttribute("src", audio_src);
        audio_elem.setAttribute("type", "audio/ogg");
        audio_elem.setAttribute('id', id_value);
        sounds_div.appendChild(audio_elem);
	}
    position_items();
}