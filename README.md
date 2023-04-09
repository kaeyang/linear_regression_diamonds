# linear_regression_diamonds

What makes one diamond more expensive than the other? I plan to answer this question using linear regression. Linear regression is a linear approach to modeling the relationship between a response and predictor(s). I applied this modeling process on a Diamond dataset to create a model that infers the price based on the physical properties (predictors) of each diamond. The final model also suggests which predictors are most significant in predicting the price.

We find that the model ‘log(Price) ~ log(Carat) + Color + Depth + Table’ is the best model for determining the price of a diamond. We also consider the two versions of this model to highlight the differences that occur when we keep or discard the influential points found at the beginning of our process. When we exclude the influential data points from our model, we see a reduction in the heteroscedasticity problem of the residuals; however, ultimately, the sample size of this data set is still substantial enough for the statistical tests of the predictors to hold true. For the model containing the influential points, we have an adjusted R-squared of 0.947, and for the model without them, we have an adjusted R-squared of 0.952, meaning that in both cases, the goodness of fit of the model is quite high.
