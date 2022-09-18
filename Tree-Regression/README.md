# Regression Tree

This was a final project for my Math of Data Mining and Pattern Recognition course. It basically recovers the information from a MysterImage which has had >99% of its pixels removed at random (i'm guessing a uniform distribution). Luckily, the pixels are distributed randomly throughout the image so we can extrapolate much of the remaining information. We do this by using a regression tree, which much like a decision tree, tries to box the pixels together so that the color differences are minimized, which we quantify with the MSE (mean squared error). Read about the details in "Math_444___Final.pdf"

![Regression](regression_image-3x3.png)

We can see the results based on tree depth above. I think this result was really cool since it shows that most of the visual information of this somewhat complicated structure could be encoded in less than 1% of the pixels. 

## Next Steps:

This is a pretty simple model, but a cool related idea I want to explore is compression based decision trees. It's fairly simple to understand - you just block regions with low MSEs into larger regions. The main challenge of this would be to do the blocking and indexing efficiently. When I find a strech of free time I'm hoping to look into papers on this :D