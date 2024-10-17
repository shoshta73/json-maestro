Installation
============

This section will guide you through the process of installing JSONMaestro.

There are two ways to install JSONMaestro:

1. Using pip
2. From source

Using pip
---------

The recommended way to install JSONMaestro is using pip. This method is the easiest and most straightforward way to install JSONMaestro.

To install JSONMaestro using pip, follow these steps:

1. Open a terminal or command prompt.

2. Run the following command to install JSONMaestro:

.. code-block:: bash

	pip install jsonmaestro

From source
-----------

If you prefer to install JSONMaestro from source, you can do so by following these steps:

1. Clone the repository:

.. code-block:: bash

	git clone https://github.com/gbowne1/json-maestro.git # via https
	git clone git@github.com:gbowne1/json-maestro.git # via ssh

2. Navigate to the cloned repository:

.. code-block:: bash

	cd /path/to/cloned/json-maestro

3. Install the required dependencies:

.. code-block:: bash

	pip install -r requirements.txt

4. Install JSONMaestro using your preferred method (NOTE: both are shown here, either one should work):

.. code-block:: bash

	pip install . # for installing using pip
	python setup.py install # for using setup.py script