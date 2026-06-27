import numpy as np
import torch

def calculate_gini_coefficient(distribution):
    """
    Calculate the Gini coefficient for a given distribution.
    Gini coefficient is a measure of statistical dispersion intended to represent
    the inequality of a distribution.
    """
    if len(distribution) == 0:
        return 0

    # Sort the distribution
    sorted_distribution = np.sort(distribution)
    n = len(sorted_distribution)
    
    # Calculate Gini coefficient
    cumulative_values = np.cumsum(sorted_distribution)
    gini = (2 * np.sum((np.arange(1, n + 1) * sorted_distribution)) - (n + 1) * cumulative_values[-1]) / (n * cumulative_values[-1])
    return gini


def calculate_entropy(distribution):
    """
    Calculate the entropy of a given distribution.
    Entropy measures the uncertainty or randomness in the distribution.
    """
    distribution = np.array(distribution)
    distribution = distribution[distribution > 0]  # Remove zero entries to avoid log(0)
    probabilities = distribution / np.sum(distribution)
    entropy = -np.sum(probabilities * np.log2(probabilities))
    return entropy


def calculate_herfindahl_index(distribution):
    """
    Calculate the Herfindahl-Hirschman Index (HHI) for a given distribution.
    HHI is a measure of market concentration and can be used to assess decentralization.
    """
    distribution = np.array(distribution)
    probabilities = distribution / np.sum(distribution)
    hhi = np.sum(probabilities ** 2)
    return hhi


def analyze_governance_token_distribution(distribution):
    """
    Analyze the governance token distribution using Gini coefficient,
    entropy, and Herfindahl-Hirschman Index (HHI).
    """
    gini = calculate_gini_coefficient(distribution)
    entropy = calculate_entropy(distribution)
    hhi = calculate_herfindahl_index(distribution)
    return {
        "Gini Coefficient": gini,
        "Entropy": entropy,
        "Herfindahl-Hirschman Index": hhi
    }


if __name__ == '__main__':
    # Dummy data: governance token distributions for four applications
    app1_distribution = np.array([40, 30, 20, 10])  # Example: 4 holders with different shares
    app2_distribution = np.array([25, 25, 25, 25])  # Example: Equal distribution
    app3_distribution = np.array([90, 5, 3, 2])     # Example: Highly unequal distribution
    app4_distribution = np.array([50, 20, 15, 10, 5])  # Example: Moderately unequal distribution

    # Analyze each application's governance token distribution
    for i, distribution in enumerate([app1_distribution, app2_distribution, app3_distribution, app4_distribution], start=1):
        print(f"Application {i} Analysis:")
        results = analyze_governance_token_distribution(distribution)
        for metric, value in results.items():
            print(f"  {metric}: {value:.4f}")
        print()