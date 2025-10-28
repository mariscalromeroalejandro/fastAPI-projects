# Password generator
This is a basic project that generates secure passwords using FastAPI and Python. The application allows users to specify the length and complexity of the password, including options for uppercase letters, lowercase letters, numbers, and special characters.

## Usage
```
API ENDPOINT: '/v1/passwordgenerator/'
```

Query parameters available:
| Parameter              | Type    | Description                                         | Default Value |
|------------------------|---------|-----------------------------------------------------|----------------|
| length                 | int     | Length of the generated password                    | 8             |
| exclude_numbers        | bool    | Exclude numbers from the password if set to true     | false          |
| exclude_special_chars  | bool    | Exclude special characters from the password if set to true | false          |

## Example Request
```
GET /v1/passwordgenerator/?length=16&exclude_numbers=true
``` 

## Example Response
```json
{
  "password": "aBcdEfGhIjKlMnOp"
}
```