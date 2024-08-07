document.getElementById('search-button').addEventListener('click', function() {
    var query = document.getElementById('search-input').value;
    var resultsDiv = document.getElementById('search-results');

    
    resultsDiv.innerHTML = '';

    if (query.trim() === '') {
        resultsDiv.innerHTML = 'Please enter a search query.';
        return;
    }

    
    resultsDiv.innerHTML = 'You searched for: ' + query;
});