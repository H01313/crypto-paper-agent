#!/usr/bin/env python3
import json
from datetime import datetime

print("🚀 CRYPTO AGENT WERKT!")

trade = {
    "time": datetime.now().isoformat(),
    "symbol": "BTC/USDT",
    "action": "buy",
    "price": 65234,
    "rsi": 28.5,
    "winrate": 0.65,
    "simulation": True
}

print("TRADE:", json.dumps(trade, indent=2))

with open('logs.json', 'w') as f:
    json.dump([trade], f)

print("✅ LOGS GESAVED!")
