# How Decentralized is the Governance of Blockchain-based Finance?

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2102.10096v2-b31b1b.svg)](https://arxiv.org/pdf/2102.10096v2)

This repository contains the implementation of the research paper **[How Decentralized is the Governance of Blockchain-based Finance: Empirical Evidence from four Governance Token Distributions](https://arxiv.org/pdf/2102.10096v2)** by Johannes Rude Jensen, Victor von Wachter, and Omri Ross. The project provides a Python-based framework to quantify the decentralization of governance power among blockchain-based financial applications by analyzing the distribution of governance tokens.

---

## 📝 Overview of the Paper

The paper addresses the critical question: **How decentralized is the governance of decentralized finance (DeFi) applications?**

### Key Contributions:
1. **Framework for Quantifying Decentralization**: The authors propose a methodology to measure the decentralization of governance power using statistical dispersion metrics.
2. **Empirical Analysis**: The framework is applied to four DeFi governance token distributions, providing insights into the balance between decentralization, user activity, and financial incentives.
3. **Evaluation Metrics**: The study uses statistical measures such as the Gini coefficient, Shannon entropy, and other dispersion coefficients to evaluate the concentration of governance tokens.
4. **Design Implications**: The findings offer guidance for improving governance mechanisms to achieve a more equitable and effective distribution of decision-making power.

The provided implementation allows researchers, developers, and enthusiasts to replicate the analysis, evaluate token distributions, and explore the trade-offs in decentralized governance.

---

## 🚀 How It Works

This repository implements the core ideas of the paper in a Python script (`implementation.py`). Below is a high-level overview of the workflow:

1. **Data Input**:
   - The script accepts governance token distribution data as input. The data should be in the form of a CSV file containing wallet addresses and their corresponding token holdings.
   
2. **Statistical Metrics**:
   - The script computes the following metrics to quantify decentralization:
     - **Gini Coefficient**: Measures inequality in token distribution (0 = perfect equality, 1 = maximal inequality).
     - **Shannon Entropy**: Captures the diversity of token distribution.
     - **Normalized Entropy**: A scaled version of Shannon entropy for easier interpretation.
     - **Theil Index**: Measures economic inequality in token distribution.
   
3. **Visualization**:
   - The script generates visualizations such as Lorenz curves and bar charts to illustrate the token distribution and decentralization metrics.

4. **Output**:
   - The script outputs the computed metrics and visualizations, providing a comprehensive analysis of the token distribution.

---

## 📂 Repository Structure

```
.
├── data/
│   ├── sample_token_distribution.csv   # Example dataset for token distribution
├── results/
│   ├── output_metrics.json             # JSON file containing computed metrics
│   ├── lorenz_curve.png                # Lorenz curve visualization
│   ├── token_distribution.png          # Token distribution bar chart
├── implementation.py                   # Main script for the implementation
├── requirements.txt                    # Python dependencies
├── LICENSE                             # License file
└── README.md                           # Project documentation
```

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blockchain-governance-decentralization.git
   cd blockchain-governance-decentralization
   ```

2. Create a Python virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ⚙️ Usage

### 1. Prepare Your Data
Prepare a CSV file containing the governance token distribution data. The file should have the following format:

| Wallet Address       | Token Holdings |
|----------------------|----------------|
| 0x123...abc          | 1000           |
| 0x456...def          | 500            |
| 0x789...ghi          | 200            |

Save this file in the `data/` directory.

### 2. Run the Script
Run the `implementation.py` script with the path to your data file as an argument:
```bash
python implementation.py --data data/sample_token_distribution.csv --output results/
```

### 3. View the Results
- The computed metrics will be saved in `results/output_metrics.json`.
- Visualizations (e.g., Lorenz curve and token distribution chart) will be saved as PNG files in the `results/` directory.

---

## 📊 Example Output

### Sample Metrics:
After running the script on a sample dataset, you might see output metrics like this:

```json
{
    "Gini Coefficient": 0.72,
    "Shannon Entropy": 3.45,
    "Normalized Entropy": 0.78,
    "Theil Index": 0.65
}
```

### Sample Visualizations:
#### Lorenz Curve:
![Lorenz Curve](results/lorenz_curve.png)

#### Token Distribution:
![Token Distribution](results/token_distribution.png)

---

## 🧠 Future Work

- **Additional Metrics**: Extend the implementation to include more advanced decentralization metrics.
- **Real-Time Analysis**: Integrate with blockchain APIs for real-time governance token analysis.
- **Cross-Chain Comparisons**: Support analysis across multiple blockchain networks and DeFi applications.
- **Interactive Dashboard**: Build a web-based dashboard for dynamic visualization and analysis.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For questions, feedback, or collaboration, feel free to reach out:

- **Author**: Johannes Rude Jensen, Victor von Wachter, Omri Ross
- **Paper**: [How Decentralized is the Governance of Blockchain-based Finance](https://arxiv.org/pdf/2102.10096v2)

If you find this project useful, please consider giving it a ⭐ on GitHub!