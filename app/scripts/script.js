const socket = io.connect('/socket.io/');

socket.on('connect', () => {
    console.log('Connected to WebSocket');
});

socket.on('arbitrage_opportunity', data => {
    const trade = JSON.parse(data.trade);
    const tradeHistory = document.getElementById('trade-history');
    const tradeElement = document.createElement('div');
    tradeElement.textContent = `Arbitrage Opportunity: Asset - ${trade.asset}, Exchanges - ${trade.exchanges.join(', ')}, Profit - ${trade.profit}`;
    tradeHistory.appendChild(tradeElement);
});

function adjustThreshold() {
    const threshold = parseFloat(document.getElementById('threshold').value);
    socket.emit('adjust_threshold', { threshold: threshold });
}
