# vault-recursive-delete
This is a small helper script to delete a hashicorp vault directory recursively

# Usage

First install the requirements

```
pip install -r requirements.txt
```

Then you can delete a folder recursively from your vault server:

```
python vault-delete-recursively.py $FOLDER
```

You need to have VAULT\_ADDR and VAULT\_TOKEN defined in your environment.

# Maintainer

Christian Beneke <c.beneke@wirelab.org>
