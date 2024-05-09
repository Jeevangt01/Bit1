document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('startMiningBtn').addEventListener('click', startMining);
    document.getElementById('viewStatisticsBtn').addEventListener('click', viewStatistics);
    document.getElementById('sendToWalletBtn').addEventListener('click', sendToWallet);
});

function startMining() {
    // Show mining screen and hide others
    document.getElementById('homepage').style.display = 'none';
    document.getElementById('mining-screen').style.display = 'block';
    // Send request to backend to start mining
    fetch('/start_mining', { method: 'POST' })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

function viewStatistics() {
    // Show statistics screen and hide others
    document.getElementById('homepage').style.display = 'none';
    document.getElementById('statistics-screen').style.display = 'block';
    // Send request to backend to fetch statistics
    fetch('/get_statistics')
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}

function sendToWallet() {
    // Show wallet screen and hide others
    document.getElementById('homepage').style.display = 'none';
    document.getElementById('wallet-screen').style.display = 'block';
    // Handle sending rewards to wallet
    const walletAddress = prompt("Enter your Bitcoin wallet address:");
    if (walletAddress) {
        fetch('/send_to_wallet', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ wallet_address: walletAddress })
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
    }
}
