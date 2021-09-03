## ----global_options, include=FALSE----------------------------------------------------------------------------------------
library(knitr)
# global options
knitr::opts_chunk$set(dpi = 100, 
                      echo=TRUE, 
                      warning=FALSE, message=FALSE, eval = TRUE, 
                      fig.show='hide', fig.width= 7,fig.height= 6,fig.align='center', out.width = '50%', 
                      fig.path= 'Figures/')

show.result = FALSE # change to show solutions
# code chunk for solutions should be: echo = show.result, eval = show.result



## ---- eval = FALSE, message=FALSE-----------------------------------------------------------------------------------------
## if (!requireNamespace("BiocManager", quietly = TRUE))
##     install.packages("BiocManager")
## 
## BiocManager::install.packages('mixOmics')


## ---- results = 'hide'----------------------------------------------------------------------------------------------------
library(mixOmics)
data(srbct)
# The gene expression data
X <- srbct$gene
dim(X)
pca.srbct <- pca(X, ncomp = 10, center = TRUE, scale = TRUE)
pca.srbct
plot(pca.srbct)


## -------------------------------------------------------------------------------------------------------------------------
plotIndiv(pca.srbct, comp = c(1,2), group = srbct$class, ind.names = FALSE,
          legend = TRUE, title = 'SRBCT, PCA comp 1 - 2')


## ----eval = FALSE---------------------------------------------------------------------------------------------------------
## col.srbct = as.numeric(srbct$class)
## plotIndiv(pca.srbct, col = col.srbct,  style = '3d', ind.names = FALSE)


## -------------------------------------------------------------------------------------------------------------------------
plotVar(pca.srbct, cex = 0.9)


## -------------------------------------------------------------------------------------------------------------------------
X <- srbct$gene
Y <- srbct$class
summary(Y)
dim(X)
length(Y) # always check you have the right dimensions


## -------------------------------------------------------------------------------------------------------------------------
srbct.plsda <- plsda(X, Y, ncomp = 3)


## -------------------------------------------------------------------------------------------------------------------------
plotIndiv(srbct.plsda, comp = c(1,2),
          ind.names = FALSE, 
          legend = TRUE, title = 'SRBCT, PLSDA comp 1 - 2')


## -------------------------------------------------------------------------------------------------------------------------
select.keepX = c(50, 40, 30)
splsda.srbct <- splsda(X, Y, ncomp = 3, keepX = select.keepX) 


## -------------------------------------------------------------------------------------------------------------------------
plotIndiv(splsda.srbct, comp = c(1,2),
          ind.names = FALSE, 
          legend = TRUE,
          title = 'SRBCT, sPLSDA comp 1 - 2')


## -------------------------------------------------------------------------------------------------------------------------
plotVar(splsda.srbct, comp = c(1,2), 
        var.names = list(substr(srbct$gene.name[, 2], 1, 5)), cex = 3)


## -------------------------------------------------------------------------------------------------------------------------
plotLoadings(splsda.srbct, comp = 2, method = 'mean', contrib = 'max')


## -------------------------------------------------------------------------------------------------------------------------
# example of performance evaluation code on sPLS-DA
set.seed(34)  # remove the seed for your own study!
perf.splsda <- perf(splsda.srbct, folds = 5, validation = "Mfold", 
                  progressBar = FALSE, nrepeat = 10)


## ---- results = 'hide'----------------------------------------------------------------------------------------------------
# perf.srbct  # lists the different outputs
perf.splsda$error.rate

# error rate per class
perf.splsda$error.rate.class


## ---- fig.show = TRUE-----------------------------------------------------------------------------------------------------
par(mfrow=c(1,2))
#this is for comp 1
plot(perf.splsda$features$stable[[1]], type = 'h', 
     xlab = 'variables selected across CV folds', ylab = 'Stability frequency')
title(main = 'Feature stability for comp = 1')

# for comp2
plot(perf.splsda$features$stable[[2]], type = 'h', 
     xlab = 'variables selected across CV folds', ylab = 'Stability frequency')
title(main = 'Feature stability for comp = 2')
par(mfrow=c(1,1))


