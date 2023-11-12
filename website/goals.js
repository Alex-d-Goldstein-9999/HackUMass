document.addEventListener('DOMContentLoaded', function () {
    // Retrieve survey data from localStorage
    const age = parseInt(localStorage.getItem('age'));
    const heightFeet = parseInt(localStorage.getItem('heightFeet'));
    const heightInches = parseInt(localStorage.getItem('heightInches'));
    const weight = parseInt(localStorage.getItem('weight'));
    const gender = localStorage.getItem('gender');
    const activityLevel = parseFloat(localStorage.getItem('activityLevel'));

    // Convert height to centimeters
    const height = (heightFeet * 12 + heightInches) * 2.54;

    // Maintenance Calories Calculation using Harris-Benedict equation
    const maintenanceCalories = calculateMaintenanceCalories(weight, height, age, gender, activityLevel);
    document.getElementById('maintenance-calories-result').textContent = `Maintenance Calories: ${maintenanceCalories.toFixed(2)} kcal`;

    // Sliding Bars
    const sliders = document.querySelectorAll("input[type='range']");

    sliders.forEach((slider) => {
        const span = slider.nextElementSibling;
        span.textContent = slider.value;

        slider.addEventListener('input', function () {
            span.textContent = this.value;
        });
    });
});

function calculateMaintenanceCalories(weight, height, age, gender, activityLevel) {
    let bmr;

    if (gender === 'male') {
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age;
    } else {
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.33 * age;
    }

    return Math.round(bmr * activityLevel);
}
