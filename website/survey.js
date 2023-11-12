function submitSurvey() {
    const age = document.getElementById('age').value;
    const heightFeet = document.getElementById('height-feet').value;
    const heightInches = document.getElementById('height-inches').value;
    const weight = document.getElementById('weight').value;
    const gender = document.getElementById('gender').value;
    const activityLevel = document.getElementById('activity-level').value;

    // Store survey data in localStorage for use on the goals.html page
    localStorage.setItem('age', age);
    localStorage.setItem('heightFeet', heightFeet);
    localStorage.setItem('heightInches', heightInches);
    localStorage.setItem('weight', weight);
    localStorage.setItem('gender', gender);
    localStorage.setItem('activityLevel', activityLevel);

    // Redirect to goals.html
    window.location.href = 'goals.html';
}
