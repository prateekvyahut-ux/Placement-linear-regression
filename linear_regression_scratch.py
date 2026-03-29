
  class meraLR():
    def _init_(self):
      self.m=None
      self.b=None
    def fit(self,X_train,y_train):
        num=0
        den=0
        for i in range(X_train.shape[0]):
              X_mean=X_train.mean()
              y_mean=y_train.mean()
              num=num+((X_train[i]-X_mean)*(y_train[i]-y_mean))
              den=den+((X_train[i]-X_mean)*(X_train[i]-X_mean))
              self.m=num/den
              self.b=y_mean-(self.m*X_mean)
   def predict(self,X_test):
        return self.m*X_test+self.b
           