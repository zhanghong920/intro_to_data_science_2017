# Anaconda and Conda environment
## Install anaconda
**Anaconda** is a distribution of packages built for data science. It comes with conda, a package and environment manager. We can use conda to create environments for isolating your projects which use different versions of packages such as python. We can also use it to install, uninstall, and update packages in our environments. 

**Anaconda** is available for Windows, Mac OS X, and Linux. You can find the installers and installation instructions at [Here](https://www.continuum.io/downloads).

Choose the Python 2 version, you can install Python 3 versions later. Also, choose the 64-bit installer if you have a 64-bit operating system, otherwise go with the 32-bit installer. 

After installation, you’re automatically in the default conda environment with all packages installed. You can check out your own install by entering conda list into your terminal.

Open the Anaconda Prompt application (if on window. Use terminal on MAC). In the prompt, run the following commands:

```
conda upgrade --all
# this step taks forever, so if in hurry, do it later.
```

Answer yes when asked if you want to install the packages. The packages that come with the initial install tend to be out of date, so updating them now will prevent future errors from out of date software.

**Troubleshooting**
If you are seeing the following "conda command not found" and are using ZShell, you have to do the following:

Add ```export PATH="/Users/username/anaconda/bin:$PATH"``` to your .zsh_config file.

## Manage environment and packages
### Create an environment
To create an environment, use conda create -n env_name list of packages in your terminal. 

i.e.:

```
conda create -n itds python=2
(itds stands for intro_to_data_science. Feel free to choose another name.)
```

When creating an environment, you can specify which version of Python to install in the environment. This command installs the most recent version of Python 2, respectively. To install a specific version, use conda create -n itds python=3.3 for Python 3.3.

### Enter and leave the environment
use `source activate itds` to enter the environment you just created on OSX/Linux. On Windows, use `activate itds`.

To leave the environment, type `source deactivate` on OSX/Linux. On Windows, use `deactivate`.

### Install packages
When you're in the environment, you'll see the environment name in the terminal prompt. The environment has only a few packages installed by default, plus the ones you installed when creating it. You can check this out with `conda list`. Installing packages in the environment is: `conda install package_name`. The specific packages you install will only be available when you're in the environment. 

### Saving and loading environments
A really useful feature is sharing environments so others can install all the packages used in your code, with the correct versions. You can save the packages to a YAML file with `conda env export > environment.yaml`. The first part conda env export writes out all the packages in the environment, including the Python version.

To create an environment from an environment file use `conda env create -f environment.yaml`. This will create a new environment with the same name listed in environment.yaml.

You can also create a pip requirements.txt file using `pip freeze` for people not using conda.

### Listing environments
If you forget what your environments are named , use `conda env list` to list out all the environments you've created. You should see a list of environments, there will be an asterisk next to the environment you're currently in.

### Removing environments
If there are environments you don't use anymore, `conda env remove -n env_name` will remove the specified environment.

### Summary
So here are the commands we want to run to create the environment we need for this class:

```
(using MAC)
conda create -n itds python=2
source activate itds
conda list
conda install numpy pandas jupyter notebook git
conda list
conda env export > environment.yaml
cat environment.yaml
source deactivate
conda env list
```
