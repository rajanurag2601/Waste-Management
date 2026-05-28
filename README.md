# Decentralized Accountability: IoT Waste Management Simulation

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.xxxxxxx.svg)](https://doi.org/10.5281/zenodo.xxxxxxx) 
*(Note: Replace the link above with your actual Zenodo DOI badge once generated)*

## Overview
This repository contains the Python-based discrete-event simulation code for the research paper **"Decentralized Accountability: A Low-Cost IoT Framework for Municipal Solid Waste Management in High-Density Informal Settlements"**. 

The model evaluates the technical fault tolerance and economic viability of a hybrid store-and-forward Mobile Reader Unit (MRU) topology paired with passive RFID technology[cite: 1]. It is specifically designed to address the connectivity constraints and high operational expenses (OPEX) in resource-constrained urban environments[cite: 1].

## Features
The simulation is built using the `SimPy` library[cite: 1] and is divided into two primary testing phases:

*   **Phase I (Network Reliability):** Stress-tests the architecture against varying cellular network degradation (20%, 40%, and 60% packet loss) to compare traditional real-time GSM, LoRa/LPWAN, and the proposed offline MRU store-and-forward system[cite: 1].
*   **Phase II (Economic Feasibility):** Calculates operational expenditure (OPEX) savings by comparing unoptimized manual routing against the proposed IoT framework, calibrated with localized economic parameters from Noida, Uttar Pradesh (including local fuel costs and minimum wage data)[cite: 1].

## Prerequisites
To run this simulation, you will need Python 3.8+ and the following libraries:
*   `simpy`
*   `pandas` (for data handling)
*   `matplotlib` (for generating success rate and OPEX charts)

You can install the dependencies using:
```bash
pip install -r requirements.txt
