function copyText() {
    var container = document.getElementById('html_code');
    var text = container.innerText;

    // Create a temporary textarea element to hold the text
    var tempTextarea = document.createElement('textarea');
    tempTextarea.value = text;
    document.body.appendChild(tempTextarea);

    // Select the text in the textarea
    tempTextarea.select();
    tempTextarea.setSelectionRange(0, 99999); /* For mobile devices */

    // Copy the selected text to the clipboard
    document.execCommand('copy');

    // Remove the temporary textarea element
    document.body.removeChild(tempTextarea);

    // Alert or display a message to indicate the text has been copied
    alert('Text copied!');
}
        