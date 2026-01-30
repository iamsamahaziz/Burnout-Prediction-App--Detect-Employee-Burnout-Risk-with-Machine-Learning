# 🔥 Burnout Prediction - Machine Learning Project

## 📋 Description

Ce projet utilise le Machine Learning pour prédire le risque de burnout chez les employés en milieu professionnel. L'objectif est d'identifier les employés à risque afin de mettre en place des mesures préventives.

## 📊 Dataset

- **Source** : `mental_health_workplace_survey.csv`
- **Taille** : 3000 employés
- **Cible** : `BurnoutRisk` (0 = Pas de risque, 1 = Risque de burnout)
- **Distribution** : 67.3% classe 0, 32.7% classe 1

### Features principales

| Catégorie | Features |
|-----------|----------|
| **Démographique** | Age, Gender, Country |
| **Travail** | JobRole, Department, YearsAtCompany, WorkHoursPerWeek |
| **Bien-être** | StressLevel, SleepHours, WorkLifeBalanceScore |
| **Support** | ManagerSupportScore, HasMentalHealthSupport, HasTherapyAccess |
| **Autres** | SalaryRange, RemoteWork, CommuteTime |

## 🛠️ Technologies utilisées

- **Python 3.12**
- **Pandas** - Manipulation des données
- **Scikit-learn** - Modèles ML
- **NumPy** - Calculs numériques

## 🚀 Modèle

```python
RandomForestClassifier(
    n_estimators=300,
    class_weight='balanced',
    random_state=42
)
```

## 📈 Résultats

| Métrique | Score |
|----------|-------|
| Accuracy | 67.5% |
| Recall (Burnout) | 29% |
| Precision (Burnout) | 30% |

### ⚠️ Limitations

L'analyse exploratoire a révélé que les features ont une très faible corrélation avec la variable cible (max 2.7%). Cela suggère que :
- Le dataset est potentiellement synthétique
- Les features ne capturent pas les vrais facteurs de burnout
- Un dataset réel serait nécessaire pour de meilleures prédictions

## 📁 Structure du projet

```
├── Burnout_prediction.ipynb    # Notebook principal
├── mental_health_workplace_survey.csv  # Dataset
└── README.md                   # Documentation
```

## 🔧 Installation

```bash
pip install pandas scikit-learn numpy matplotlib seaborn
```

## ▶️ Utilisation

```python
# Charger les données
data = pd.read_csv("mental_health_workplace_survey.csv")

# Prétraitement et entraînement
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)

# Prédiction
y_pred = model.predict(X_test)
```

## 👤 Auteur

**Samah AZIZ**  
Étudiante en Licence Ingénierie Informatique  
📧 iamsamahaziz@gmail.com  
🔗 [GitHub](https://github.com/iamsamahaziz) | [LinkedIn](https://linkedin.com/in/samah-az)

## 📝 License

Ce projet est sous licence MIT.
