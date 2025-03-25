# Looker Group Management Script

This Python script allows you to create a group in Looker and add all users to that group. The script checks if the group already exists before creating it and avoids adding users who are already members of the group.

## Features

- Creates a new group in Looker if it doesn't already exist
- Fetches all users from Looker
- Checks which users are already in the group
- Adds users who aren't yet members of the group
- Provides detailed logs and statistics about the process

## Prerequisites

1. Python 3.6 or higher
2. Looker SDK for Python

## Installation

1. Install the Looker SDK:
   ```bash
   pip install looker-sdk
   ```

2. Download the script to your local machine.

## Configuration

The script requires Looker API credentials to connect to your Looker instance. You can provide these credentials in two ways:

### Option 1: Environment Variables

Set the following environment variables:

**Linux/macOS:**
```bash
export LOOKERSDK_BASE_URL=https://your-looker-instance.com:19999
export LOOKERSDK_CLIENT_ID=your_client_id
export LOOKERSDK_CLIENT_SECRET=your_client_secret
```

**Windows (Command Prompt):**
```cmd
set LOOKERSDK_BASE_URL=https://your-looker-instance.com:19999
set LOOKERSDK_CLIENT_ID=your_client_id
set LOOKERSDK_CLIENT_SECRET=your_client_secret
```

**Windows (PowerShell):**
```powershell
$env:LOOKERSDK_BASE_URL = "https://your-looker-instance.com:19999"
$env:LOOKERSDK_CLIENT_ID = "your_client_id"
$env:LOOKERSDK_CLIENT_SECRET = "your_client_secret"
```

### Option 2: Configuration File (looker.ini)

Create a file named `looker.ini` in the same directory as the script with the following content:

```ini
[Looker]
base_url=https://your-looker-instance.com:19999
client_id=your_client_id
client_secret=your_client_secret
verify_ssl=true
```

## Usage

Run the script with the `--group-name` parameter followed by the name of the group you want to create or use:

```bash
python looker_group_script.py --group-name "Your Group Name"
```

### Example

```bash
python looker_group_script.py --group-name "Data Analysts"
```

### Expected Output

```
Group 'Data Analysts' already exists with ID: 123
Found 45 users in the system
Group 'Data Analysts' already has 20 users
User 5 (Alice Johnson) is already in group Data Analysts
User 8 (Bob Smith) is already in group Data Analysts
...
Added user 25 (Carol Davis) to group Data Analysts
Added user 27 (Dave Wilson) to group Data Analysts
...
Process completed. 25 users added, 20 users skipped.
```

## Error Handling

The script includes error handling for common scenarios:
- If the script can't connect to Looker, it will display an error message
- If group creation fails, the script will stop and report the error
- If adding a user fails, the script will continue with the next user and report the error

## Getting API Credentials

To get API credentials for your Looker instance:

1. Log in to Looker as an admin
2. Go to Admin > API Credentials
3. Click "New API Key"
4. Save the Client ID and Client Secret securely

## Troubleshooting

- **Connection Issues:** Ensure your Looker instance is accessible from your network and the URL is correct
- **Authentication Errors:** Verify your client ID and secret are correct and have not expired
- **Permission Errors:** Make sure your API credentials have the necessary permissions to create groups and manage users

## Notes

- This script adds ALL users to the specified group. If you need more selective user addition, you'll need to modify the script.
- The script needs to be run by someone with admin privileges or sufficient permissions in Looker.
