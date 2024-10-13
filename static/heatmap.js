document.addEventListener('DOMContentLoaded', function() {
    const heatmapContainer = document.getElementById('github-heatmap');
    const days = 365;
    const data = generateRandomData(days);

    for (let i = 0; i < days; i++) {
        const cell = document.createElement('div');
        cell.className = 'heatmap-cell';
        cell.style.backgroundColor = getColor(data[i]);
        cell.title = `${data[i]} contributions on Day ${i + 1}`;
        heatmapContainer.appendChild(cell);
    }
});

function generateRandomData(days) {
    return Array.from({ length: days }, () => Math.floor(Math.random() * 5));
}

function getColor(value) {
    const colors = [
        '#ebedf0',
        '#9be9a8',
        '#40c463',
        '#30a14e',
        '#216e39'
    ];
    return colors[value];
}

// In the future, you can replace the generateRandomData function with an API call to your Flask backend
// Example:
// async function fetchData() {
//     const response = await fetch('/api/github-data');
//     const data = await response.json();
//     return data;
// }