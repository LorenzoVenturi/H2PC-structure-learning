from matplotlib import pyplot as plt
import numpy as np
import pgmpy
from pgmpy.metrics import structure_score
import pyAgrum as gum
import matplotlib.pyplot as plt
from PIL import Image


def connected_node(arc, target_node):
        if arc[0].equals(target_node):
            return arc[1]
        elif arc[1].equals(target_node):
            return arc[0]

def convertBN_pyAgrum_Pgmpy(pyagrum_net: gum.BayesNet):
    model_h2pc = pgmpy.models.BayesianNetwork()
    for node in pyagrum_net.nodes():
        model_h2pc.add_node(pyagrum_net.variable(node).name())
    for arc in pyagrum_net.arcs():
        source, t2 = arc
        source_label = pyagrum_net.variable(source).name()
        target_label = pyagrum_net.variable(t2).name()
        model_h2pc.add_edge(source_label,target_label)
    return model_h2pc

def calculate_metrics(model_predicted, true_model,time,test_data):
    frozen_predicted_edges = {frozenset(edge) for edge in model_predicted.edges()}
    frozen_true_edges = {frozenset(edge) for edge in true_model.edges()}
    predicted_edges=set(model_predicted.edges())
    true_edges = set(true_model.edges())
    
    true_frozen_positives = frozen_predicted_edges & frozen_true_edges  
    false_frozen_positives = frozen_predicted_edges - frozen_true_edges 

    precision = len(true_frozen_positives)/len(frozen_predicted_edges) if frozen_predicted_edges else 0
    recall = len(true_frozen_positives)/len(frozen_true_edges) if frozen_true_edges else 0
    false_positive_edge_ratio = len(false_frozen_positives) / len(frozen_predicted_edges) if frozen_predicted_edges else 0
    
    
    false_positives = predicted_edges - true_edges  
    false_negatives = true_edges - predicted_edges  

    reversed_edges = {edge[::-1] for edge in predicted_edges} & true_edges

    
    shd = len(false_positives) + len(false_negatives) - len(reversed_edges)
    bic_score=structure_score(model_predicted,test_data,scoring_method='bic')

    # Return metrics as a dictionary
    return {
        "precision": precision,
        "recall": recall,
        "false_positive_edge_ratio": false_positive_edge_ratio,
        "shd": shd,
        "bic-score": bic_score,
        "time": time
    }
     
def visualize_model(model, true_edges, filename):

    model_graphviz = model.to_graphviz()
    predicted_edges = set(model.edges())
    reversed_edges = {edge[::-1] for edge in predicted_edges} & true_edges

    # false positive edges in red
    for edge in predicted_edges:
        if edge not in true_edges and edge[::-1] not in true_edges:
            model_graphviz.get_edge(edge[0], edge[1]).attr['color'] = 'red'
            
    # reversed edges in blue
    for edge in predicted_edges:
        if edge[::-1] in true_edges:
            model_graphviz.get_edge(edge[0], edge[1]).attr['color'] = 'blue'
            model_graphviz.get_edge(edge[0], edge[1]).attr['style'] = 'dashed'
           
    # false negative edges in yellow
    for edge in true_edges:
        if edge not in predicted_edges and edge[::-1] not in predicted_edges:
            model_graphviz.add_edge(edge[0], edge[1])
            model_graphviz.get_edge(edge[0], edge[1]).attr['color'] = 'yellow'
            model_graphviz.get_edge(edge[0], edge[1]).attr['style'] = 'dashed'
           
    model_graphviz.draw(filename, prog="dot")
     

def plot_metrics(metrics,data_dimensions):
    
    metric_names = ["False_Positive_edge_ratios", "precisions", "recalls", "shd", "bic_scores", "execution_times"]
    metric_labels = [
        "False Positive Edge Ratio",
        "Precision",
        "Recall",
        "Structural Hamming Distance (SHD)",
        "BIC Score",
        "Execution Time"
    ]

    _, axes = plt.subplots(2, 3, figsize=(18,10))
    axes = axes.flatten()
    
    for i, metric_name in enumerate(metric_names):
        ax=axes[i]
        # Plot MMHC and H2PC metrics
        ax.plot(data_dimensions, metrics["MMHC"][metric_name], label="MMHC", marker="o")
        ax.plot(data_dimensions, metrics["H2PC"][metric_name], label="H2PC", marker="s")
        ax.set_title(metric_labels[i])
        ax.set_xlabel("Input Data Dimension")
        ax.set_ylabel(metric_labels[i])
        ax.legend()
        ax.grid(True)
    plt.tight_layout()
    plt.show()    


def visualize_and_compare_models(model_h2pc, model_mmhc, true_model,path1,path2,path3):
    
    true_edges=set(true_model.edges())
   
    visualize_model(model_h2pc, true_edges, path1)

    
    visualize_model(model_mmhc, true_edges, path2)

    
    model_graphviz_true = true_model.to_graphviz()
    model_graphviz_true.draw(path3, prog="dot")

    
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))
    fig.suptitle("Bayesian Network Comparison", fontsize=16)

    
    img_h2pc = Image.open(path1)
    axes[0].imshow(img_h2pc)
    axes[0].set_title("H2PC")
    axes[0].axis('off')

    
    img_mmhc = Image.open(path2)
    axes[1].imshow(img_mmhc)
    axes[1].set_title("MMHC")
    axes[1].axis('off')

   
    img_true = Image.open(path3)
    axes[2].imshow(img_true)
    axes[2].set_title("True Model")
    axes[2].axis('off')

    fig.legend(
        handles=[
            plt.Line2D([0], [0], color='red', lw=2, label='Red Edges: Incorrect edges'),
            plt.Line2D([0], [0], color='blue', lw=2, linestyle='dashed', label='Blue Edges: Reversed edges'),
            plt.Line2D([0], [0], color='yellow', lw=2, linestyle='dashed', label='Yellow Edges: Missing edges')
        ],
        loc='lower center', ncol=2, fontsize=12, bbox_to_anchor=(0.5, -0.1)
    )

    # Adjust layout and show the plot
    plt.tight_layout(rect=[0, 0.1, 1, 0.95])
    plt.show()