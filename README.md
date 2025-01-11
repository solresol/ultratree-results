# ultratree-results
This shows the results of the ultrametric tree-based, explainable, solar-powered language model

These charts update each day.

## Total Loss

![Total Loss vs Model Size](total_loss_vs_model_size.png)

![Total Loss vs Model Size for Sense Annotated Models Including Ensembling](total_loss_vs_model_size_with_ensemble.png)

![Total Loss vs Model Size for the Careful 10000 model](careful10000_loss_vs_size.png)

## Noun Loss

Instead of looking at the total loss over all parts of speech, we would expect that nouns would get the most benefit from
having sense annotation into a hierarchy.

![Noun Loss vs Model Size](noun_loss_vs_model_size.png)

![Noun Loss vs Model Size for Sense Annotated Models Including Ensembling](noun_loss_vs_model_size_with_ensemble.png)

![Noun Loss vs Model Size for the Careful 10000 model](careful10000_noun_loss_vs_size.png)

## Time Views

![Total Loss vs Time](total_loss_vs_time.png)

![Noun Loss vs Time](noun_loss_vs_time.png)

![Model Node Count vs Time](model_node_count_vs_time.png)

## Neural Network

This plot shows the Total Loss vs Model Parameter Count for different augmentations of neural network models, together with a sample sense annotated, and unannotated model for comparison.

To-do: if the ensemble looks good, add it to the chart

![Neural Network Results](neural-results.png)


## Model Complexity

![Average Depth vs Time](average_depth_vs_time.png)

![Average In-Region Hits vs Time](average_in_region_hits_vs_time.png)

## Context Usage

![Sense Annotated](sense-annotated1-context-usage.png)

![Unannotated](unannotated-context-usage.png)


# How to reproduce these results

## Download the TinyStories data set, and sense-annotate some of it

Clone `github.com:solresol/wordnetify-tinystories.git` 

Follow the instructions in the README.md there.

I stored the sense-annotated training data in `/tinystories/wordnetify-tinystories/TinyStories.sqlite` and the sense-annotated validation data in `/tinystories/wordnetify/w2.sqlite`

## Make an ultrametric tree model

Clone `github.com:solresol/ultrametric-trees` and follow the instructions
in README.md there, including running the `cronscript.sh` to export results.

I stored the prepared data (and did training) in
`/ultratree/language-model/tiny.sqlite` and the the validation data
in `/ultratree/language-model/validation.sqlite`

## Make a baseline comparison

Clone `github.com:solresol/ultratree-neural-baseline` and follow the
instructions in the README.md file there.




