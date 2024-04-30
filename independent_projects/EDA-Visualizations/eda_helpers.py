import scipy.stats as stats
from scipy.stats import iqr
import numpy as np
import seaborn as sns
import matplotlib as plt

def custom_stats_information(value, df):
    mode = list(df[value].mode())
    num_items_in_list = len(mode)
    
    q3 = np.quantile(df[value], 0.75)
    q1 = np.quantile(df[value], 0.25)
    q2_50 = np.quantile(df[value], 0.50)
    
    iqr = q3 - q1
    
    # Q3 + 1.5 * IQR: upper outlier gate
    upper_outlier_water_mark_whisker = q3 + 1.5*iqr
    
    # Q1 - 1.5 * IQR: lower outlier gate
    lower_outlier_water_mark_whisker = q1 - 1.5*iqr
    
    if num_items_in_list == 1:
        print('{} has mode value: {}'.format(value, mode[0]))
    else:
        print('{} has multi-mode value: {}'.format(value, num_items_in_list))
        
        
    print("{} min value is {:.2f}\n"
       "{} max value is {:.2f}\n"
       "{} mean value is {:.2f}\n"
       "{} median value is {:.2f}\n"
       "{} std value is {:.2f}\n"
       "{} mode value is {:.2f}  mode items {}\n"
       "{} skew value is {:.2f}\n"
       "{} IQR value is {:.2f}\n"
       "{} Lower outlier gate value is {:.2f}\n"
       "{} Outer outlier gate value is {:.2f}\n"
       "{} Q1_25 value is {:.2f}\n"
       "{} Q_50 value is {:.2f}\n"
       "{} Q3_75 value is {:.2f}".format(value,
                                    df[value].min(),
                                    value,
                                    df[value].max(),
                                    value, 
                                    df[value].mean(),
                                    value,
                                    df[value].median(),
                                    value,
                                    df[value].std(),
                                    value,
                                    num_items_in_list, mode,
                                    value,
                                    df[value].skew(),
                                    value,
                                    iqr,
                                    value,
                                    lower_outlier_water_mark_whisker,
                                    value,
                                    upper_outlier_water_mark_whisker,
                                    value,
                                    q1,
                                    value,
                                    q2_50,
                                    value,
                                    q3))
    
    
def histogram_boxplot(data, feature, figsize=(12, 7), kde=False, bins=None):
    f2, (ax_box2, ax_hist2) = plt.subplots(
        nrows=2,  # Number of rows of the subplot grid= 2
        sharex=True,  # x-axis will be shared among all subplots
        gridspec_kw={"height_ratios": (0.25, 0.75)},
        figsize=figsize,
    )  # creating the 2 subplots
    sns.boxplot(
        data=data, x=feature, ax=ax_box2, showmeans=True, color="violet"
    )  # boxplot will be created and a star will indicate the mean value of the column
    sns.histplot(
        data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins, palette="winter"
    ) if bins else sns.histplot(
        data=data, x=feature, kde=kde, ax=ax_hist2
    )  # For histogram
    ax_hist2.axvline(
        data[feature].mean(), color="green", linestyle="--"
    )  # Add mean to the histogram
    ax_hist2.axvline(
        data[feature].median(), color="black", linestyle="-"
    )  # Add median to the histogram


def sort_values_labeled_barplot(data, feature, perc=False, n=None):
    total = len(data[feature])  # length of the column
    count = data[feature].nunique()
    if n is None:
        plt.figure(figsize=(count + 1, 5))
    else:
        plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=15)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n],
    )

    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # percentage of each class of the category
        else:
            label = p.get_height()  # count of each level of the category

        x = p.get_x() + p.get_width() / 2  # width of the plot
        y = p.get_height()  # height of the plot

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )  # annotate the percentage

    plt.show()  # show the plot


def sort_values_labeled_barplot_top_values(data, feature, perc=False, n=10):  # Set the default value of n to 10
    total = len(data[feature])  # length of the column
    plt.figure(figsize=(n + 1, 5))
    plt.xticks(rotation=90, fontsize=15)
    
    # Sort the data based on the value counts and select the top n values
    ordered_data = data[feature].value_counts().index[:n]
    
    ax = sns.countplot(data=data, x=feature, palette="Paired", order=ordered_data)

    for p in ax.patches:
        if perc:
            label = "{:.1f}%".format(100 * p.get_height() / total)
        else:
            label = p.get_height()

        x = p.get_x() + p.get_width() / 2
        y = p.get_height()

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )
    
    plt.show()