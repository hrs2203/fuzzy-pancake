sampleData = {
    "inputQuery": "inputQuery. inputQuery. inputQuery. inputQuery. inputQuery.",
    "newsArticles": [
        {
            "articleURL": "urlLocation1",
            "articleTitle": "title1",
            "articleBody": "artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1, artice content 1.",
            "fakeDetection": 80.0,
            "clickBaitDetection": 60.0,
        },
        {
            "articleURL": "urlLocation2",
            "articleTitle": "title2",
            "articleBody": "artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2, artice content 2.",
            "fakeDetection": 80.0,
            "clickBaitDetection": 60.0,
        },
        {
            "articleURL": "urlLocation3",
            "articleTitle": "title3",
            "articleBody": "artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3, artice content 3.",
            "fakeDetection": 80.0,
            "clickBaitDetection": 60.0,
        },
        {
            "articleURL": "urlLocation4",
            "articleTitle": "title4",
            "articleBody": "artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4, artice content 4.",
            "fakeDetection": 80.0,
            "clickBaitDetection": 60.0,
        },
        {
            "articleURL": "urlLocation5",
            "articleTitle": "title5",
            "articleBody": "artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5, artice content 5.",
            "fakeDetection": 80.0,
            "clickBaitDetection": 60.0,
        },

    ]

}

function generateTableBody(inputData) {
    var contentBody = '<table class="table">'
    contentBody += "<tr><th>articleURL</th><th>articleTitle</th><th>fakeDetection</th><th>clickBaitDetection</th></tr>"

    for (let index = 0; index < inputData.length; index++) {
        var element = inputData[index];
        contentBody += `
        <tr>
            <td>${element["articleURL"]}</td>
            <td>${element["articleTitle"]}</td>
            <td>${element["fakeDetection"]}%</td>
            <td>${element["clickBaitDetection"]}%</td>
        </tr>`
    }

    contentBody = contentBody + "</table>"
    return contentBody;
}

function getArticleBody(inputData) {
    var contentBody = ""

    for (let index = 0; index < inputData.length; index++) {
        const element = inputData[index];
        contentBody += `
        <div class="card m-2">
            <div class="card-body">
                <h5 class="card-title">${element["articleTitle"]}</h5><hr>
                <p class="card-text">${element["articleBody"]}</p>
            </div>
        </div>`
    }

    return contentBody;
}

function searchClickEvent() {
    queryBlock = document.getElementById('NewsDetection');
    query = queryBlock.value;

    outputBlock = document.getElementById("outputBlock");

    if (query.length == 0) {
        outputBlock.innerHTML = `<p>detected empty query.<p>`
    }

    else {
        sampleData.inputQuery = query;
        // ======== informing user ===========
        outputBlock.innerHTML = `<p>Working on "${query}", please wait...<p>`

        setTimeout(function () {
            // ======== loadind response =========
            outputBlock.innerHTML = ``
            outputBlock.innerHTML += generateTableBody(sampleData.newsArticles);
            outputBlock.innerHTML += "<br>"
            outputBlock.innerHTML += getArticleBody(sampleData.newsArticles);
        }, 3000);
    }




}