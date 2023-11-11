const puppeteer = require('puppeteer');
const fs = require('fs');

(async () => {
    // Launch the browser
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    // Navigate to the webpage
    await page.goto('https://umassdining.com/locations-menus/worcester/menu'); // Replace with your actual URL

    // Extract data
    const data = await page.evaluate(() => {
        const foodElements = Array.from(document.querySelectorAll('.lightbox-nutrition'));

        // Extract data for each food item
        const foodData = foodElements.map((foodElement) => {
            const element = foodElement.querySelector('a');
            const servingSize = element ? element.getAttribute('data-serving-size') : '';
            const calories = element ? element.getAttribute('data-calories') : '';
            const total_fat = element ? element.getAttribute('data-total-fat') : '';
            const total_carbohydrates = element ? element.getAttribute('data-total-carb') : '';
            const protein = element ? element.getAttribute('data-protein') : '';

            return {
                name: foodElement.textContent.trim(),
                serving_size: servingSize.trim(),
                calories: calories.trim(),
                total_fat: total_fat.trim(),
                total_carbohydrates: total_carbohydrates.trim(),
                protein: protein.trim(),
            };
        });

        return foodData;
    });

    // Close the browser
    await browser.close();

    // Store data in a JSON file
    const jsonContent = JSON.stringify(data, null, 2);
    fs.writeFileSync('output.json', jsonContent);

    console.log('Data extracted and stored in output.json');
})();
