# Anime-Recommender-System
Animatrix is an anime recommender system that aims to provide anime recommendations through the traditional method of collaborative filtering (CF). The key idea behind CF is that similar users have similar interests and that similar items will also be liked by these same users. Consequently, this method focuses on providing a recommendation based on a user’s past behavior and actions. There are two main types of collaborative filtering: memory-based and model-based; our team has focused on implementing a variation of these types of filters in order to explore the effectiveness and efficiency in providing relevant anime recommendations. Within memory-based algorithms, we implemented neighborhood-based, user-to-user top-N, and item-to-item top-N using multiple similarity measures to compute the similarities between animes and users. In addition, we have also focused on exploring method-based algorithms by attempting to implement Naive Bayes and successfully implementing SVD.

### Directory Organization
- KNN: K-Nearest-Neighbors approach with RMSE and MAE scores
- SVD: Singular-value decomposition approach with adjustments in order to increase RMSE and MAE scores
- TopN: Top-N approach using user-to-user and item-to-item approach with RMSE and MAE scores
