## Target Search Script for ChEMBL API

This Python script automates the process of searching for molecular targets using the ChEMBL API and saves the results to CSV files. It’s useful for researchers or developers working on drug discovery, target validation, or bioinformatics analysis.

### Features
- **Search ChEMBL Targets:** Search for protein or enzyme targets by name (e.g., "alpha-glucosidase").
- **Dynamic CSV Export:** Save target data, including ChEMBL IDs and preferred names, to organized CSV files.
- **Directory Management:** Automatically creates the output directory if it doesn’t exist.
- **Error Handling:** Catches and reports errors during API queries.

### Usage
1. **Install Required Libraries:**
   ```bash
   pip install chembl-webresource-client pandas
   ```

2. **Run the Script:**
   Edit the `query_list` in the `main` function to include your search terms.
   
   ```python
   query_list = ['alpha_glucosidase', 'ppar_gamma']
   ```

3. **Execute the Script:**
   ```bash
   python search_targets.py
   ```

4. **Check Results:**
   The results will be saved as CSV files, named based on the search terms (e.g., `targets_alpha-glucosidase.csv`).

### File Structure
```
├── search_targets.py
├── targets_alpha-glucosidase.csv
└── targets_ppar-gamma.csv
```

### Example Output
| target_chembl_id | pref_name         | search_term        |
|------------------|-------------------|--------------------|
| CHEMBL123456      | Alpha-glucosidase | alpha-glucosidase  |
| CHEMBL654321      | PPAR gamma        | ppar-gamma         |

### Notes
- Ensure you have an active internet connection to access the ChEMBL API.
- Modify the output directory by changing `job_dir` in the `main` function.

This script provides a simple yet powerful way to access and store target data for further analysis. Let me know if you’d like me to add more features or optimize the workflow! 🚀

