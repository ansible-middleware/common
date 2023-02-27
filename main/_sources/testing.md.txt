# Testing

## Continuous integration

The collection is tested with ansible-test:

```
ansible-test sanity -v --color --python ${{ matrix.python_version }} --exclude changelogs/fragments/.gitignore --skip-test symlinks
```
