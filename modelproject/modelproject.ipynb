{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# **Project 2: Model Analysis Project**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**By Christian Hjorth Hansen and Jacob Mai Kaaber**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Introduction**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In this project we consider the consumer's choice problem with two goods and the firms maximization problem. We start by solving the consumer's problem for 2 different consumers, one with Cobb-Douglas preferences and the other with logarithmic preferences. Next, we find the social optimum for the two consumers. Lastly, we solve the firms maximization problem, where the reader can choose between the settings of a competitive market or a monopolistic market. This project is made as an interactive helping tool, such that the user can adjust the parameters to the user's function."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Importing necessary tools**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We start by importing the tools, which we are going to use in this project."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import ipywidgets as widgets #For making widgets for the income and prices\n",
    "import matplotlib.pyplot as plt # For making plots\n",
    "from mpl_toolkits.mplot3d import Axes3D # This addition allows us to make 3D-plots\n",
    "import numpy as np # This is used, when we make graphs\n",
    "from scipy import optimize # This is used for solving the consumer's problem\n",
    "import warnings # We import this feature because we want to avoid printing a warning when dividing by 0\n",
    "warnings.filterwarnings(\"ignore\", category=RuntimeWarning) "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Consumer problems**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Setting the prices**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We solve the consumer problems for both consumers simultaniosly. The consumer on the left will be the one with cobb-douglas preferences and the one on the rigth is the consumer with the logarithmic preferences."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We start by implementing the two prices as widgets. There are two widgets for each variable. These are connected and will move simultaniosly, allowing for either setting the variables using the slider or writing a specific value using the text-widget."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mPrice on good 1 (P1)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "dd5da20007094b2ca9ddff0fb2cdc443",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=5.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "046f29c729934c229029b36ec2fd5bff",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=5.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mPrice on good 2 (P2)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "33dee84196d44f938a0d9413831be367",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=15.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2717389e44fe4de7ace4020070dc7b65",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=5.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Price on good 1\n",
    "\n",
    "# We only describe the code for the prices, as it is repeated for all variables.\n",
    "# First we print a headline \"Price on good 1\", where the first part is used to make the text bold. We also write P1 in a parenthesis,\n",
    "# as this is the variable name which we are going to use.\n",
    "print('\\033[1m' + 'Price on good 1 (P1)')\n",
    "# Now we create the text-widget, where we set the starting value to 5.\n",
    "P1 = widgets.FloatText(\n",
    "value=5)\n",
    "# Next we create a slide-widget (using floats, such that decimals can be used). Here we set the same starting value, \n",
    "# we set the steps to 1 and we define the minimum value to 0 and the maximum value to 100.\n",
    "# This can off course be adjusted for the problem settings.\n",
    "P1b = widgets.FloatSlider(\n",
    "value=5,\n",
    "step=1,\n",
    "min=0,\n",
    "max=100.0,)\n",
    "# Next we print both widgets\n",
    "display(P1,P1b)\n",
    "# And lastly we link the 2 widgets together, so you can change either widget.\n",
    "linkp1 = widgets.jslink((P1, 'value'), (P1b, 'value'))\n",
    "\n",
    "# Price on good 2\n",
    "print('\\033[1m' + 'Price on good 2 (P2)')\n",
    "P2 = widgets.FloatText(\n",
    "value=15)\n",
    "P2b = widgets.FloatSlider(\n",
    "value=5,\n",
    "step=1,\n",
    "min=0,\n",
    "max=100.0,)\n",
    "display(P2,P2b)\n",
    "\n",
    "linkp2 = widgets.jslink((P2, 'value'), (P2b, 'value'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Setting the income level**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mIncome for consumer 1 (I1)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f74740eacafe471eb73b6646b8740485",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=100.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8cbfa49314b344e6bb6f7984102b0a15",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=100.0, max=1000.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mIncome for consumer 2 (I2)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1a3e0796e95f43409997912eefe9cd6d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=100.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1ab188fee7c643128eb3260d455f74f2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=100.0, max=1000.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Income consumer 1\n",
    "print('\\033[1m' + 'Income for consumer 1 (I1)')\n",
    "I1 = widgets.FloatText(\n",
    "value=100)\n",
    "I1b = widgets.FloatSlider(\n",
    "value=100,\n",
    "step=1,\n",
    "min=0,\n",
    "max=1000,)\n",
    "display(I1,I1b),\n",
    "\n",
    "linkI1 = widgets.jslink((I1, 'value'), (I1b, 'value'))\n",
    "             \n",
    "# Income consumer 2\n",
    "print('\\033[1m' + 'Income for consumer 2 (I2)')\n",
    "I2 = widgets.FloatText(\n",
    "value=100)\n",
    "I2b = widgets.FloatSlider(\n",
    "value=100,\n",
    "step=1,\n",
    "min=0,\n",
    "max=1000,)\n",
    "display(I2,I2b)\n",
    "\n",
    "linkI2 = widgets.jslink((I2, 'value'), (I2b, 'value'))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next we plot the budget constraint, this way we are able to show, what the consumer is able to afford. To do this we first need to define the budget constraint function, whicch is\n",
    "\\\\[\n",
    "\\begin{eqnarray*}\n",
    "I(p_{1},p_{2}) & = & x_{1}*p_{1}+x_{2}*p_{2}\n",
    "\\end{eqnarray*}\n",
    "\\\\]\n",
    "And then isolate for \\begin{eqnarray*} x_{2} \\end{eqnarray*}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA3QAAAFOCAYAAADO7l9ZAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDMuMC4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvOIA7rQAAIABJREFUeJzt3X20bHldHvjna18Qm0Ze7Is2NIKIQSVZAnPFJBCmw5s0UTCGGMgkIhI7LkMGJjpKFkqI0cnojEY0xqQFBAxRDEJEBJWlAmNWaLyNLS82SEPodEvT3JbXRl4C/uaPvQ9d99Q+71W7ald9PmvVulWnqs7+nX3r1nOfb+2qU621AAAAMD1fsOoFAAAAcDwKHQAAwEQpdAAAABOl0AEAAEyUQgcAADBRCh0AAMBEKXScWFW9vqr+0arXsa6q6rVV9ZQFfr+/XVU3VNWtVfWgRX1fABZPRu5PRsLJKXRbqKreV1Wf7J/sPlxVv1FV91qDdX1HVf3+qtcxq6paVd3vJN+jtXZ5a+3Fh9zeYYL//03y9NbaRa21PzzJ2ma2+41V9caq+nhVnauqN1TV4xfxvaegqv5yVf1WVd1SVX45J2wxGXl4MnI7VNVTqurqqvpYVd1YVT9eVadWvS5uo9Btr29urV2U5JIkNyf5mRWvZ5JW9IR27yTvOM4dq+qCga89Mcl/TvKSJJcm+dIkz0nyzSdY49ra4+/sfyb5lSRPG3k5wHqSkQsgI6dnj7+zC5M8M8nFSb4hySOTfN+Y6+IArTWnLTsleV+SR81cflySP5m5/Pok/2jm8nck+f2Zy49O8s4kH03yb5O8Yef2SS5I8hNJbkny35M8PUlLcqq//s5JXpDkpiR/muRH+vt8TZJPJflckluTfGSPtd8tyS8keX+SDyf5LzPXfVeS65J8KMmrktxj5rqW5LuTvLu/388mqf66+/U/w0f7db+s//ob+/t9ol/T30tyWZIbk/xAkg8k+cUkd03y6iTn+u/96iSXDu3PnX2ZboL44X4fXd5f96P9z/+pfnv/dtfP/oX913fW9J7+61/Tb+Mj6ULs8TP3eVGSn0vymv4+j9r1PSvJ/0jyf+7zePmCJD+Y5PokH0wXanfur7tPv56n9N/nliTPnrnvQ5KcTfKxdP8p+sn+65cluXGvx2WS56YL0P+Y5ONJ3pbkLyX55/0abkjymJn7Dj6uZvb5f03yb9I9Nn5kn5/1fknaqv+NOjk5re4UGSkjb7teRg7/zP8sya+v+t+q020nr9Btuaq6MN2T8JsOefuLk/xquievi5O8J8lDZ27yXUkuT/LAJA9O8i27vsWLk3w2XUA8KMlj0j2RX5suTP5b6w6TuMseS/jFdJOiByS5e7onoFTVI5L86yTflm6ien2SX951329K8vVJvq6/3Tf2X/9XSX47Xehcmn4S21p7eH/91/Vrell/+cvShea9k1yR7sn8F/rLX57kk+lCfC/fkORd6fbfjyd5QVVVa+3ZSf6/3HaoyNNn79Ra+3TrJsY7a/rKqrpdkl/v13/3JP80yUur6v4zd/376YLwTumCctb9k9wrycv3We939Ke/meS+SS4a+Pke1n+vRyZ5TlV9Tf/15yV5Xmvti5N8ZbpXwQ7rm3Pbfwb+MMlvpdvX90zyw0n+w8xtBx9XM9d/Q5L3pttHP3qENQBbTEYmkZEyct7Dc8xXQVmSVTdKp/FP6aY8t6abVn023STvr8xc//rsMX1M8u1J3jRzXaWbxu1M1343yT+euf5R6aeP6Q5T+HSSL5q5/slJfm/3dvZY9yVJ/iLJXQeue0GSH5+5fFG6w+ju019uSR42c/2vJHlWf/4lSa7MzMRw5nYtyf1mLl+W5DNJ7rDPOh+Y5MND+7P/Ga+bue7CfhtfNrTv9/j+n19Tkr+Rbgr6BTPX/1KS5/bnX5TkJft8r4f232+/n+d3knzPzOX79/v2VG6bPs5OW9+c5En9+Tcm+ZdJLt71PS/LwdPH181c983pHrM7E8U79du9yyEfV//jkP82vELn5LTlp8jIREbu3FZGzv+8T033mL74sPdxWv7JK3Tb61taN+H7wnSHfLyhqr7sEPe7R7qX8pP0//Odubz7+l3n753kdkluqqqPVNVH0k2Q7n7INd8ryYdaax/eY13Xz6zr1iR/lm5SteMDM+f/PF2gJcn3pwvdN1fVO6rqOw9Yx7nW2qd2LlTVhVX1H6rq+qr6WLon6LsMHYu/ex2ttT/vz160x20Pco8kN7TW/mLma9fn/J/7huztz/o/LzlgG9fPXL4+t/3nY8de+/Zp6Q4DeWdV/UFVfdM+29nt5pnzn0xyS2vtczOX02/nMI+r/fYBwG4yUkYmMvI8VfUtSf7vdIfB3nKEtbJkCt2Wa619rrX2inTHpT+s//In0k3FdsyG2E3pQiNJUlU1e7m//tKZy7PX3ZBuSnRxa+0u/emLW2sP2FnOAcu9IcndqmroUJP3p3vS2lnXHZN8SbpjxffVWvtAa+27Wmv3SPKPk/y7Az61a/c6vzfdRO4bWnfYxM5hKHXQtg/xvQ/y/iT3qqrZf8tfnvN/7v2+57vS7de/c8A27j1z+cvTTa1vHr75zIZbe3dr7cnpguPHkry8/7s57zHWB/vpg77fHg56XCVH368AMjIyMjJyZw2PTfLz6T4w6G3HXAtLotBtueo8Id0x2Nf2X74mybf2U7X75fxP/vuNJA+oqm/tPwnpf8/5YfYrSZ5RVffsQ+UHdq5ord2U7jj2n6iqL66qL6iqr6yq/7W/yc1JLq2q2w+ttb//a9OFyV2r6nZVtRMM/ynJU6vqgVX1hUn+ryRXtdbed4h98HeraidgP5zuiW1nynVzumPi93OndNOwj1TV3ZL8i4O2uY/DbG/WVeme+L+/3x+XpTv0Yvd7Iwb10+N/luSHquqpM38vD6uqK/ub/VKS/6OqvqKqLkq3b1/WWvvsQd+/qv5BVZ3up6Mf6b/8uSR/kuQOVfW3+vc4/GC6SfiRHeJxdaD+38Edkty+v3yH/nEEbDEZKSMjI3feg/nSJH+ntfbm46yD5VLottevV9Wt6T5Z6UeTPKW1tvMG13+T7hj4m9O9kfalO3fqX2L/u+lecv+zJF+V7tORdvx8uieOt6Z7k+5r0k2qdp78vz3df5r/OF0wvDy3Hcrwu+neZPuBqtrrpfx/mO7Y9Hem+ySnZ/br+p0kP5Tuzeg3pXtz8ZMOuS++PslV/f54VZJntNb+e3/dc5O8uD9M4dv2uP9PJfmidJ9e9aYkv3nI7Q55XpInVve7j376oBu31j6T5PHp3mR/S5J/l+TbW2vvPOwGW2svT/em/+9MN2m8Od0nYP1af5MXpnvj9RvTfeLYp9K9sfwwHpvkHf2+fV669w18qrX20STfk+T56Saln0h3TP5x7fe4Oox7p/sPx86/gU+mm8wC20lG3kZGysgfSvdJma+p7vcz3lpVrz3BeliwnY+khaWoqsuT/PvW2r0PvDEAbBEZCSyCV+hYqKr6oqp6XFWdqqp7pju04pWrXhcArJqMBJZh6YWuqu5fVdfMnD5WVc9c9nZZmUr3EbwfTnc4ybVJnrPSFQGsIfm4lWQksHCjHnJZ3af0/Gm6Tzq6/qDbA8A2kI8AHNfYh1w+Msl7hBUAnEc+AnAsp0be3pPSfbzrearqiiRXJMkd73jH/+Wrv/qrR14WAKtw9dVX39JaO+7vV9okg/mYyEiAbXSUfBztkMv+96a8P8kDWmt7/rLFM2fOtLNnz46yJgBWq6qubq2dWfU6Vumw+ZjISIBtcZR8HPOQy8uTvOWgsAKALSMfATi2MQvdk7PH4SQAsMXkIwDHNkqhq6oLkzw6ySvG2B4ATIF8BOCkRvlQlNbanyf5kjG2BQBTIR8BOKmxf20BAAAAC6LQAQAATJRCBwAAMFEKHQAAwEQpdAAAABO1kYWuqjsBALeRjwCbZ+MK3WxQCS0AmKfYAWyOjSt0rZ1/WWABwDAZCTB9G1fokuFSJ7QA2Ha78zGRjwBTt5GFLhFaADCkNYNPgE2ysYUuEVoAsBeDT4DNsNGFbofQAoB5Bp8A07cVhS7ZO7QAYNsZfAJM19YUuh0mkQAwT6kDmKatK3SJ0AKAIQ7BBJierSx0idACgL0YfAJMx9YWuh1CCwDmGXwCTMPWF7rEB6YAwF4MPgHWm0I3wyQSAOYpdQDrS6HbRWgBwDyHYAKsJ4VugNACgGEGnwDrRaHbh9ACgHkGnwDrQ6E7gFIHAMNkJMDqKXSHYBIJAMOUOoDVUuiOQGgBwDyDT4DVUeiOSGgBwDCDT4DxKXTHJLQAYJ7BJ8C4FLoTUOoAYJiMBBjHKIWuqu5SVS+vqndW1bVV9dfG2O4YTCIBOK5NzsdEqQMYw6mRtvO8JL/ZWntiVd0+yYUjbXc0rc2HVNVwmAFAbyvyMTk/I3fOy0iAk1t6oauqL07y8CTfkSSttc8k+cyyt7sKQguAw9qmfEwMPgGWZYxDLu+b5FySX6iqP6yq51fVHWdvUFVXVNXZqjp77ty5EZa0XA4xAeAQDszHZLMy0tsUABZvjEJ3KsmDk/xca+1BST6R5FmzN2itXdlaO9NaO3P69OkRlrR8Sh0ABzgwHxMZCcD+xih0Nya5sbV2VX/55ekCbOOZRAKwj63Nx0SpA1iUpRe61toHktxQVffvv/TIJH+87O2uE6EFwG7y0eATYBHG+pTLf5rkpf0neL03yVNH2u7a8IEpAAzY+nxMfGAKwEmMUuhaa9ckOTPGttad0AJgh3y8jcEnwPGM8ovFOZ9DMAFgmIwEOBqFbkW8bwAAhil1AIen0K2Y0AKAeQafAIej0K0BoQUAwww+Afan0K0RoQUA8ww+Afam0K0ZpQ4AhslIgHkK3RoyiQSAYUodwPkUujUmtABgnsEnwG0UujUntABgmMEngEI3GUILAOYZfALbTqGbEKUOAIbJSGBbKXQTYxIJAMOUOmAbKXQTJbQAYJ7BJ7BtFLoJE1oAMMzgE9gWCt0GEFoAMM/gE9gGCt2GUOoAYJiMBDaZQrdBTCIBYJhSB2wqhW4DCS0AmGfwCWwihW5DCS0AGGbwCWwShW7DCS0AmGfwCWwKhW4LKHUAMExGAlOn0G0Jk0gAGKbUAVOm0G0ZoQUA8ww+galS6LaQ0AKAYQafwNQodFtMaAHAPINPYEoUui2n1AHAMBkJTIFCh0kkAOxBqQPWnULH5wktAJhn8Amss1NjbKSq3pfk40k+l+SzrbUzY2yXo9sJrNmQ2jk/VPgAOD75OC2tzZe4KvkIrNYoha73N1trt4y4PU5AaAGMRj5OiMEnsG4ccsmeHIIJAMNkJLAuxip0LclvV9XVVXXF7iur6oqqOltVZ8+dOzfSkjgM7xsAWKp98zGRketMqQPWwViF7qGttQcnuTzJP6mqh89e2Vq7srV2prV25vTp0yMtiaMQWgBLsW8+JjJy3Rl8Aqs2SqFrrb2///ODSV6Z5CFjbJfFEloAiyUfN4fBJ7AqSy90VXXHqrrTzvkkj0ny9mVvl+URWgAnJx83j8EnsApjfMrllyZ5ZXXPZqeS/KfW2m+OsF2WyKdgApyYfNxQMhIY09ILXWvtvUm+btnbYXw+uhng+OTjZlPqgLH4tQWcmEMwAWCeQzCBMSh0LITQAoBhBp/AMil0LJTQAoB5Bp/Asih0LJxSBwDDZCSwaAodS2ESCQDDlDpgkRQ6lkpoAcA8g09gURQ6lk5oAcAwg0/gpBQ6RiO0AGCewSdwEgodo1LqAGCYjASOQ6FjdCaRADBMqQOOSqFjZYQWAMwz+ASOQqFjpYQWAAwz+AQOQ6FjLQgtAJhn8AkcRKFjbSh1ADBMRgJ7UehYKyaRADBMqQOGKHSsJaEFAPMMPoHdFDrWltACgGEGn8AOhY61J7QAYJ7BJ5AodEyEUgcAw2QkbDeFjskwiQSAYUodbC+FjskRWgAwz+ATtpNCxyQJLQAYZvAJ20WhY9KEFgDMM/iE7aHQMXlKHQAMk5Gw+RQ6NoJJJAAMU+pgsyl0bBShBQDzDD5hcyl0bByhBQDDDD5h8yh0bCyhBQDzDD5hs4xW6Krqgqr6w6p69VjbBKUOWHfykVWRkbAZxnyF7hlJrh1xe5DEJBJYe/KRlVHqYPpGKXRVdWmSv5Xk+WNsD4YILWDdyEfWgcEnTNtYr9D9VJLvT/IXQ1dW1RVVdbaqzp47d26kJbGNhBawZvbNx0RGMh6DT5impRe6qvqmJB9srV29121aa1e21s601s6cPn162UsCoQWs3GHyMZGRjMvgE6ZnjFfoHprk8VX1viS/nOQRVfUfR9gu7EupA1ZMPrK2ZCRMx9ILXWvtn7fWLm2t3SfJk5L8bmvtHyx7u3AYJpHAqshH1p1SB9Pg99BBhBYADDH4hPV3asyNtdZen+T1Y24TDmsnsGZDauf8UOEDWBT5yLprbb7EVclHWAdeoYNdvFoHAPO8WgfrSaGDAUodAAyTkbBeFDrYg0kkAAxT6mB9KHRwAKEFAPMMPmE9KHRwCEILAIYZfMJqKXRwBEILAOYZfMLqKHRwREodAAyTkTA+hQ6OwSQSAIYpdTAuhQ5OQGgBwDyDTxiPQgcnJLQAYJjBJyyfQgcLIrQAYJ7BJyyXQgcLpNQBwDAZCcuh0MGCmUQCwDClDhZPoYMlEVoAMM/gExZLoYMlEloAMMzgExZDoYMRCC0AmGfwCSd36EJXVY+uqp+vqgf2l69Y3rJg8yh1sLlkJJyMjITjO3WE235Pkqcm+cGquluSBy5nSbC5dgJrNqR2zg+FGTAZMhJOqLX5ElclH+EgRznk8lxr7SOtte9L8pgkX7+kNcHGM4mEjSMjYQEcgglHd5RC9xs7Z1prz0ryksUvB7aH0IKNIiNhgQw+4fAOLHRV9VNVVa21X5v9emvtZ5a3LNgeQgumS0bC8hh8wuEc5hW6W5O8qqouTJKqekxV/dflLgu2i1IHkyUjYclkJOzvwA9Faa39YFX9/SRvqKpPJ/lEkmctfWWwZXxgCkyPjIRx+MAU2NuBha6qHpnku9KF1CVJntZae9eyFwbbSmjBdMhIGI/BJww7zCGXz07yQ621y5I8McnLquoRS10VbDnvG4DJkJEwModgwvkOc8jlI2bOv62qLk/yq0n++jIXBni1DtadjITV8God3OYov7YgSdJauynJI5ewFmCASSRMh4yEcclIOEahS5LW2icXvRBgbw7BhOmQkTAupY5td6xCdxRVdYeqenNV/VFVvaOq/uWytwmbSmjB5pCPsDgGn2yzA99DtwCfTvKI1tqtVXW7JL9fVa9trb1phG3DxvG+AdgY8hEWzHvP2UZLL3SttZbuF68mye36k39WcEJCC6ZNPsJyGHyybZZ+yGWSVNUFVXVNkg8meV1r7apd119RVWer6uy5c+fGWBJsBIdgwrQdlI/9bWQkHIOMZFuMUuhaa59rrT0wyaVJHlJVf3nX9Ve21s601s6cPn16jCXBxvC+AZiug/Kxv42MhGNS6tgGoxS6Ha21jyR5fZLHjrld2AZCC6ZLPsLyGHyy6cb4lMvTVXWX/vwXJXlUkncue7uwjYQWTId8hHEZfLKpxviUy0uSvLiqLkhXIH+ltfbqEbYLW8sHpsAkyEcYmQ9MYRON8SmXb03yoGVvBzifUgfrTT7C6shINsmo76EDxuUQTAAY5hBMNoVCB1tAaAHAPINPNoFCB1tCaAHAMINPpkyhgy0jtABgnsEnU6XQwRZS6gBgmIxkahQ62FImkQAwTKljShQ62HJCCwDmGXwyFQodILQAYA8Gn6w7hQ74PKEFAPMMPllnCh1wHqUOAIbJSNaRQgfMMYkEgGFKHetGoQP2JLQAYJ7BJ+tEoQP2JbQAYJjBJ+tAoQMORWgBwDyDT1ZNoQMOTakDgGEyklVR6IAjMYkEgGFKHaug0AHHIrQAYJ7BJ2NT6IBjE1oAMMzgk7EodMCJCS0AmGfwyRgUOmAhlDoAGCYjWSaFDlgYk0gAGKbUsSwKHbBwQgsA5hl8sgwKHbAUQgsAhhl8skgKHbBUQgsA5hl8sigKHbB0Sh0ADJORnJRCB4zCJBIAhil1nIRCB4xKaAHAPINPjkuhA0YntABgmMEnR6XQASsjtABgnsEnR7H0QldV96qq36uqa6vqHVX1jGVvE5gOpY5tJR+Bg8hIDuPUCNv4bJLvba29parulOTqqnpda+2PR9g2MAE7gTUbUjvnh8IMNoR8BA7U2nyJq5KP3Gbpr9C11m5qrb2lP//xJNcmueeytwtMj0kk20Q+AoflEEz2M+p76KrqPkkelOSqXV+/oqrOVtXZc+fOjbkkYM0ILbbRXvnYXycjgSQGnwwbrdBV1UVJfjXJM1trH5u9rrV2ZWvtTGvtzOnTp8daErDGhBbbYr98TGQkcD6DT3YbpdBV1e3ShdVLW2uvGGObwPQpdWw6+Qgcl4xkxxifcllJXpDk2tbaTy57e8BmMYlkU8lH4KSUOpJxXqF7aJJ/mOQRVXVNf3rcCNsFNojQYgPJR+DEDD5Z+q8taK39fhIPKeDE/HoDNol8BBbJrzfYXqN+yiXAIni1DgDmebVuOyl0wCQpdQAwTEZuF4UOmCyTSAAYptRtD4UOmDyhBQDzDD63g0IHbAShBQDDDD43m0IHbBShBQDzDD43l0IHbBylDgCGycjNo9ABG8kkEgCGKXWbRaEDNprQAoB5Bp+bQ6EDNp7QAoBhBp/Tp9ABW0NoAcA8g89pU+iAraLUAcAwGTlNCh2wdUwiAWCYUjc9Ch2wtYQWAMwz+JwWhQ7YakILAIYZfE6DQgcQoQUAQww+159CB9BT6gBgmIxcXwodwAyTSAAYptStJ4UOYIDQAoB5Bp/rR6ED2IPQAoBhBp/rQ6EDOIDQAoB5Bp/rQaEDOASlDgCGycjVUugADskkEgCGKXWro9ABHJHQAoB5Bp+rodABHIPQAoBhBp/jUugATkBoAcA8g8/xKHQAJ6TUAcAwGbl8Ch3AAphEAsAwpW65ll7oquqFVfXBqnr7srcFsGpCi6OQkcC2MPhcnjFeoXtRkseOsB2AtSC0OIIXRUYCW8Tgc/GWXuhaa29M8qFlbwdg3QgtDiIjgW1k8LlYa/Eeuqq6oqrOVtXZc+fOrXo5AAuj1HFSMhLYVDJyMdai0LXWrmytnWmtnTl9+vSqlwOwUCaRnISMBDaZUndya1HoALaB0AKAeQafJ6PQAYxIaAHAMIPP4xnj1xb8UpL/luT+VXVjVT1t2dsEWHdCi0RGAuxm8Hl0p5a9gdbak5e9DYApam0+oKqGyx6bSUYCDJORh+eQS4AVMokEgGGOZjkchQ5gDQgtAJhn8HkwhQ5gTQgtABhm8Lk3hQ5gzQgtAJhn8DlMoQNYQ0odAAyTkedT6ADWlEkkAAxT6m6j0AGsOaEFAPMMPjsKHcAECC0AGLbtg0+FDmBCtj20AGDINg8+FTqAiVHqAGDYNmakQgcwQds8iQSA/WxbqVPoACZs20ILAA5jmwafCh3AxG1TaAHAUWzD4FOhA9gQ2xBaAHBUmz74VOgANohSBwDDNjUjFTqADbPpk0gAOK5NLHUKHcCG2sTQAoCT2rTBp0IHsME2LbQAYFE2ZfCp0AFsgU0JLQBYpE0YfCp0AFtCqQOAYVPOSIUOYItswiQSAJZhqqVOoQPYQlMNLQBYpikOPhU6gC01xdACgDFMafCp0AFsuSmFFgCMZSqDT4UOAKUOAPaw7hmp0AGQZDqTSAAY2zqXOoUOgPOsc2gBwKqs6+BToQNgzrqGFgCs2roNPkcpdFX12Kp6V1VdV1XPGmObAJzcuoXWppGPANO0ToPPpRe6qrogyc8muTzJ1yZ5clV97bK3C8BiKHXLIR8Bpm8dMnKMV+gekuS61tp7W2ufSfLLSZ4wwnYBWJC9JpGciHwE2ACrLnVjFLp7Jrlh5vKN/dc+r6quqKqzVXX23LlzIywJgOMYCi2O7cB8TGQkwBTsHnyOmZdjFLqhfnrej9hau7K1dqa1dub06dMjLAmA49oJLeXuxA7Mx0RGAkzJKvJxjEJ3Y5J7zVy+NMn7R9guAKwz+QjAiY1R6P4gyVdV1VdU1e2TPCnJq0bYLgCsM/kIwImdWvYGWmufraqnJ/mtJBckeWFr7R3L3i4ArDP5CMAiLL3QJUlr7TVJXjPGtgBgKuQjACc1yi8WBwAAYPEUOgAAgIlS6AAAACZKoQMAAJgohQ4AAGCiFDoAAICJqtbaqtdwnqo6l+T6BXyri5PcsoDvMwZrXY4prTWZ1nqtdTmmtNZkMeu9d2vt9CIWsw0WlJFTepxNaa3JtNZrrcsxpbUm01rvtq310Pm4doVuUarqbGvtzKrXcRjWuhxTWmsyrfVa63JMaa3J9NZLZ0p/b1NaazKt9Vrrckxprcm01mute3PIJQAAwEQpdAAAABO1yYXuylUv4AisdTmmtNZkWuu11uWY0lqT6a2XzpT+3qa01mRa67XW5ZjSWpNprdda97Cx76EDAADYdJv8Ch0AAMBGU+gAAAAmatKFrqoeW1XvqqrrqupZA9d/YVW9rL/+qqq6z/ir/Pxa7lVVv1dV11bVO6rqGQO3uayqPlpV1/Sn56xirf1a3ldVb+vXcXbg+qqqn+737Vur6sErWuf9Z/bXNVX1sap65q7brHS/VtULq+qDVfX2ma/drapeV1Xv7v+86x73fUp/m3dX1VNWtNb/p6re2f89v7Kq7rLHffd9zIy01udW1Z/O/F0/bo/77vvcMdJaXzazzvdV1TV73Hfs/Tr4XLWuj1n2NpWMnFo+9uuRkYtZn3wcd70y8uRrXc+MbK1N8pTkgiTvSXLfJLdP8kdJvnbXbb4nyb/vzz8pyctWuN5Lkjy4P3+nJH8ysN7Lkrx61fu2X8v7kly8z/WPS/LaJJXkrya5ag3WfEGSD6T7RYxrs1+TPDzJg5O8feZrP57kWf35ZyX5sYH73S3Je/s/79qfv+sK1vqYJKf68z82tNbDPGZGWutzk3zfIR4n+z53jLHWXdf/RJLnrMl+HXyuWtfHrNOef4+Tycip5WO/Hhm5mDXJx3HXKyNPvta1zMgpv0L1hiYrAAAFoUlEQVT3kCTXtdbe21r7TJJfTvKEXbd5QpIX9+dfnuSRVVUjrvHzWms3tdbe0p//eJJrk9xzFWtZkCckeUnrvCnJXarqkhWv6ZFJ3tNau37F6zhPa+2NST6068uzj80XJ/mWgbt+Y5LXtdY+1Fr7cJLXJXns0haa4bW21n67tfbZ/uKbkly6zDUc1h779TAO89yxUPuttX9O+rYkv7TMNRzWPs9Va/mYZU+TycgNzMdERh6KfFweGbkc65qRUy5090xyw8zlGzMfAJ+/Tf8P7qNJvmSU1e2jP6zlQUmuGrj6r1XVH1XVa6vqAaMu7HwtyW9X1dVVdcXA9YfZ/2N7Uvb+B78u+3XHl7bWbkq6J4ckdx+4zTru4+9MN3UectBjZixP7w9/eeEehzys2379G0lubq29e4/rV7Zfdz1XTfUxu60mmZETycdERi7TVJ9rppCPiYxcmHXKyCkXuqEp4u7fwXCY24yqqi5K8qtJntla+9iuq9+S7lCIr0vyM0n+y9jrm/HQ1tqDk1ye5J9U1cN3Xb9W+7aqbp/k8Un+88DV67Rfj2Ld9vGzk3w2yUv3uMlBj5kx/FySr0zywCQ3pTtMY7e12q9Jnpz9J48r2a8HPFftebeBr/ndOKsxuYycUD4mMnLV1m3/TiEfExm5MOuWkVMudDcmudfM5UuTvH+v21TVqSR3zvFefl6Iqrpdur/8l7bWXrH7+tbax1prt/bnX5PkdlV18cjL3FnL+/s/P5jklelegp91mP0/psuTvKW1dvPuK9Zpv864eefwm/7PDw7cZm32cf/G3W9K8r+1/kDw3Q7xmFm61trNrbXPtdb+IsnP77GGddqvp5J8a5KX7XWbVezXPZ6rJvWYZVoZOaV87NcgI5dnUs81U8nHfvsycjHrWruMnHKh+4MkX1VVX9FPnp6U5FW7bvOqJDufIPPEJL+71z+2ZeuPAX5Bkmtbaz+5x22+bOf9C1X1kHR/P3823io/v447VtWdds6ne9Pv23fd7FVJvr06fzXJR3deal6RPSc467Jfd5l9bD4lya8N3Oa3kjymqu7aHxbxmP5ro6qqxyb5gSSPb639+R63OcxjZul2vUflb++xhsM8d4zlUUne2Vq7cejKVezXfZ6rJvOYJcmEMnJK+dhvX0Yu12Sea6aUj/32ZeQJrW1GthE/cWfRp3SfIvUn6T6N59n913443T+sJLlDusMLrkvy5iT3XeFaH5buZdW3JrmmPz0uyXcn+e7+Nk9P8o50nyj0piR/fUVrvW+/hj/q17Ozb2fXWkl+tt/3b0tyZoX79sJ04XPnma+tzX5NF6I3Jfmf6aYzT0v3PpXfSfLu/s+79bc9k+T5M/f9zv7xe12Sp65ordelO+Z753G786l490jymv0eMytY6y/2j8e3pntyvWT3WvvLc88dY6+1//qLdh6nM7dd9X7d67lqLR+zTvv+XU4iI/d5zK3N8/iu9crIxa1NPo67Xhl58rWuZUZW/80BAACYmCkfcgkAALDVFDoAAICJUugAAAAmSqEDAACYKIUOAABgohQ6AACAiVLoAAAAJkqhgxWpqt+rqkf353+kqn561WsCgFWTj3A0p1a9ANhi/yLJD1fV3ZM8KMnjV7weAFgH8hGOoFprq14DbK2qekOSi5Jc1lr7eFXdN8mzk9y5tfbE1a4OAFZDPsLhOeQSVqSq/kqSS5J8urX28SRprb23tfa01a4MAFZHPsLRKHSwAlV1SZKXJnlCkk9U1TeueEkAsHLyEY5OoYORVdWFSV6R5Htba9cm+VdJnrvSRQHAislHOB7voYM1UlVfkuRHkzw6yfNba/96xUsCgJWTj7A3hQ4AAGCiHHIJAAAwUQodAADARCl0AAAAE6XQAQAATJRCBwAAMFEKHQAAwEQpdAAAABOl0AEAAEzU/w/peLgF+X/28gAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1080x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def x2_func(x1,I,P1,P2): # We define x2 as a function of x1\n",
    "    return (I-x1*P1)/P2 # The function is derived by isolating x2 in the budgetconstraint\n",
    "       \n",
    "N=500\n",
    "shape_tuple = (N,N)\n",
    "x1_values = np.empty(shape_tuple)\n",
    "if I1.value>I2.value:\n",
    "    x_max1=I1.value/P1.value  \n",
    "else:\n",
    "    x_max1=I2.value/P1.value \n",
    "for i in range(N): # 0,1,...,N-1\n",
    "    for j in range(N): # 0,1,...,N-1\n",
    "        x1_values[i,j] = (i/(N-1))*x_max1 # in [0,x_max1]\n",
    "def Figure_1():\n",
    "    fig = plt.figure(figsize=(15,5)) # create the figure \n",
    "    ax = fig.add_subplot(1,2,1) # We add a subplot and place it in the top left corner\n",
    "    ax.plot(x1_values,x2_func(x1_values,I1.value,P1.value,P2.value),'b'); # creates surface plot in the axis\n",
    "    ax.set_xlabel('$x_1$') # add labels\n",
    "    ax.set_ylabel('$x_2$') # add labels\n",
    "    ax.set_title(\"Budget constraint for Consumer 1\") # add title\n",
    "    ay = fig.add_subplot(1,2,2) # We add a second plot and place it in the top right corner\n",
    "    ay.plot(x1_values,x2_func(x1_values,I2.value,P1.value,P2.value),'b'); # creates surface plot in the axis\n",
    "    ay.set_xlabel('$x_1$') # add labels\n",
    "    ay.set_ylabel('$x_2$') # add labels\n",
    "    ay.set_title(\"Budget constraint for Consumer 2\") # add title\n",
    "Figure_1()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Utility function**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "After setting the price levels and income levels, we define the utilityfunctions. \n",
    "\\\\[\n",
    "u_{Consumer_1}(x_1,x_2) = x_1^{\\alpha}x_2^{1-\\alpha}\n",
    "\\\\]\n",
    "\\\\[\n",
    "u_{Consumer_2}(x_1,x_2) = \\beta*log(x_1)+(1-\\beta)*log(x_2)\n",
    "\\\\]\n",
    "These functions can easily be altered to fit your own problem using the widgets, which allows you to change the values of \\\\(\\alpha\\\\) and \\\\(\\beta\\\\) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mConsumer 1:\n",
      "\u001b[1mAlpha (α)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4cb6d344aee441ac967546cc7027c045",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.5)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4a277e30e9c2444fb3e6317eee5c1e27",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=0.5, max=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mConsumer 2:\n",
      "\u001b[1mBeta (β)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f7559e1306ef42528653a9005834ce8f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.5)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "215a488a82d94234a126f5e31e87f692",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=0.5, max=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Consumer 1\n",
    "def c1_u_func(x1,x2,alpha): # We define a utility function\n",
    "    return (x1**alpha)*(x2**(1-alpha))\n",
    "\n",
    "print('\\033[1m' + 'Consumer 1:')\n",
    "print('\\033[1m' + 'Alpha (\\u03B1)') # We use this code \\u03B1 and similar ones to print greek letters. This particular one is for alpha\n",
    "alpha = widgets.FloatText(\n",
    "value=0.5)\n",
    "alphab = widgets.FloatSlider(\n",
    "value=0.5,\n",
    "step=0.1,\n",
    "min=0,\n",
    "max=1,)\n",
    "display(alpha,alphab)\n",
    "\n",
    "mylink = widgets.jslink((alpha, 'value'), (alphab, 'value'))\n",
    "\n",
    "# Consumer 2\n",
    "\n",
    "def c2_u_func(x1,x2,beta): # We define a utility function\n",
    "    return beta*np.log(x1)+(1-beta)*np.log(x2)\n",
    "\n",
    "print('\\033[1m' + 'Consumer 2:')\n",
    "print('\\033[1m' + 'Beta (\\u03B2)')\n",
    "beta = widgets.FloatText(\n",
    "value=0.5)\n",
    "betab = widgets.FloatSlider(\n",
    "value=0.5,\n",
    "step=0.1,\n",
    "min=0,\n",
    "max=1,)\n",
    "display(beta,betab)\n",
    "\n",
    "mylink = widgets.jslink((beta, 'value'), (betab, 'value'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We set the utlity values so we can plot the indifference curves."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mUtility for consumer 1 (u1)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d562753dab9f44ca9d12e8caa8489acc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=10.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3c0e271dadd04e88b7b4ea870e0ff839",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=10.0, max=50.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mUtility for consumer 2 (u2)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ed65ea6f324d45489de1defb7a04febc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5893c2572e5c462cbd0feb7aa89a2d71",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=1.0, max=3.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "print('\\033[1m' + 'Utility for consumer 1 (u1)')\n",
    "u1 = widgets.FloatText(\n",
    "value=10)\n",
    "u1b = widgets.FloatSlider(\n",
    "value=10,\n",
    "step=0.1,\n",
    "min=0,\n",
    "max=50,)\n",
    "display(u1,u1b)\n",
    "mylink = widgets.jslink((u1, 'value'), (u1b, 'value'))\n",
    "\n",
    "print('\\033[1m' + 'Utility for consumer 2 (u2)')\n",
    "u2 = widgets.FloatText(\n",
    "value=1)\n",
    "u2b = widgets.FloatSlider(\n",
    "value=1,\n",
    "step=0.1,\n",
    "min=0,\n",
    "max=3,)\n",
    "display(u2,u2b)\n",
    "mylink = widgets.jslink((u2, 'value'), (u2b, 'value'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next we plot the utilityfunctions using the values choosen above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def c1_x2_func2(x1,u,alpha):\n",
    "    return u**(1/(1-alpha))*(x1**(-alpha/(1-alpha)))\n",
    "def c2_x2_func2(x1,u,beta):\n",
    "    return np.exp((u-beta*np.log(x1))/(1-beta))\n",
    "\n",
    "def Figure_2():\n",
    "    fig = plt.figure(figsize=(15,5)) # creates the figure\n",
    "    ax = fig.add_subplot(1,2,1) # creates subplot \n",
    "    ax.plot(x1_values,c1_x2_func2(x1_values,u1.value,alpha.value),'b'); # creates surface plot in the axis\n",
    "    ax.set_xlabel('$x_1$') # add labels\n",
    "    ax.set_ylabel('$x_2$') # add labels\n",
    "    ax.set_title(\"Utility for Consumer 1\") # add title\n",
    "    ax.set_ylim([0, 20]) # here we limit the y axis, which is needed due to the values going towards negative infinity, when x1 goes towards 0.\n",
    "    ay = fig.add_subplot(1,2,2) # creates subplot \n",
    "    ay.plot(x1_values,c2_x2_func2(x1_values,u2.value,beta.value),'b'); # creates surface plot in the axis, but this time we use a different method due to the fact that we are using numpy functions (exp and log).\n",
    "    ay.set(xlabel='$x_1$', ylabel='$x_2$',\n",
    "       title=\"Utility for Consumer 2\", xlim=[0,I2.value/P1.value], ylim=[0,I2.value/P2.value]) # We also need to set our labels and title in a different way.\n",
    "Figure_2()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Solution**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we solve the consumer's problem for both types. This is done by maximizing the utility with regards to the budget constraint.\n",
    "\\\\[\n",
    "\\begin{eqnarray*}\n",
    "\\max_{x_{1},x_{2}}u(x_{1},x_{2})\\\\\n",
    "\\text{s.t.}\\\\\n",
    "p_{1}x_{1}+p_{2}x_{2} & \\leq & I,\\,\\,\\,p_{1},p_{2},I>0\\\\\n",
    "x_{1},x_{2} & \\geq & 0\n",
    "\\end{eqnarray*}\n",
    "\\\\]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def c1(x1,I,P1,P2,alpha): # First we define a function, which we will use to find the optimal value of x1. *****************************************************************\n",
    "    x2 = (I-P1*x1)/P2\n",
    "# We return the negative function of our utility and then minimizes this, which is the same as maximizing the utility\n",
    "    return -c1_u_func(x1,x2,alpha) \n",
    "\n",
    "def c2(x1,I,P1,P2,beta):\n",
    "    x2 = (I-P1*x1)/P2\n",
    "    return -c2_u_func(x1,x2,beta)\n",
    "\n",
    "# Next we use our optimizing function to maximize the utility. \n",
    "# Here we define x1 to be between 0 and the maximum number of good 1 you can buy for your income\n",
    "solver_c1 = optimize.minimize_scalar(c1, method='bounded', bounds=(0,I1.value/P1.value), args=(I1.value,P1.value,P2.value,alpha.value))  \n",
    "solver_c2 = optimize.minimize_scalar(c2, method='bounded', bounds=(0,I2.value/P1.value), args=(I2.value,P1.value,P2.value,beta.value)) \n",
    "# We then define our answers for both consumers\n",
    "c1_x1 = solver_c1.x\n",
    "c1_x2 = (I1.value-P1.value*c1_x1)/P2.value\n",
    "c1_u = c1_u_func(c1_x1,c1_x2,alpha.value)\n",
    "\n",
    "c2_x1 = solver_c2.x\n",
    "c2_x2 = (I2.value-P1.value*c2_x1)/P2.value\n",
    "c2_u = c2_u_func(c2_x1,c2_x2,beta.value)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This provides the following results:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mConsumer 1:\n",
      "\u001b[0mx1 = 10.0\n",
      "x2 = 3.3\n",
      "u  = 5.77\n",
      "I-p1*x1-p2*x2 = 0.00\n",
      "\n",
      "\u001b[1mConsumer 2:\n",
      "\u001b[0mx1 = 10.0\n",
      "x2 = 3.3\n",
      "u  = 1.75\n",
      "I-p1*x1-p2*x2 = 0.00\n"
     ]
    }
   ],
   "source": [
    "print('\\033[1m' + 'Consumer 1:')\n",
    "print('\\033[0m' + f'x1 = {c1_x1:.1f}') # Prints the x1 value\n",
    "print(f'x2 = {c1_x2:.1f}') # Prints the x2 value\n",
    "print(f'u  = {c1_u:.2f}') # Prints the utility\n",
    "print(f'I-p1*x1-p2*x2 = {I1.value-P1.value*c1_x1-P2.value*c1_x2:.2f}') # Prints a calculation to see whether the whole income has been used, such that income - consumption = 0 \n",
    "print ('')\n",
    "print('\\033[1m' + 'Consumer 2:')\n",
    "print('\\033[0m' + f'x1 = {c2_x1:.1f}') \n",
    "print(f'x2 = {c2_x2:.1f}') \n",
    "print(f'u  = {c2_u:.2f}') \n",
    "print(f'I-p1*x1-p2*x2 = {I2.value-P1.value*c2_x1-P2.value*c2_x2:.2f}') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can compare this answer to the one, we get from solving the problem manually.\n",
    "\n",
    "**Consumer 1:**\n",
    "\\\\[\n",
    "\\begin{eqnarray*}\n",
    "x_1^{\\ast} &=& \\alpha \\frac{I}{p_1} \\\\\n",
    "x_2^{\\ast} &=& (1-\\alpha) \\frac{I}{p_2}\\\\\n",
    "u^{\\ast} &=& u_{Consumer_1}(x_1^{\\ast},x_2^{\\ast})\n",
    "\\end{eqnarray*}\n",
    "\\\\]\n",
    "\n",
    "**Consumer 2:**\n",
    "\\\\[\n",
    "\\begin{eqnarray*}\n",
    "x_1^{\\ast} &=& \\beta \\frac{I}{p_1} \\\\\n",
    "x_2^{\\ast} &=& (1-\\beta) \\frac{I}{p_2}\\\\\n",
    "u^{\\ast} &=& u_{Consumer_2}(x_1^{\\ast},x_2^{\\ast})\n",
    "\\end{eqnarray*}\n",
    "\\\\]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mConsumer 1:\n",
      "\u001b[0mx1 = 10.0\n",
      "x2 = 3.3\n",
      "u  = 5.77\n",
      "\n",
      "\u001b[1mConsumer 2:\n",
      "\u001b[0mx1 = 10.0\n",
      "x2 = 3.3\n",
      "u  = 1.75\n"
     ]
    }
   ],
   "source": [
    "print('\\033[1m' + 'Consumer 1:')\n",
    "print('\\033[0m' + f'x1 = {alpha.value*I1.value/P1.value:.1f}') # Prints the x1 value\n",
    "print(f'x2 = {(1-alpha.value)*I1.value/P2.value:.1f}') # Prints the x2 value\n",
    "print(f'u  = {c1_u_func(alpha.value*I1.value/P1.value,(1-alpha.value)*I1.value/P2.value,alpha.value):.2f}') # Prints the utility\n",
    "print ('')\n",
    "print('\\033[1m' + 'Consumer 2:')\n",
    "print('\\033[0m' + f'x1 = {beta.value*I2.value/P1.value:.1f}') \n",
    "print(f'x2 = {(1-beta.value)*I2.value/P2.value:.1f}') \n",
    "print(f'u  = {c2_u_func(beta.value*I2.value/P1.value,(1-beta.value)*I2.value/P2.value,beta.value):.2f}') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can also visualize this by plotting our budget constraint against the utility function, where we use the results from above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def Figure_3():\n",
    "    fig = plt.figure(figsize=(15,5))  \n",
    "    ax = fig.add_subplot(1,2,1)\n",
    "    ax.plot(x1_values,c1_x2_func2(x1_values,c1_u,alpha.value),'b');\n",
    "    ax.plot(x1_values,x2_func(x1_values,I1.value,P1.value,P2.value),'b');\n",
    "    ax.set_xlabel('$x_1$') \n",
    "    ax.set_ylabel('$x_2$') \n",
    "    ax.set_title(\"Solution for Consumer 1\") \n",
    "    ax.set_ylim([0, I1.value/P2.value])\n",
    "    ax.set_xlim([0,I1.value/P1.value])\n",
    "    ax.plot(c1_x1,c1_x2, color='red', marker='o', linestyle='dashed', linewidth=5, markersize=10, fillstyle='none') \n",
    "    ay = fig.add_subplot(1,2,2)\n",
    "    ay.plot(x1_values,c2_x2_func2(x1_values,c2_u,beta.value),'b'); \n",
    "    ay.plot(x1_values,x2_func(x1_values,I2.value,P1.value,P2.value),'b')\n",
    "    ay.set(xlabel='$x_1$', ylabel='$x_2$',\n",
    "       title=\"Solution for Consumer 2\", xlim=[0,I2.value/P1.value], ylim=[0,20]) \n",
    "    ay.plot(c1_x1, c1_x2, color='red', marker='o', linestyle='dashed', linewidth=5, markersize=10, fillstyle='none')\n",
    "Figure_3()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We see that the utility function touches the budget constraint (shown by the red circle) at the result we found above."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Social optimum**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First we define the necessary aggregated variables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "soc_I=I1.value+I2.value\n",
    "def u_func(x1,x2,alpha,beta):\n",
    "    return c1_u_func(x1,x2,alpha)+c2_u_func(x1,x2,beta)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "And then we solve for the social optimum: \n",
    "\n",
    "\\\\[\n",
    "\\begin{eqnarray*}\n",
    "\\max_{x_{1},x_{2}}u_{Consumer_1}(x_{1},x_{2})+u_{Consumer_2}(x_{1},x_{2})\\\\\n",
    "\\text{s.t.}\\\\\n",
    "p_{1}x_{1}+p_{2}x_{2} & \\leq & I_{Consumer_1}+I_{Consumer_2},\\,\\,\\,p_{1},p_{2},I_{Consumer_1},I_{Consumer_2}>0\\\\\n",
    "x_{1},x_{2} & \\geq & 0\n",
    "\\end{eqnarray*}\n",
    "\\\\]\n",
    "\n",
    "**Notice:** We dont plot the graphs since isolateing \\\\(x_2\\\\) isn't possible for costumer 2."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mSocial optimum:\n",
      "\u001b[0mx1 = 20.0\n",
      "x2 = 6.7\n",
      "u  = 13.99\n",
      "I-p1*x1-p2*x2 = 0.00\n"
     ]
    }
   ],
   "source": [
    "def c1_and_c2(x1,I,P1,P2,alpha,beta): \n",
    "    x2 = (I-P1*x1)/P2\n",
    "    return -u_func(x1,x2,alpha,beta)\n",
    "\n",
    "solver = optimize.minimize_scalar(c1_and_c2, method='bounded', bounds=(0,soc_I/P1.value), args=(soc_I,P1.value,P2.value,alpha.value,beta.value)) \n",
    "soc_x1 = solver.x\n",
    "soc_x2 = (soc_I-P1.value*soc_x1)/P2.value\n",
    "soc_u = u_func(soc_x1,soc_x2,alpha.value,beta.value)\n",
    "\n",
    "print('\\033[1m' + 'Social optimum:')\n",
    "print('\\033[0m' + f'x1 = {soc_x1:.1f}')\n",
    "print(f'x2 = {soc_x2:.1f}') \n",
    "print(f'u  = {soc_u:.2f}') \n",
    "print(f'I-p1*x1-p2*x2 = {soc_I-P1.value*soc_x1-P2.value*soc_x2:.2f}') "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We can then compare this result to our earlier results from solving the consumer problems individually. We see that the changes is given by:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mChanges:\n",
      "\u001b[0mΔx1 = 0.0\n",
      "Δx2 = 0.0\n",
      "Δu = 6.47\n"
     ]
    }
   ],
   "source": [
    "print('\\033[1m' + 'Changes:')\n",
    "print('\\033[0m' + f'\\u0394x1 = {soc_x1-c1_x1-c2_x1:.1f}') \n",
    "print(f'\\u0394x2 = {soc_x2-c1_x2-c2_x2:.1f}') \n",
    "print(f'\\u0394u = {soc_u-c1_u-c2_u:.2f}')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Firms maximization problem**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    " ### **Determine the competitive situation**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First we need to select the competitive situation of the problem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "3fe9164f612a46caa732fed12952b678",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "RadioButtons(description='Competition:', options=('Competitive', 'Monopolistic'), value='Competitive')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "competition=widgets.RadioButtons(\n",
    "    options=['Competitive', 'Monopolistic'],\n",
    "    value='Competitive',\n",
    "    description='Competition:',\n",
    "    disabled=False\n",
    ")\n",
    "competition"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Set demand according to the competition**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Since you have picked the competitive market, you need to choose the price, p, at which the other firms sell their goods\n",
      "\n",
      "\u001b[1mPrice on goods (P)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7104e0f76e284cac92cc232a02993ccb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=15.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4990240766e64a798eaa4636069797d2",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=5.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "if ('Competitive'==competition.value): # This is the start of an if statement, which checks which form of competition was choosen.\n",
    "    print('Since you have picked the competitive market, you need to choose the price, p, at which the other firms sell their goods')\n",
    "    print('')\n",
    "    print('\\033[1m' + 'Price on goods (P)')\n",
    "    P = widgets.FloatText(\n",
    "    value=15)\n",
    "    Pb = widgets.FloatSlider(\n",
    "    value=5,\n",
    "    step=1,\n",
    "    min=0,\n",
    "    max=100.0,)\n",
    "    display(P,Pb)\n",
    "    linkP = widgets.jslink((P, 'value'), (Pb, 'value'))\n",
    "\n",
    "else:\n",
    "    print('Since you have picked monopolistic competition, we need to define the demand function of the consumer. Here we use a linear function (D(x)=b-a*x), where the slope, a, and the constant term, b, are determined by the widgets below.')\n",
    "    print('')\n",
    "    # Determine a\n",
    "    print('\\033[1m' + 'Slope of demand function (a)')\n",
    "    a = widgets.FloatText(\n",
    "    value=5)\n",
    "    aa = widgets.FloatSlider(\n",
    "    value=5,\n",
    "    step=0.5,\n",
    "    min=0,\n",
    "    max=10.0,)\n",
    "    display(a,aa)\n",
    "    linka = widgets.jslink((a, 'value'), (aa, 'value'))\n",
    "\n",
    "    # Determine b\n",
    "    print('\\033[1m' + 'Constant term (b)')\n",
    "    b = widgets.FloatText(    \n",
    "    value=200)\n",
    "    bb = widgets.FloatSlider(\n",
    "    value=200,\n",
    "    step=1,\n",
    "    min=0,\n",
    "    max=500.0,)\n",
    "    display(b,bb)\n",
    "    linkb = widgets.jslink((b, 'value'), (bb, 'value'))\n",
    "    # Note that we don't define the demand function yet since the user need to be able to change the variables first. Therefore, we define the demand function, when solving the problem"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Define the Total Cost function**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next we define our total cost function, which is defined in a quadratic form. (We have included total cost, as it is needed to determine whether the firm wants to enter the market or not)\n",
    "\n",
    "\\\\[\n",
    "TC(x) = c*x^2+FC\n",
    "\\\\]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mSlope, c\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "83fed593f8d04cc5aff698b4dcb72f0f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=0.5)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a59ad98f47ee4ea393e0653c4ad1d300",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=0.5, max=10.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\u001b[1mFixed costs (FC)\n"
     ]
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "1255c259963c474680dd753f2256948d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatText(value=10.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bae2ed5f1d194f67a70f683fc055e78b",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "FloatSlider(value=10.0, step=1.0)"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Determine variable costs\n",
    "print('\\033[1m' + 'Slope, c')\n",
    "c = widgets.FloatText(\n",
    "value=0.5)\n",
    "cb = widgets.FloatSlider(\n",
    "value=0.5,\n",
    "step=0.1,\n",
    "min=0,\n",
    "max=10.0,)\n",
    "display(c,cb)\n",
    "linkb = widgets.jslink((c, 'value'), (cb, 'value'))\n",
    "    \n",
    "# Determine fixed costs\n",
    "print('\\033[1m' + 'Fixed costs (FC)')\n",
    "FC = widgets.FloatText(\n",
    "value=10)\n",
    "FCb = widgets.FloatSlider(\n",
    "value=10,\n",
    "step=1,\n",
    "min=0,\n",
    "max=100.0,)\n",
    "display(FC,FCb)\n",
    "linkb = widgets.jslink((FC, 'value'), (FCb, 'value'))   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 576x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "def TC(x,c,FC):\n",
    "    return c*x**2+FC\n",
    "def MC(x,c):\n",
    "    return c*x*2\n",
    "\n",
    "p_x_max=50 # Here set the capacity limit at 50\n",
    "shape_tuple = (N,N)\n",
    "p_x_values = np.empty(shape_tuple)\n",
    "\n",
    "for i in range(N): \n",
    "    for j in range(N): \n",
    "        p_x_values[i,j] = (i/(N-1))*p_x_max \n",
    "\n",
    "def Figure_7():\n",
    "    fig = plt.figure(figsize=(8,5))  \n",
    "    ax = fig.add_subplot(1,1,1)\n",
    "    ax.plot(p_x_values,TC(p_x_values,c.value,FC.value), 'b'); \n",
    "    ax.set_xlabel('$x$') \n",
    "    ax.set_ylabel('$TC$') \n",
    "    ax.set_title('Total cost')\n",
    "Figure_7()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Solution**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We now solve the maximization problem by maximizing the porfit of the firm.\n",
      "And since you have choosen the competitive market. The profit function of the firm is π=p*x-TC(x)\n",
      "The results are:\n",
      "x = 15.0\n",
      "Price = 15.0\n",
      "π = 102.5\n",
      "Total cost  = 122.5\n",
      "Revenue  = 225.0\n",
      "\n",
      "We can also show this result by plotting the marginal cost against the marginal revenue. The marginal costs is the first derivative\n",
      "of the total cost function. This means MC(x)=2*VC*x. The marginal revenue is equal to the price level, p. This gives us the following plot.\n",
      "It shows that for MR=MC, the firm maximizes its profit.\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "print('We now solve the maximization problem by maximizing the profit of the firm.')\n",
    "if ('Competitive'==competition.value):\n",
    "    print('And since you have choosen the competitive market. The profit function of the firm is \\u03C0=p*x-TC(x)')\n",
    "elif ('Monopolistic'==competition.value):\n",
    "    print('And since you have choosen the monopolistic market. The profit function of the firm is \\u03C0=D(x)*p-TC(x)')\n",
    "\n",
    "if ('Competitive'==competition.value):\n",
    "    def pi_competitive(x,P,c,FC):\n",
    "        return -(P*x-TC(x,c,FC)) # Here we define pi as the profit times -1, so that we can use scipy optimize\n",
    "    \n",
    "    solver4 = optimize.minimize_scalar(pi_competitive, method='bounded', bounds=(0,p_x_max), args=(P.value,c.value,FC.value)) \n",
    "    \n",
    "    # We define our answers as\n",
    "    x_opt1 = solver4.x\n",
    "    price1 = P.value\n",
    "    pi1=P.value*x_opt1-TC(x_opt1,c.value,FC.value)\n",
    "    TC1 = TC(x_opt1,c.value,FC.value)\n",
    "    REV1  = P.value*x_opt1\n",
    "    print('The results are:')\n",
    "    print(f'x = {x_opt1:.1f}')\n",
    "    print(f'Price = {P.value:.1f}')\n",
    "    print(f'\\u03C0 = {pi1:.1f}') \n",
    "    print(f'Total cost  = {TC1:.1f}') \n",
    "    print(f'Revenue  = {REV1:.1f}') \n",
    "    \n",
    "    if pi1>-FC.value and pi1<0: # We define an if statement to check, whether the firm wants to produce anything.\n",
    "        print('')\n",
    "        print('Although the profit is negative, the firm will still produce since they must cover some of the fixed costs')\n",
    "    elif pi1<-FC.value:\n",
    "        print('Since the profit is less than the fixed costs, the firm would not produce anything, as this will lower their profits')\n",
    "    \n",
    "    print('')\n",
    "    print('We can also show this result by plotting the marginal cost against the marginal revenue. The marginal costs is the first derivative')\n",
    "    print('of the total cost function. This means MC(x)=2*VC*x. The marginal revenue is equal to the price level, p. This gives us the following plot.') \n",
    "    print('It shows that for MR=MC, the firm maximizes its profit.')\n",
    "    def MR1(x,P):\n",
    "        return P*x/x\n",
    "    def Figure_8():\n",
    "        fig = plt.figure(figsize=(15,5)) \n",
    "        ax = fig.add_subplot(1,2,1)\n",
    "        ax.plot(p_x_values,MR1(p_x_values,P.value),'b'); \n",
    "        ax.plot(p_x_values,MC(p_x_values,c.value),'b')\n",
    "        ax.set_xlabel('$x$') \n",
    "        ax.set_ylabel('$p$') \n",
    "        ax.set_title('Marginal cost and Marginal revenue')\n",
    "        ax.plot(x_opt1, P.value, color='red', marker='o', linestyle='dashed', linewidth=5, markersize=10, fillstyle='none')\n",
    "        ay = fig.add_subplot(1,2,2)\n",
    "        ay.plot(p_x_values,TC(p_x_values,c.value,FC.value),'b');\n",
    "        ay.plot(p_x_values,P.value*p_x_values/p_x_values,'b');\n",
    "        ay.set_xlabel('$x$')\n",
    "        ay.set_ylabel('$p$')\n",
    "        ay.set_title('Total cost and Price')\n",
    "        ay.set_xlim(0,20)\n",
    "        ay.set_ylim(0,100)\n",
    "    Figure_8()    \n",
    "    \n",
    "\n",
    "    \n",
    "elif ('Monopolistic'==competition.value):\n",
    "    def pi_monopolistic(x,b,a,c,FC):\n",
    "        return -((b-a*x)*x-TC(x,c,FC)) # Here we define pi as the profit times -1, so that we can use scipy optimize\n",
    "    \n",
    "    solver5 = optimize.minimize_scalar(pi_monopolistic, method='bounded', bounds=(0,p_x_max), args=(b.value,a.value,c.value,FC.value))\n",
    "    \n",
    "    def MR2(x,b,a):\n",
    "        return b-2*a*x\n",
    "    \n",
    "    # We define our answers as\n",
    "    x_opt2 = solver5.x \n",
    "    price2 = b.value-a.value*x_opt2\n",
    "    pi2=(b.value-a.value*x_opt2)*x_opt2-TC(x_opt2,c.value,FC.value)\n",
    "    TC2 = TC(x_opt2,c.value,FC.value)\n",
    "    REV2  = (b.value-a.value*x_opt2)*x_opt2\n",
    "    print('The results are:')\n",
    "    print(f'x = {x_opt2:.1f}')\n",
    "    print(f'Price = {price2:.1f}')\n",
    "    print(f'\\u03C0 = {pi2:.1f}') \n",
    "    print(f'Total cost = {TC2:.1f}') \n",
    "    print(f'Revenue = {REV2:.1f}') \n",
    "    \n",
    "    if pi2>-FC.value and pi2<0:\n",
    "        print('')\n",
    "        print('Although the profit is negative, the firm will still produce since they must cover some of the fixed costs')\n",
    "    elif pi2<-FC.value and pi2<0:\n",
    "        print('Since the profit is less than the fixed costs, the firm would not produce anything, as this will lower their profits')\n",
    "    \n",
    "    print('')\n",
    "    print('We can also show this result by plotting the marginal cost against the marginal revenue. The marginalcosts is the first derivative')\n",
    "    print('of the total cost. This means MC(x)=2*c*x. The marginal revenue is equal to MR(x)=b-2*a*x.')\n",
    "    print('When plotting this, we notice that when MR=MC, the firm maximizes its profit.')\n",
    "    print('And as they have monopolly, they find the optimal value of x, when MR=MC, and sets the optimal price on the demand function according to this.')\n",
    "    \n",
    "    def Figure_9():\n",
    "        fig = plt.figure(figsize=(15,5)) # creates the figure \n",
    "        ax = fig.add_subplot(1,2,1)\n",
    "        ax.plot(p_x_values,b.value-a.value*p_x_values, 'b' ); \n",
    "        ax.plot(p_x_values,MC(p_x_values,c.value), 'r');\n",
    "        ax.plot(p_x_values,MR2(p_x_values,b.value,a.value), 'r');\n",
    "        ax.plot(x_opt2, MR2(x_opt2,b.value,a.value), color='blue', marker='*', linestyle='dashed', linewidth=5, markersize=10, fillstyle='full')\n",
    "        ax.plot(x_opt2, b.value-a.value*x_opt2, color='red', marker='o', linestyle='dashed', linewidth=5, markersize=10, fillstyle='full')\n",
    "        ax.vlines(x=x_opt2, ymin=0, ymax=price2) # This code plots a vertical line at the optimal value of x\n",
    "        ax.set_xlabel('$x$') \n",
    "        ax.set_ylabel('$p$') \n",
    "        ax.set_ylim(0,b.value)\n",
    "        ax.set_xlim(0,b.value/a.value)\n",
    "        ax.set_title('Marginal cost and Marginal revenue')\n",
    "        ay = fig.add_subplot(1,2,2)\n",
    "        ay.plot(p_x_values,TC(p_x_values,c.value,FC.value),'b');\n",
    "        ay.plot(p_x_values,b.value-a.value*p_x_values,'b')\n",
    "        ay.set_xlabel('$x$')\n",
    "        ay.set_ylabel('$p$')\n",
    "        ay.set_title('Total cost and Demand function')\n",
    "        ay.set_ylim(0,b.value)\n",
    "        ay.set_xlim(0,b.value/a.value)\n",
    "    Figure_9()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
