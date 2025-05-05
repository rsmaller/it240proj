function verifyEmbed() {
    return navigator.pdfViewerEnabled; /* Sourced from https://developer.mozilla.org/en-US/docs/Web/API/Navigator/plugins. */
}

function setEmbedStyles() { /* Element selectors sourced from https://stackoverflow.com/questions/36587177/how-can-i-conditionally-change-css-styles-with-js. */
    embedCompatibility = verifyEmbed();
    if (!embedCompatibility) {
        document.getElementById("resume-embed").classList.add("hidden");
        document.getElementById("unsupported-embed-message").classList.remove("hidden");
    }
    console.log("Resume PDF embed: ", document.getElementById("resume-embed"));
    console.log("PDF viewing compatible: ", embedCompatibility);
}

function main() {
    setEmbedStyles();
}

window.onload = main; /* Sourced from https://stackoverflow.com/questions/8739605/getelementbyid-returns-null. */
