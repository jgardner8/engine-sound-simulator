# Run
pip install -r requirements.txt --user
python main.py

## Troubleshooting
PermissionError: The user (that this program is being run as) does not have permission to access the input events, check groups and permissions, for example, on Debian, the user needs to be in the input group.
```
sudo usermod -aG input $USER
su - $USER # or logout and login again
```
