# Property Analysis and Recommendation System

A Python project for exploring residential real-estate listings in Gurgaon, estimating property prices, and finding similar apartment projects. It combines a Streamlit interface with Jupyter notebooks for data preparation, exploratory analysis, feature work, and model experiments.

## What It Does

- **Property price prediction:** estimates a listing price from property type, sector, bedrooms, bathrooms, balconies, property age, built-up area, rooms, furnishing, luxury, and floor category.
- **Apartment recommendations:** ranks similar apartment projects using precomputed similarity matrices built during the recommender workflow.
- **Nearby-location search:** lists locations within a selected distance of a chosen area, based on the bundled distance matrix.
- **Market analysis:** explores price and price-per-square-foot patterns, property area, bedroom mix, and Gurgaon sector locations in the notebooks and analytics app.
- **Data science workflow:** includes separate flat and independent-house cleaning, data merging, missing-value handling, outlier treatment, feature engineering and selection, model selection, and recommendation experiments.

The project data is focused on Gurgaon (Gurugram), Haryana. Predictions and recommendations are exploratory outputs based on the bundled data and artifacts, not professional valuation or investment advice.

## Application Preview

The main Streamlit entry point is `Main_App.py`. Its navigation currently has **Home**, **Price Predictor**, and **Analysis App** options. The Analysis App route currently opens the apartment recommender and nearby-location search. `Analysis_App.py` contains a separate analytics page with a word cloud, area-versus-price charts, a sector price-per-square-foot map, bedroom distributions, and price comparisons.

## Run Locally

### Requirements

- Python 3.10 or newer is recommended.
- Install the packages used by the Streamlit app and notebooks:

```bash
python -m venv .venv
```

Activate the environment, then install dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

python -m pip install streamlit streamlit-option-menu pandas numpy scikit-learn plotly wordcloud matplotlib seaborn xgboost jupyter
```

Some exploratory notebooks may use additional packages depending on which cells are run. Install those in the same environment if a notebook reports a missing import.

### Start the dashboard

From the repository root, run:

```bash
streamlit run Main_App.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) to open in a browser. Keep the CSV and pickle files in the project root; the application loads them using paths relative to its working directory.

To open an individual notebook:

```bash
jupyter notebook
```

Then select the notebook you want to explore. Run notebook cells in order and check the input/output filenames used in each notebook before rerunning it, because many steps write derived CSVs or model artifacts into the repository root.

## How The Application Works

### Price prediction

The **Price Predictor** reads `df.pkl` for the choices shown in its form and loads the trained preprocessing/model pipeline from `pipeline.pkl`. The pipeline predicts log-transformed price; the application converts the result back with `expm1` and displays an approximate range in crore (Cr). The model expects the feature names and categories used during training, so the bundled pipeline and its corresponding data should be kept together.

### Apartment recommendation and distance search

The recommender loads `location_distance.pkl` and `cosine_sim1.pkl`, `cosine_sim2.pkl`, and `cosine_sim3.pkl`. It combines the precomputed similarity matrices with weights of 30, 20, and 8, respectively, to rank projects similar to the selected apartment. The location view uses the distance matrix to show locations within the entered radius.

### Analytics

`Analysis_App.py` reads `data_viz1.csv` and `feature_text.pkl` to render its charts and word cloud. The map uses Plotly with the OpenStreetMap base map.

## Repository Guide

### Streamlit application

| File | Purpose |
| --- | --- |
| `Main_App.py` | Main dashboard navigation and page routing |
| `Price_Predictor.py` | Price prediction form and inference |
| `Recommend_Appartments.py` | Apartment similarity recommendations and location radius search |
| `Analysis_App.py` | Market-analysis charts and map |
| `Home.py` | Home view |

### Notebooks

| Notebook | Focus |
| --- | --- |
| `Univariate_EDA.ipynb`, `Multi_variate_eda.ipynb` | Exploratory analysis of individual and combined property features |
| `pandas_profining.ipynb` | Dataset profiling |
| `data_preprocessing_flats.ipynb`, `data_preprocessing_houses.ipynb` | Cleaning flat and independent-house listings separately |
| `merge_flats_house.ipynb`, `data_preprocessing_level2.ipynb` | Combining and preparing the property data |
| `outlier_detection_removal.ipynb`, `missing_value_impute.ipynb` | Outlier treatment and missing-value handling |
| `feature_engineering.ipynb`, `feature_selection.ipynb` | Derived features and selection of model inputs |
| `baseline_model.ipynb`, `model_selection.ipynb`, `insights_module.ipynb` | Price-prediction baselines, model experiments, and analysis |
| `data_visualization.ipynb` | Visual analysis and preparation of visualization inputs |
| `recommender_system.ipynb` | Apartment recommendation and similarity artifacts |

### Data and generated artifacts

- **Raw/source listings:** `gurgaon_properties.csv`, `flats.csv`, `independent-house.csv`, `appartments.csv`, and `latlong.csv`.
- **Prepared datasets:** `flats_cleaned.csv`, `house_cleaned.csv`, `gurgaon_properties_cleaned_v1.csv`, `gurgaon_properties_cleaned_v2.csv`, `gurgaon_properties_outlier_treated.csv`, `gurgaon_properties_missing_value_imputation.csv`, `gurgaon_properties_post_feature_Selection.csv`, and `gurgaon_properties_post_feature_selection_v2.csv`.
- **Application analysis data:** `data_viz1.csv` and `feature_text.pkl`.
- **Prediction artifacts:** `df.pkl` and `pipeline.pkl`.
- **Recommendation artifacts:** `location_distance.pkl`, `cosine_sim1.pkl`, `cosine_sim2.pkl`, and `cosine_sim3.pkl`.
- **Report:** `output_report.html` contains a generated data-analysis report.

The filenames with `v1`, `v2`, `post_feature_selection`, `missing_value_imputation`, and `outlier_treated` represent intermediate outputs from the notebook workflow. They are not all interchangeable; use the input expected by the notebook you are running.

## Data and Model Notes

- The checked-in datasets and model files are required for the dashboard features described above; do not remove them unless you also update the application paths or regenerate the artifacts.
- Pickle files can execute code when loaded. Only run this project with pickle artifacts from a source you trust.
- The trained pipeline was serialized with a particular Python and scikit-learn environment. If loading it fails after installing current package versions, recreate the environment used to generate it or retrain and export the pipeline.
- The project does not currently include a pinned dependency file, automated tests, or documented model-quality metrics. Model outputs should therefore be validated before any real-world use.
- Source-data provenance, redistribution rights, and update cadence are not documented in the repository. Confirm those details before republishing the underlying data.
