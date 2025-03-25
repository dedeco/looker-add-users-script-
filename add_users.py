import looker_sdk
import sys
import argparse

def create_group_and_add_users(group_name):
    """
    Creates a new group in Looker if it doesn't exist, fetches all users, and adds them to the group.
    
    Args:
        group_name (str): The name of the group to create or use
    """
    try:
        # Initialize the Looker SDK
        # Note: This assumes you have configured your credentials in looker.ini
        # or using environment variables (LOOKERSDK_BASE_URL, LOOKERSDK_CLIENT_ID, LOOKERSDK_CLIENT_SECRET)
        sdk = looker_sdk.init40()
        
        # Check if group already exists
        group_id = None
        existing_groups = sdk.all_groups()
        for group in existing_groups:
            if group.name == group_name:
                group_id = group.id
                print(f"Group '{group_name}' already exists with ID: {group_id}")
                break
        
        # Create the group if it doesn't exist
        if group_id is None:
            try:
                # Create a dictionary with the group properties
                new_group = {'name': group_name}
                created_group = sdk.create_group(new_group)
                group_id = created_group.id
                print(f"Created new group: '{group_name}' with ID: {group_id}")
            except Exception as create_error:
                print(f"Error creating group '{group_name}': {str(create_error)}")
                return
        
        # Get all users
        try:
            all_users = sdk.all_users()
            print(f"Found {len(all_users)} users in the system")
        except Exception as users_error:
            print(f"Error fetching users: {str(users_error)}")
            return
        
        # Get current users in the group to avoid duplicates
        try:
            group_users_list = sdk.all_group_users(group_id=group_id)
            # Create a set of user IDs that are already in the group for faster lookups
            users_in_group = {user.id for user in group_users_list}
            print(f"Group '{group_name}' already has {len(users_in_group)} users")
        except Exception as group_users_error:
            print(f"Warning: Could not fetch existing group users: {str(group_users_error)}")
            users_in_group = set()  # Empty set as fallback
        
        # Add all users to the group
        users_added = 0
        users_skipped = 0
        
        for user in all_users:
            try:
                # Check if user is already in the group
                if user.id in users_in_group:
                    print(f"User {user.id} ({user.display_name}) is already in group {group_name}")
                    users_skipped += 1
                    continue
                
                # Add user to group
                user_inclusion = {'user_id': user.id}
                sdk.add_group_user(
                    group_id=group_id,
                    body=user_inclusion
                )
                print(f"Added user {user.id} ({user.display_name}) to group {group_name}")
                users_added += 1
                
            except Exception as user_error:
                print(f"Failed to add user {user.id} ({user.display_name}): {str(user_error)}")
                users_skipped += 1
        
        print(f"Process completed. {users_added} users added, {users_skipped} users skipped.")
        
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Create or use a Looker group and add all users to it.')
    parser.add_argument('--group-name', type=str, required=True, help='Name of the group to create or use')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Run the main function with the provided group name
    create_group_and_add_users(args.group_name)
