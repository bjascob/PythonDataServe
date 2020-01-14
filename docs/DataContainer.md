# DataContainer

The DataContainer is a small class that facilitates saving raw data to a .pkl file.

## Example

```
from dataserve import DataContainer
dc = DataContainer()
dc.x = 5
dc.y = 'a'
dc.add_object_data( my_object )
dc.save('test.pkl.gz')

dc2 = DataContainer('test.pkl.gz')
```

## Methods
**init**
```
DataContainer(self, load_fn=None)
```
If the optional `load_fn` is supplied, the pkl or pkl.gz file will be loaded.

**add_object_data**
```
add_object_data(self, obj, add_private=False)
```
The method adds any attribute data from the `obj` to the DataContainer.  By default attributes starting with an underscore are omitted.  If `add_private=True`, they will be included.

**save**
```
save(self, filename)
```
Save the DataContainer to a pickle file.  The filename should end in .pkl or .pkl.gz.  For .pkl.gz, the data will be gzipped which takes some additional time but saves on space.

**load**
```
load(self, filename)
```
Load the DataContainer from a file.  If the filename ends in .gz the loader will used gunzip to load the data.  This is identical to instantiating the DataContainer with a filename.
