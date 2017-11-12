import numpy as np
import tensorflow as tf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
#matplotlib inline
plt.rcParams['figure.figsize'] = (10, 6)

#random-ish data
X = np.arange(0.0, 5.0, 0.1)
X

##You can adjust the slope and intercept to verify the changes in the graph
a=-1
b=10

Y= a*X + b 

#plt.plot(X,Y) 
#plt.ylabel('Dependent Variable')
#plt.xlabel('Indepdendent Variable')
#plt.show()

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 3 + 2
# noisey y data
y_data = np.vectorize(lambda y: y + np.random.normal(loc=0.0, scale=0.1))(y_data)

list(zip(x_data,y_data)) [0:5]

# now tensorflow
a = tf.Variable(1.0)
b = tf.Variable(0.2)
y = a * x_data + b

# mean squared error
# Error = y (true) - y-data (noisey)
loss = tf.reduce_mean(tf.square(y - y_data))

# Choosiing descent step
optimizer = tf.train.GradientDescentOptimizer(0.5)
# Minimize loss ^
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

train_data = []
for step in range(100):
    evals = sess.run([train,a,b])[1:]
    if step % 5 == 0:
        print(step, evals)
        train_data.append(evals)
		
converter = plt.colors
cr, cg, cb = (1.0, 1.0, 0.0)
for f in train_data:
    cb += 1.0 / len(train_data)
    cg -= 1.0 / len(train_data)
    if cb > 1.0: cb = 1.0
    if cg < 0.0: cg = 0.0
    [a, b] = f
    f_y = np.vectorize(lambda x: a*x + b)(x_data)
    line = plt.plot(x_data, f_y)
    plt.setp(line, color=(cr,cg,cb))

plt.plot(x_data, y_data, 'ro')

green_line = mpatches.Patch(color='red', label='Data Points')

plt.legend(handles=[green_line])

plt.show()