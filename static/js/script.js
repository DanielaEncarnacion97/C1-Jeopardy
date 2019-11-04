function savedQuestion(questionId) {
    alert("Your question with id number: " + questionId + " has been added to favorites.");

    const savedQuestions = localStorage.getItem("savedQuestions")
    const questions = savedQuestions !== null ? savedQuestions.split(",").map(item => item) : []

    if (!questions.includes(questionId)) {

        questions.push(questionId)

        localStorage.setItem("savedQuestions", questions)
    } else {
        localStorage.setItem("savedQuestions", questions.filter(function (item) {
            return item !== questionId
        }))
    }

}

function getSavedQuestions() {
    var returnQuestions = localStorage.getItem("savedQuestions");
    console.localStorage(returnQuestions)

    var line = document.createTextNode(returnQuestions.toString());
    return line
}