## -------------------------------------------------------------------------------------------------------------------------
# just the head of the selectVar output:
head(selectVar(splsda.srbct, comp = 2)$value)
# save the name of selected var + stability from perf:
select.name <- selectVar(splsda.srbct, comp = 2)$name
stability <- perf.splsda$features$stable[[2]][select.name]
# just the head of the stability of the selected var:
head(cbind(selectVar(splsda.srbct, comp = 2)$value, stability))


## ---- eval = FALSE--------------------------------------------------------------------------------------------------------
## # this chunk takes ~ 4-5 min to run, you can skip that part and
## # load the .RData provided instead in RData/
## srbct.plsda <- plsda(X, Y, ncomp = 10)
## perf.srbct.plsda <- perf(srbct.plsda, validation = "Mfold", folds = 5,
##                   progressBar = FALSE, nrepeat = 10)
## # perf.srbct.plsda              #will list the different outputs
## # perf.srbct.plsda$error.rate  #outputs the error rate for each comp and each distance
## 
## #save(perf.srbct.plsda, file = 'RData/SRBCT-perf-PLSDA.RData')


## -------------------------------------------------------------------------------------------------------------------------
# to gain some computing time on the tuning, directly load the data
load('RData/SRBCT-perf-PLSDA.RData')


## -------------------------------------------------------------------------------------------------------------------------
# sd to show the error bars across the repeats
plot(perf.srbct.plsda, overlay = 'measure', sd = TRUE)


## ---- eval = FALSE--------------------------------------------------------------------------------------------------------
## # this chunk takes ~ 6 min to run, load the .RData provided instead.
## # Some convergence issues may arise but it is ok (run on CV)
## 
## # grid of possible keepX values that will be tested for comp 1 and comp 2
## list.keepX <- c(1:10,  seq(20, 100, 10))
## 
## tune.splsda.srbct <- tune.splsda(X, Y, ncomp = 4, validation = 'Mfold', folds = 5,
##                            progressBar = FALSE, dist = 'mahalanobis.dist',
##                           test.keepX = list.keepX, nrepeat = 10)
## 
## # mean error rate across all CV folds and nrepeats
## error <- tune.splsda.srbct$error.rate
## # optimal keepX achieving lowest error rate
## select.keepX <- tune.splsda.srbct$choice.keepX
## 
## #save(error, tune.splsda.srbct, select.keepX, list.keepX, file = 'RData/SRBCT-tune-sPLSDA.RData')


## -------------------------------------------------------------------------------------------------------------------------
# to gain some computing time on the tuning, directly load the data
load('RData/SRBCT-tune-sPLSDA.RData')


## -------------------------------------------------------------------------------------------------------------------------
# just a head of the classif error rate per keepX and comp
head(tune.splsda.srbct$error.rate)


## -------------------------------------------------------------------------------------------------------------------------
# the optimal number of components according to our one-sided t-tests
tune.splsda.srbct$choice.ncomp

#the optimal keepX parameter according to minimal error rate
tune.splsda.srbct$choice.keepX
# argument option to show the optimal keepX values
# sd to show the error bars across the repeats
plot(tune.splsda.srbct, optimal = TRUE, sd = TRUE)


## -------------------------------------------------------------------------------------------------------------------------
# set the seed for reproducibility purposes during this workshop
set.seed(33)
train <- sample(1:nrow(X), 50)    # randomly select 50 samples in the training set
test <- setdiff(1:nrow(X), train) # rest is part of the test set

# store matrices into training and test set:
X.train <- X[train, ]
X.test <- X[test,]
Y.train <- Y[train]
Y.test <- Y[test]

# check dimensions are OK:
dim(X.train)
dim(X.test)


## -------------------------------------------------------------------------------------------------------------------------
splsda.srbct.train <- splsda(X.train, Y.train, ncomp = 3, keepX = c(20,30,40))


## -------------------------------------------------------------------------------------------------------------------------
splsda.srbct.predict <- predict(splsda.srbct.train, X.test,
                       dist = "mahalanobis.dist")


## -------------------------------------------------------------------------------------------------------------------------
# just the head:
head(data.frame(splsda.srbct.predict$class, Truth = Y.test))
# compare prediction on the third component
table(splsda.srbct.predict$class$mahalanobis.dist[,3], Y.test)


## -------------------------------------------------------------------------------------------------------------------------
#On component 4, just the head:
head(splsda.srbct.predict$predict[, , 3])

