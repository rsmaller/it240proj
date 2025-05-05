function verifyEmbed() {
    return !document.createElement('embed').getContext; /* Sourced from https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection */
}

function setEmbedStyles() { /* Element selectors sourced from https://stackoverflow.com/questions/36587177/how-can-i-conditionally-change-css-styles-with-js */
    if (verifyEmbed()) {
        console.log("<embed> is supported.");
    } else {
        console.log("<embed> is not supported.");
        console.log(document.getElementById("resume-embed"));
        document.getElementById("resume-embed").classList.add("hidden");
        document.getElementById("unsupported-embed-message").classList.remove("hidden");
    }
}

function main() {
    setEmbedStyles();
}

window.onload = main; /* Sourced from https://stackoverflow.com/questions/8739605/getelementbyid-returns-null */
