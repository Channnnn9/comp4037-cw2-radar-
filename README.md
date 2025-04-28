# COMP4037 Coursework 2 - Radar Chart Visualization

This repository contains the Python code for the radar chart visualization created as part of COMP4037 Coursework 2.

## Files

- `radar_chart_visualization.py`: Python script that generates a radar chart comparing six diet groups based on six environmental indicators.

## Data

The dataset `Results_21MAR2022_nokcaladjust.csv` is required to run the Python script.  
**Note**: Due to file size and coursework copyright considerations, the dataset is not included in this repository.  
Please use the original dataset provided in the coursework brief.

## How to Run

1. Install the required Python libraries if not already installed:
    ```
    pip install pandas numpy matplotlib scikit-learn
    ```
2. Place the dataset `Results_21MAR2022_nokcaladjust.csv` in the same directory as the Python script.
3. Run `radar_chart_visualization.py` to generate the radar chart.

## Output

The radar chart compares six diet groups (vegan, veggie, fish, meat, meat50, meat100) across six key environmental indicators:
- GHG emissions
- Land Use
- Water Scarcity
- Eutrophication Potential
- Biodiversity Impact
- Agricultural Water Usage

The chart visually highlights the differences in environmental impact among the diet groups.

---
