function savedQuestion(questionId)
  {
      alert(questionId);
      
      const savedQuestions = localStorage.getItem("savedQuestions")
      const questions = savedQuestions !== null ? savedQuestions.split(",").map(item => item ) : []
      
      if (!questions.includes(questionId)){
        
        questions.push(questionId)
  
        localStorage.setItem("savedQuestions", questions)
      }else{
        localStorage.setItem("savedQuestions", questions.filter(function(item) {
            return item !== questionId
        }))
      }
      
  }
  