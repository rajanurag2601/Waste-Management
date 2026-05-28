import matplotlib.pyplot as plt
import numpy as np

# Set standard academic styling
plt.rcParams.update({'font.size': 12, 'font.family': 'serif'})

def generate_opex_chart():
    # Data from Table II OPEX Breakdown
    categories = ['Fuel', 'Labor', 'Node Maintenance', 'Total OPEX']
    manual_costs = [4500, 6200, 0, 10700]
    iot_costs = [3100, 3200, 50, 6350]

    x = np.arange(len(categories))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, manual_costs, width, label='Manual Model', color='#a3a3a3', edgecolor='black')
    rects2 = ax.bar(x + width/2, iot_costs, width, label='Proposed IoT (MRU)', color='#2b5c8f', edgecolor='black')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Cost (Simulated USD)')
    ax.set_title('Monthly OPEX Breakdown: Manual vs. Proposed Decentralized IoT', pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()

    # Auto-label bars with exact values
    ax.bar_label(rects1, padding=3, fmt='$%d')
    ax.bar_label(rects2, padding=3, fmt='$%d')

    fig.tight_layout()
    
    # Save as high-res PNG for the paper
    plt.savefig('opex_comparison_chart.png', dpi=300, bbox_inches='tight')
    print("Saved: opex_comparison_chart.png")
    plt.show()


def generate_reliability_chart():
    # Data from Network Outage Simulation
    technologies = ['GSM / Real-Time Tracker', 'Store-and-Forward (MRU)']
    success_rates = [65.0, 99.8]  # 35% data loss vs 99.8% reliability

    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Use distinct colors for contrast
    colors = ['#d9534f', '#5cb85c']
    bars = ax.bar(technologies, success_rates, width=0.5, color=colors, edgecolor='black')

    # Add formatting and labels
    ax.set_ylabel('Data Delivery Success Rate (%)')
    ax.set_title('Packet Reliability Under 40% Network Outage Probability', pad=20)
    ax.set_ylim(0, 110) # Set limit slightly higher to fit labels

    # Add percentage labels on top of the bars
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f'{yval}%', ha='center', va='bottom', fontweight='bold')

    fig.tight_layout()

    # Save as high-res PNG for the paper
    plt.savefig('data_reliability_chart.png', dpi=300, bbox_inches='tight')
    print("Saved: data_reliability_chart.png")
    plt.show()

# Execute the functions to generate and save the graphs
if __name__ == "__main__":
    generate_opex_chart()
    generate_reliability_chart()
