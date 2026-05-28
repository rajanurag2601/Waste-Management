"""
Phase I Simulation — Packet Delivery vs. Network Outage Probability
===================================================================
Discrete-event simulation for the paper:
  "Decentralized Accountability: A Low-Cost IoT Framework for
   Municipal Solid Waste Management in High-Density Informal Settlements"

Systems compared
----------------
1. GSM Real-Time Tracking     : packet lost permanently if link is DOWN
2. LoRa / LPWAN Real-Time     : ~20 % better penetration than GSM in
                                  dense iron-sheet environments
3. Proposed MRU Store-and-Forward : offline buffering; only lost on
                                    hardware failure or depot sync error

Simulation parameters
---------------------
Nodes              : 1,000 collection points
Workers (MRUs)     : 10
Duration           : 30 days  =>  30,000 collection events
HW failure rate    : 2 % / month  (0.067 % / day)
Depot sync fail    : 0.2 % per sync attempt
Outage levels      : 20 %, 40 %, 60 %
Random seed        : 42 (reproducible)
"""

import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

random.seed(42)
np.random.seed(42)

# ── constants ──────────────────────────────────────────────────────────────────
DAYS            = 30
NODES           = 1_000
COLLECTIONS     = DAYS * NODES
HW_FAIL_DAILY   = 0.02 / 30
DEPOT_SYNC_FAIL = 0.002
OUTAGE_LEVELS   = [0.20, 0.40, 0.60]
LABELS          = ["20 %", "40 %", "60 %"]


def simulate(outage_rate: float) -> dict:
    gsm_delivered  = 0
    lora_delivered = 0
    mru_delivered  = 0
    lora_outage    = outage_rate * 0.80   # LoRa better penetration

    for _ in range(COLLECTIONS):
        # GSM
        if random.random() >= outage_rate:
            gsm_delivered += 1
        # LoRa
        if random.random() >= lora_outage:
            lora_delivered += 1
        # MRU Store-and-Forward
        if random.random() < HW_FAIL_DAILY:
            continue
        if random.random() >= DEPOT_SYNC_FAIL:
            mru_delivered += 1

    total = COLLECTIONS
    return {
        "GSM":  round(gsm_delivered  / total * 100, 1),
        "LoRa": round(lora_delivered / total * 100, 1),
        "MRU":  round(mru_delivered  / total * 100, 1),
    }


results = {lvl: simulate(lvl) for lvl in OUTAGE_LEVELS}

# ── print table ────────────────────────────────────────────────────────────────
print(f"{'Outage':>10}  {'GSM':>8}  {'LoRa':>8}  {'MRU':>8}")
for lvl, res in results.items():
    print(f"{lvl*100:>9.0f}%  {res['GSM']:>7.1f}%  {res['LoRa']:>7.1f}%  {res['MRU']:>7.1f}%")

# ── plot ───────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
x, width = np.arange(len(OUTAGE_LEVELS)), 0.24
colors = {"GSM": "#d32f2f", "LoRa": "#f57c00", "MRU": "#388e3c"}

for offset, key, label in [
    (-width, "GSM",  "GSM (Real-Time)"),
    (0,      "LoRa", "LoRa / LPWAN (Real-Time)"),
    (width,  "MRU",  "Proposed MRU (Store-and-Forward)"),
]:
    bars = ax.bar(x + offset, [results[l][key] for l in OUTAGE_LEVELS],
                  width, label=label, color=colors[key], zorder=3)
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2., h + 0.5,
                f"{h:.1f}%", ha="center", va="bottom", fontsize=8.5, fontweight="bold")

ax.set_xlabel("Network Outage Probability", fontsize=11)
ax.set_ylabel("Data Packet Delivery Success Rate (%)", fontsize=11)
ax.set_title("Phase I: Packet Delivery Rate vs. Network Outage Probability\n"
             "GSM vs. LoRa/LPWAN vs. Proposed MRU Store-and-Forward",
             fontsize=11, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(LABELS, fontsize=11)
ax.set_ylim(0, 112)
ax.yaxis.grid(True, linestyle="--", alpha=0.6, zorder=0)
ax.legend(fontsize=9.5, loc="upper right")
plt.tight_layout()
plt.savefig("Figure_3_multi_scenario.png", dpi=200, bbox_inches="tight")
print("Saved Figure_3_multi_scenario.png")