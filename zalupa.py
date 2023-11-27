import warnings # Потому что в будущем в библиотеках будут изменения
warnings.filterwarnings("ignore")

import numpy as np
import seaborn as sns
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, recall_score, precision_score, f1_score, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split
from umap import UMAP

def read_data(filename: str, delimeter=','):
    with open(filename, mode="r", newline='') as f:
        features = list()
        targets = list()
        for row in f:
            line = list()
            for s in row.split(delimeter):
                s = s.strip()
                if s:
                    line.append(s)
            features.append(list(map(float ,line[1:-1])))
            targets.append(int(line[-1])-1)
    return features, targets

def make_meshgrid(x, y, h=.02):
    x_min, x_max = x.min() - 1, x.max() + 1
    y_min, y_max = y.min() - 1, y.max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                        np.arange(y_min, y_max, h))
    return xx, yy

def plot_contours(model, xx, yy, ax, **params):
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.contourf(xx, yy, Z, **params)
    return out

def plot_surface(model, xx, yy, ax, **params):
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    out = ax.plot_surface(xx, yy, Z, **params)
    return out

def plot_results(features, targets, model, figsize=(10, 5), in3d=False):
    xx, yy = make_meshgrid(features[:, 0], features[:, 1])

    fig = plt.figure(figsize=(15, 15))
    
    if in3d:
        ax = fig.gca(projection='3d')
    else:
        ax = fig.gca()
    colormap = 'coolwarm'
    labels = np.unique(targets).tolist()
    palette = np.array(sns.color_palette(colormap, n_colors=len(labels)))
    cmap = sns.color_palette(colormap, as_cmap=True)

    patchs = []
    for i, color in enumerate(palette):
        patchs.append(mpatches.Patch(color=color, label=i))
    if in3d:
        plot_surface(model, xx, yy, ax, cmap=cmap, alpha=0.8)
    else:
        plot_contours(model, xx, yy, ax, cmap=cmap, alpha=0.8)
    plt.scatter(features[:, 0], features[:, 1], c=targets, cmap=cmap, s=40, edgecolors='k')
    # plt.xticks(())
    # plt.yticks(())
    plt.axis('off')
    # plt.legend(handles=patchs, loc='upper right')
    plt.show()

features, targets = read_data('123.data', delimeter=',')
features = np.array(features)
targets = np.array(targets)
print(classification_report(targets, targets))
np.unique(targets)
print(classification_report(targets, targets))
features = UMAP().fit_transform(features)
features = StandardScaler().fit_transform(features)
x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.3, stratify=targets, shuffle=True)
x_train.shape, x_test.shape

svc_parameters = {
    'kernel':['poly', 'rbf', 'sigmoid'],
    'C': np.linspace(1, 10, 11),
    'degree': np.linspace(3, 6, 4)
}

clf_svc = GridSearchCV(SVC(), svc_parameters)

clf_svc.fit(x_train, y_train)
clf_svc.best_params_
print(classification_report(y_train, clf_svc.predict(x_train), digits=3, zero_division=0))
print(classification_report(y_test, clf_svc.predict(x_test), digits=3, zero_division=0))
best_svc = SVC(**clf_svc.best_params_)
best_svc.fit(x_train, y_train)
len(best_svc.support_vectors_)

plot_results(features, targets, best_svc, figsize=(15, 10))
plot_results(features, targets, best_svc, figsize=(13, 13), in3d=True)