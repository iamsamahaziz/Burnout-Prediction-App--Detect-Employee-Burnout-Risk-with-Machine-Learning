# 🔥 Employee Burnout Prediction

## 📋 Description

Projet de Machine Learning pour prédire le risque de burnout chez les employés à partir de données synthétiques. Ce modèle utilise la régression logistique pour classifier les employés selon leur risque de burnout.

## 📊 Dataset

- **Source** : [Kaggle - Synthetic HR Burnout Dataset](https://www.kaggle.com/datasets/ankam6010/synthetic-hr-burnout-dataset)
- **Fichier** : `Synthetic_employee_burnout.csv`
- **Variable cible** : `Burnout` (0 = Pas de burnout, 1 = Burnout)

### Features

| Feature | Description |
|---------|-------------|
| Name | Nom de l'employé (supprimé) |
| Gender | Genre (encodé via one-hot) |
| JobRole | Rôle professionnel (encodé via one-hot) |

## 🛠️ Technologies

- **Python 3.12**
- **Pandas** - Manipulation des données
- **Scikit-learn** - StandardScaler, LogisticRegression, Metrics

## � Pipeline

1. Chargement des données (`pd.read_csv()`)
2. Prétraitement (suppression "Name", One-hot encoding)
3. Normalisation (`StandardScaler`)
4. Split 80/20 stratifié
5. Modélisation (`LogisticRegression(class_weight="balanced")`)
6. Prédiction avec seuil 0.80

## 📈 Résultats

| Métrique | Score |
|----------|-------|
| **Accuracy** | 96.25% |
| **Recall (Burnout)** | 88.46% |
| **Precision (Burnout)** | 65.71% |

## 📁 Structure

```
Burnout_Projet/
├── Burnout_prediction.ipynb
├── Synthetic_employee_burnout.csv
└── README.md
```

## 🔧 Installation

```bash
pip install pandas scikit-learn numpy
```

## 👤 Auteur

**Samah AZIZ**  
Étudiante en Licence Ingénierie Informatique - FST Mohammedia  
📧 iamsamahaziz@gmail.com  
🔗 [GitHub](https://github.com/iamsamahaziz) | [LinkedIn](https://linkedin.com/in/samah-az)
