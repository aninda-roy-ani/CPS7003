from week4.data_access_layer import role_crud, user_crud


def create_role(role_name):
    # Business rule: role name must be unique
    existing_role = role_crud.get_role_by_name(role_name)

    if existing_role:
        return None

    created_role = role_crud.create_role(role_name)
    return created_role


def delete_role(role_id):
    # Business rule: prevent deletion of roles that are in use
    role_crud.delete_role(role_id)

if __name__ == "__main__":
    delete_role(3)
    #create_role("STAFF")