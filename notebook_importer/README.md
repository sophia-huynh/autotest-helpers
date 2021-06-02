# Notebook Importer

This allows jupyter notebooks to be imported as python modules. 

Import the `notebook_importer` module first and then import files with an `.ipynb` extension. For example:

```python
import notebook_importer
import my_notebook # assumes a file named 'my_notebook.ipynb' in the python path
```

This will not execute the cells in the notebook right away.

To inspect the cells in the notebook:

```python
cells = notebook_importer.get_cells(my_notebook) # returns a list of notebook cells
```

To run a single cell:

```python
cells[0].run()
```

To run all cells in order:

```python
for cell in cells:
    cell.run()

# OR

notebook_importer.run_cells(my_notebook)
```


## Installation:

```shell
pip install 'git+https://github.com/MarkUsProject/autotest-helpers.git#subdirectory=notebook_importer'
```
