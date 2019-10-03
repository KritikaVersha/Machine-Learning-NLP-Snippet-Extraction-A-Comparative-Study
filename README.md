# Machine-Learning-NLP-Snippet-Extraction-A-Comparative-Study

In this project we aim to implement using Labeled LDA to solve the problem of Credit Attribution
in multi-labeled corpora.

A plethora of blogging, news and data websites like Reuters, del.icio.us, Flickr and Tumblr have
widely useful articles labeled with multiple user-provided tags. However not every part of the document
represents every tag equally. There are some parts of the document that focus on a particular
tag more than the others. That is, there is no uniform Credit Attribution in a corpora. This poses
an avenue to develop a better search system at an intra-document level. The users browsing the
documents looking for a particular tag might prefer to look at the most relevant part of the document
related to the tag. In other words they would prefer to look at a snippet of the document whose
’specificity’ to that particular topic is higher than the rest of the document.
This immediately gives rise to an application resulting from an approached solution to the above
described problem of Credit Attribution - Snippet Extraction. This would enable a user searching
for a particular label to view relevant portions of the document(to his label) without having to scan
the entire document, thus improving his efficiency and the better utilization of existing data.
The main method described in the paper [2], implemented here is an extention of the Latent Dirichlet
Allocation (LDA) [3], Labeled-LDA. We have also implemented methods based on Hidden Markov
Model and compared the results of L-LDA to it.
