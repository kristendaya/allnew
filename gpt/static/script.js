function calculateBMI() {
    var weightInput = document.getElementById("weight");
    var heightInput = document.getElementById("height");
    var resultDiv = document.getElementById("result");

    var weight = parseFloat(weightInput.value);
    var height = parseFloat(heightInput.value) / 100; // cm를 m로 변환

    if (isNaN(weight) || isNaN(height)) {
        resultDiv.innerHTML = "Please enter valid weight and height.";
        return;
    }

    var bmi = weight / (height * height);
    var category = "";

    if (bmi < 18.5) {
        category = "Underweight";
    } else if (bmi < 25) {
        category = "Normal weight";
    } else if (bmi < 30) {
        category = "Overweight";
    } else {
        category = "Obese";
    }

    var resultHTML = "<h2>BMI Result</h2>";
    resultHTML += "<p>Your BMI: " + bmi.toFixed(2) + "</p>";
    resultHTML += "<p>Category: " + category + "</p>";

    resultDiv.innerHTML = resultHTML;
}