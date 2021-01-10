// d = {
//     "inputQuery1": "Lorem Ipsem , Lorem Ipsem , Lorem Ipsem , Lorem Ipsem ,",
//     "inputQuery2": "Lorem Ipsem , Lorem Ipsem , Lorem Ipsem , Lorem Ipsem ,",
//     "comparisonMetrics": {
//         "SemanticSimilarity": 50.0,
//         "DoTheyAgree": true,
//         "otherKindOfSimilarity": 60,
//     }
// }

// outputBlock.innerHTML = generateCompareTable(responseQuery);


function getQueryResponse(q1, q2) {

    requestBody = {
        "inputQuery1": q1,
        "inputQuery2": q2
    }

    var settings = {
        "url": "http://hrs2203.pythonanywhere.com/compareQuery",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({ "inputQuery1": q1, "inputQuery2": q2 }),
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        outputBlock.innerHTML = generateCompareTable(JSON(response));
    });

}


function generateCompareTable(inputData) {
    var contentBody = '<table class="table">'
    contentBody += `
    <tr>
        <th>inputQuery1</th>
        <td>${inputData["inputQuery1"]}</td>
    </tr>
    <tr>
        <th>inputQuery2</th>
        <td>${inputData["inputQuery2"]}</td>
    </tr>
    <tr>
        <th>SemanticSimilarity</th>
        <td>${inputData["comparisonMetrics"]["SemanticSimilarity"]}</td>
    </tr>
    <tr>
        <th>DoTheyAgree</th>
        <td>${inputData["comparisonMetrics"]["DoTheyAgree"]}</td>
    </tr>
    <tr>
        <th>otherKindOfSimilarity</th>
        <td>${inputData["comparisonMetrics"]["otherKindOfSimilarity"]}</td>
    </tr>
    </table>
    `
    return contentBody;
}

function compareClickEvent() {
    queryBlock1 = document.getElementById('query1');
    query1 = queryBlock1.value;

    queryBlock2 = document.getElementById('query2');
    query2 = queryBlock2.value;

    outputBlock = document.getElementById("outputBlock");


    if (query1.length == 0 || query2.length == 0) {
        outputBlock.innerHTML = `<p>detected empty query.<p>`
    } else {
        // ======== informing user ===========
        outputBlock.innerHTML = `<p>Comparing Queries Please Wait...<p>`

        getQueryResponse(query1, query2);

    }

}