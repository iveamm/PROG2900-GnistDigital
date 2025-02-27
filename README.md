# GNIST

Welcome to GNIST. This project is developed by Gruppe 208 for PROG2900 at NTNU.

## Table of Contents

1. [Project Structure](#project-structure)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Local Setup](#local-setup)
3. [Migrating the database](#migrating-the-database)
4. [Running the Application](#running-the-application)
5. [API Documentation](#api-documentation)

## Project Structure

The GNIST project is organized into two main components:

- **FrontEnd/**: Contains the React application that serves as the user interface.
- **BackEnd/**: Houses the Django application responsible for server-side operations, including API and database management.

Root directory files:
- `.gitignore`: Specifies intentionally untracked files to ignore.
- `README.md`: Documentation that provides setup instructions and information.
- `Gnist brukermanual.pdf`: User manual for the applicaiton.

## Getting Started

### Prerequisites

To get started, you'll need to install:
- Node.js and npm (Node Package Manager)
- Python and pip (Python Package Manager)
- A preferred IDE, such as Visual Studio Code

### Local Setup

1. **Clone the Repository**:
   Clone the repository to your local machine using the following command:
    ```
    git clone https://gitlab.stud.idi.ntnu.no/ahmadmm/gnist.git
    ```
    Navigate into the prog2900-gnistdigital folder
    ```
    cd prog2900-gnistdigital
    ```
    Navigate to the project directory:
    ```
    cd gnist
    ```

2. **FrontEnd Setup**:
    Navigate to the FrontEnd directory:
    ```
    cd FrontEnd
    ```
    Install the necessary npm packages:
    ```
    npm install
    ```
    In FrontEnd directory create .env file in the root of the Frontend folder and add auth0 domain and clientId for your application: 
    ```
    REACT_APP_AUTH0_DOMAIN={your applications auth0 domain}
    REACT_APP_AUTH0_CLIENT_ID={your applications auth0 client id}
    ```
3. **BackEnd Setup**:
    Navigate to the BackEnd directory:
    ```
    cd ../BackEnd
    ```
    Set up a Python virtual environment:
    ```
    python -m venv myenv
    ```
    Navigate to myenv then activate the virtual environment:
    For Windows:
    ```
    .\Scripts\activate 
    ```
    For macOS and Linux:
    ```
    source myenv/bin/activate
    ```
    Inside the BackEnd directory where is the requirements.txt located
    Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```
    Navigate to gnist again and follow the Start the BackEnd instructions bellow.


## Migrating the databse
   In the terminal window ensure that you're in the Backend directory within the same folder as the manage.py file and the vitual environment is activated. 

1. **Create migrations**

   ```
   python manage.py makemigrations digital_medlemsordning
   ```

2. **Apply migrations**

   ```
   python manage.py migrate 
   ```

## Running the Application

1. **Start the FrontEnd**:
   Inside the FrontEnd directory, start the React application:
    ```
    npm start
    ```
   Your default web browser will open to `http://localhost:3000`.

2. **Start the BackEnd**:
   In a new terminal window, ensure you're in the BackEnd directory within the same folder as the manage.py file and the virtual environment is activated, then start the Django server:
    ```
    python manage.py runserver
    ```
   The Django API will be available at `http://localhost:8000`.

## API Documentation

<details>
<summary><h4>Create a new activity:</h4></summary>

```http
  POST /digital_medlemsordning/create_activity/
```

| Content-Type                      |
|-----------------------------------|
|`application/multipart/form-data`  |

| Parameter      | Type     | Description                                |
|:---------------|:---------|:-------------------------------------------|
| `title`        | `string` | **Required**. Ttile of activity            |
| `description`  | `string` | **Required**. Description of activity      |
| `image`        | `file`   | **Required**. Image of activity            |
| `date`         | `string` | **Required**. Date of activity             |
| `limit`        | `string`|  **Optional**. Member capacity of activity  |

##### Example POST-Body:
```json
{
    "title": "Football Night",
    "description": "Manchester United vs Arsenal 21:00",
    "image": "football_.jpg",
    "date": "2024-08-19",
    "limit": 40
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "Activity created successfully"
}
```

</details>

<details>
<summary><h4>Retrieve all future activities:</h4></summary>

```http
  GET /digital_medlemsordning/get_future_activities/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "activityID": "81",
        "title": "Football night",
        "description": "Manchester United vs Liverpool 18:00",
        "image": "/media/activity_pics/football_image3.png",
        "date": "2025-05-29",
        "limit": 40,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    {
        "activityID": 77,
        "title": "Skydive",
        "description": "Skydive lessons at 5 PM in Copenhagen.",
        "image": "/media/activity_pics/skydive.jpeg",
        "date": "2025-05-09",
        "limit": null,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve all past activities:</h4></summary>

```http
  GET /digital_medlemsordning/get_past_activities/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "activityID": 77,
        "title": "Skydive",
        "description": "Skydive lessons at 5 PM in Copenhagen.",
        "image": "/media/activity_pics/skydive.jpeg",
        "date": "2024-05-09",
        "limit": null,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    {
        "activityID": "81",
        "title": "Football night",
        "description": "Manchester United vs Liverpool 18:00",
        "image": "/media/activity_pics/football_image3.png",
        "date": "2023-05-29",
        "limit": 40,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve all curent date activites:</h4></summary>

```http
  GET /digital_medlemsordning/get_activity_today/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "activityID": 77,
        "title": "Skydive",
        "description": "Skydive lessons at 5 PM in Copenhagen.",
        "image": "/media/activity_pics/skydive.jpeg",
        "date": "2024-05-10",
        "limit": null,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    {
        "activityID": "81",
        "title": "Football night",
        "description": "Manchester United vs Liverpool 18:00",
        "image": "/media/activity_pics/football_image3.png",
        "date": "2024-05-10",
        "limit": 40,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "Soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Howard",
                "last_name": "Linus",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve all activites:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_activity/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "activityID": 55,
        "title": "Yoga Retreat",
        "description": "Enjoy the tranquility of yoga in a serene setting, focusing on breath control, flexibility, and strength. Ideal for all levels, this session promotes mental clarity and physical wellness.",
        "image": "/media/activity_pics/YougaYogaSeaWall.jpg",
        "date": "2025-05-09",
        "limit": null,
        "signed_up_count": 0,
        "signed_up_members": []
    },
    {
        "activityID": 75,
        "title": "Hiking Adventure",
        "description": "Hiking Adventure",
        "image": "/media/activity_pics/Hiking_Adventure_zHouiE5.jpeg",
        "date": "2024-03-12",
        "limit": 20,
        "signed_up_count": 1,
        "signed_up_members": [
            {
                "first_name": "soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            }
        ]
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve specific activity:</h4></summary>

```http
  GET /digital_medlemsordning/get_activity_details/{activityID}/
```

| Parameter   | Type     | Description                       |
|:------------|:---------|:----------------------------------|
| `activityID`| `string` | **Required**. The Activity ID     |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "activityID": 75,
    "title": "Hiking Adventure",
    "description": "Hiking Adventure",
    "image": "/media/activity_pics/Hiking_Adventure_zHouiE5.jpeg",
    "date": "2024-03-12",
    "limit": 20,
    "signed_up_count": 1,
    "signed_up_members": [
        {
            "first_name": "soso",
            "last_name": "Larote",
            "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
        }
    ]
}
```

</details>

<details>
<summary><h4>Delete a specific activity:</h4></summary>

```http
  DELETE /digital_medlemsordning/delete_activity/{ID}/
```

| Parameter   | Type     | Description                       |
|:------------|:---------|:----------------------------------|
| `activityID`| `string` | **Required**. The Activity ID     |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Activity deleted successfully"
}
```

</details>

<details>
<summary><h4>Sign up a member to an activity:</h4></summary>

```http
  POST /digital_medlemsordning/sign_up_activity/
```

| Parameter   | Type     | Description                       |
|:------------|:---------|:----------------------------------|
| `auth0ID`   | `string` | **Required**. The Members Auth0ID |
| `activityID`| `string` | **Required**. The Activity ID     |

##### Example POST-Body:
```json
{
    "auth0_id": "auth0|661a52a2cad534c6e30e3c37",
    "activity_id": 75
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "User signed up for the activity successfully"
}
```

</details>

<details>
<summary><h4>Unregister a member from an activity:</h4></summary>

```http
  POST /digital_medlemsordning/undo_signup_activity/
```

| Parameter    | Type     | Description                        |
|:-------------|:---------|:-----------------------------------|
| `auth0ID`    | `string` | **Required**. The Members Auth0ID  |
| `userID`     | `string` | **Optional**. The Members User ID  |
| `activityID` | `string` | **Optional**. The Activity ID      |

- Either auth0ID or userID must be provided, but not both.

##### Example POST-Body:
```json
{
    "auth0_id": "auth0|661a52a2cad534c6e30e3c37",
    "activity_id": 75
}
```

##### Example POST-Body:
```json
{
    "user_id": "45",
    "activity_id": 75
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "Sign-up undone successfully"
}
```

</details>

<details>
<summary><h4>Retrieve all registered members for a specific activity:</h4></summary>

```http
  GET /digital_medlemsordning/get_signed_up_members/{activityID}/
```

| Parameter    | Type     | Description                     |
|:-------------|:---------|:--------------------------------|
| `activityID` | `string` | **Optional**. The Activity ID   |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "activity_id": 77,
    "activity_title": "skydive",
    "sign_up_members": [
        {
            "user_id": 299,
            "first_name": "Miles",
            "last_name": "Larote",
            "birthdate": "2001-12-30",
            "profile_pic": "/media/profile_pics/bevis.png"
        },
        {
            "user_id": 289,
            "first_name": "John",
            "last_name": "Davies",
            "birthdate": "2006-04-16",
            "profile_pic": "/media/profile_pics/default_profile_picture.png"
        },
        ...
    ]
}
```

</details>

<details>
<summary><h4>Retrieve all activites a specific member is registered for:</h4></summary>

```http
  GET /get_member_activites/{auth0ID}/
```

| Parameter    | Type     | Description                        |
|:-------------|:---------|:-----------------------------------|
| `auth0ID`    | `string` | **Required**. The Members Auth0ID  |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "activityID": 77,
        "title": "skydive",
        "description": "skydive",
        "image": "/media/activity_pics/skydive.jpeg",
        "date": "2024-05-09",
        "limit": null,
        "signed_up_count": 2,
        "signed_up_members": [
            {
                "first_name": "soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            },
            {
                "first_name": "Chris",
                "last_name": "wfwfwf",
                "auth0ID": "auth0|661a52a2cad534c6e30e3c37"
            }
        ]
    },
    {
        "activityID": 79,
        "title": "Basketball",
        "description": "Tournement in Oslo at 5 PM",
        "image": "/media/activity_pics/basket.jpeg",
        "date": "2024-05-09",
        "limit": 20,
        "signed_up_count": 1,
        "signed_up_members": [
            {
                "first_name": "soso",
                "last_name": "Larote",
                "auth0ID": "auth0|661e47baf4c703e30aaee8fc"
            }
        ]
    },
    ...
]
```

</details>

<details>
<summary><h4>Create a new member:</h4></summary>

```http
  POST /digital_medlemsordning/register_user/
```

| Parameter        | Type     | Description                          |
|:-----------------|:---------|:-------------------------------------|
| `auth0id`        | `string` | **Required**. The Members Auth0ID    |
| `first_name`     | `string` | **Required**. Members first name     |
| `last_name`      | `string` | **Required**. Members last name      |
| `birthdate`      | `string` | **Required**. Members birthdate      |
| `gender`         | `string` | **Required**. Members gneder         |
| `phone_number`   | `string` | **Required**. Members phone number   |
| `email`          | `string` | **Required**. Members email          |
| `guardian_name`  | `string` | **Optional**. Members guardian name  |
| `guardian_phone` | `string` | **Optional**. Members guardian phone |

- Gender options: gutt | jente | ikke-Binær | vil ikke si

##### Example POST-Body:
```json
{
    "auth0id": "auth",
    "first_name": "Samuel",
    "last_name": "Samson",
    "birthdate": "2002-09-05",
    "phone_number": "12344321",
    "gender": "gutt",
    "email": "lol@hotmail.com"
}
```

##### Example POST-Body:
```json
{
    "auth0id": "auth",
    "first_name": "Samuel",
    "last_name": "Samson",
    "birthdate": "2002-09-05",
    "phone_number": "12344321",
    "gender": "gutt",
    "email": "lol@hotmail.com",
    "guardian_name": "Miles",
    "guardian_phone": "987654321"
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `201 Created`| `application/json` |

##### Example Response Body:
```json
{
    "message": "Added new user"
}
```

</details>

<details>
<summary><h4>Delete a specific member:</h4></summary>

```http
  DELETE /digital_medlemsordning/delete_member/{auth0ID}/
```

| Parameter | Type     | Description                        |
|:----------|:---------|:-----------------------------------|
| `auth0ID` | `string` | **Required**. The Members Auth0ID  |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Member deleted successfully"
}
```

</details>

<details>
<summary><h4>Retrieve Member attendence for specific date: </h4></summary>

```http
  GET /digital_medlemsordning/get_member_attendance/?date={date}
```

| Parameter    | Type     | Description          | Default value  |
|:-------------|:---------|:---------------------|:---------------| 
| `date`       | `string` | **Optional**. Date   | `Current Date` | 

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Member attendance for 2024-04-06 retrieved successfully.",
    "members_present": [
        {
            "name": "Rodger Smith",
            "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg"
        },
        {
            "name": "Lisa Stevens",
            "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg"
        },
        {
            "name": "John Conway",
            "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg"
        },
        {
            "name": "Norm Sandington",
            "profile_pic": "/media/profile_pics/portofino_2464491k_qiVdymd.jpg"
        },
        {
            "name": "Samantha Pilkington",
            "profile_pic": "/media/profile_pics/81zm9tKLsxL._AC_SL1170__JIVQUhu.jpg"
        }
    ]
}
```

</details>

<details>
<summary><h4>Retrieve member attendence statistics for a given time period:</h4></summary>

```http
  GET /digital_medlemsordning/member_attendance_stats/?start_date={start_date}&end_date={end_date}
```

| Parameter | Type        | Description                     | Default value  |
|:-------------|:---------|:--------------------------------|:---------------| 
| `start_date` | `string` | **Required**. Starting date     | `Current Date` |
| `end_date`   | `string` | **Required**. End date          | `Current Date` |             

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "total_attendance": 19,
    "attendance_by_gender": {
        "vil ikke si": 3,
        "jente": 6,
        "gutt": 9,
        "ikke-binær": 1
    }
}
```

</details>

<details>
<summary><h4>Retrieve member dashboard information about a specific member:</h4></summary>

```http
  GET digital_medlemsordning/get_member/{auth0ID}/
```

| Parameter | Type     | Description                     |
|:----------|:---------|:--------------------------------|
| `auth0ID` | `string` | **Required**. Auth0ID of member |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "member": {
        "first_name": "CHRIS",
        "level": "Invincible",
        "profile_color": "red",
        "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
        "banned_from": "2024-05-10",
        "banned_until": "2024-05-12",
        "role": "member"
    }
}
```

</details>


<details>
<summary><h4>Retrieve member dashboard information for all members:</h4></summary>

```http
  GET digital_medlemsordning/get_all_members/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "date": "2024-05-11",
    "members": [
        {
            "first_name": "JOHN",
            "level": "Invincible",
            "profile_color": "green",
            "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
            "banned_from": null,
            "banned_until": null,
            "role": "member"
        },
        {
            "first_name": "SALLY",
            "level": "Rookie",
            "profile_color": "green",
            "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
            "banned_from": null,
            "banned_until": null,
            "role": "member"
        },
        ...
    ]
}
```

</details>

<details>
<summary><h4>Search for a member based on first or last name:</h4></summary>

```http
  GET /digital_medlemsordning/search_member/?name={name}
```

| Parameter | Type        | Description               |
|:----------|:---------|:-----------------------------|
| `name`    | `string` | **Required**. Name of member |

* Case insensitive. 
* Retrievs any member whos first or last name contains the required string paramater.

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "userID": 69,
        "auth0ID": "auth0|65e06e072cc8113ba2d5cdea",
        "first_name": "John",
        "last_name": "Smith",
        "birthdate": "2002-09-05",
        "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
        "gender": "gutt",
        "points": 101,
        "phone_number": "12345678",
        "email": "testing@gmail.com",
        "guardian_name": null,
        "guardian_phone": null,
        "verified": true,
        "banned": true,
        "banned_from": "2024-05-10",
        "banned_until": "2024-05-12",
        "info": "",
        "role": "member"
    },
    {
        "userID": 119,
        "auth0ID": "auth0|65f9cb6b6b09e9bfdc447d30",
        "first_name": "Larry",
        "last_name": "Johnsen",
        "birthdate": "2006-03-06",
        "profile_pic": "/media/profile_pics/81zm9tKLsxL._AC_SL1170__JIVQUhu.jpg",
        "gender": "gutt",
        "points": 5,
        "phone_number": "12345678",
        "email": "chrisa2511@gmail.com",
        "guardian_name": "",
        "guardian_phone": "",
        "verified": false,
        "banned": false,
        "banned_from": null,
        "banned_until": null,
        "info": "",
        "role": "member"
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve all information of all members:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_members_info/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "userID": 54,
        "auth0ID": "auth0|65ef275a34065d2b94cc1d8d",
        "first_name": "Mia",
        "last_name": "Bird",
        "birthdate": "2007-01-01",
        "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
        "gender": "jente",
        "points": 5,
        "phone_number": "43675543",
        "email": "mia@gmail.com",
        "guardian_name": "",
        "guardian_phone": "",
        "verified": true,
        "banned": false,
        "banned_from": null,
        "banned_until": null,
        "info": "nøkkel til klubbhus",
        "role": "member"
    },
    {
        "userID": 55,
        "auth0ID": "auth0|65ef289190350a753bf985ae",
        "first_name": "Michael",
        "last_name": "Larson",
        "birthdate": "2008-01-07",
        "profile_pic": "/media/profile_pics/Default_Profile_Picture.jpg",
        "gender": "gutt",
        "points": 0,
        "phone_number": "20122310",
        "email": "larson54@gmail.com",
        "guardian_name": "",
        "guardian_phone": "",
        "verified": true,
        "banned": false,
        "banned_from": null,
        "banned_until": null,
        "info": "",
        "role": "member"
    },
    ...
]
```

</details>

<details>
<summary><h4>Ban a member:</h4></summary>

```http
  PUT /digital_medlemsordning/ban_member/{auth0ID}/
```

| Parameter     | Type     | Description                             |
|:--------------|:---------|:----------------------------------------|
| `auth0ID`     | `string` | **Required**. Auth0ID of member         |
| `banned_from` | `string` | **Required**. Start date of member ban  |
| `banned_until`| `string` | **Required**. End date of member ban    |

##### Example PUT-Body:
```json
{
    "banned_from": "2024-05-11",
    "banned_until": "2024-05-26"
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Member banned successfully from 2024-05-11 until 2024-05-26"
}
```

</details>

<details>
<summary><h4>Unban a member:</h4></summary>

```http
  PUT /digital_medlemsordning/unban_member/{auth0ID}/
```

| Parameter | Type        | Description                  |
|:----------|:---------|:--------------------------------|
| `auth0ID` | `string` | **Required**. Auth0ID of member |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Member unbanned successfully"
}
```

</details>

<details>
<summary><h4>Retrieve all banned members:</h4></summary>

```http
  GET /digital_medlemsordning/get_banned_members/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Banned members retrieved successfully.",
    "banned_members": [
        {
            "full_name": "John Smith",
            "profile_picture": "/media/profile_pics/Default_Profile_Picture.jpg",
            "banned_from": "2024-05-11",
            "banned_until": "2024-05-26",
            "auth0_id": "auth0|65f9cv6b6b0ee9bfdc447d25"
        },
        {
            "full_name": "Lilly Hammond",
            "profile_picture": "/media/profile_pics/Default_Profile_Picture.jpg",
            "banned_from": "2024-05-07",
            "banned_until": "2024-05-14",
            "auth0_id": "auth0|65f9cb6b6b09e9bfdc447d30"
        },
        ...
    ]
}
```

</details>

<details>
<summary><h4>Adjust the points of a member:</h4></summary>

```http
  PUT /digital_medlemsordning/adjust_member_points_total/{auth0ID}/
```

| Parameter           | Type     | Description                     |
|:--------------------|:---------|:--------------------------------|
| `auth0ID`           | `string` | **Required**. Auth0ID of member |
| `points`            | `int`    | **Required**. Number of points  |


##### Example POST-Body:
```json
{
    "points": 10
}
```

##### Example POST-Body:
```json
{
    "points": -10
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `201 Created`| `application/json` |

##### Example Response Body:
```json
{
    "message": "Member points altered"
}
```

</details>

<details>
<summary><h4>Add info to specific member:</h4></summary>

```http
  PUT /digital_medlemsordning/add_member_info/{auth0ID}/
```

| Parameter | Type        | Description                  |
|:----------|:---------|:--------------------------------|
| `auth0ID` | `string` | **Required**. Auth0ID of member |

##### Example PUT-Body:
```json
{
    "info": "Ability to acces club on saturdays"
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "auth0ID": "auth0|661a52a2cad534c6e30e3c37",
    "info": "Ability to acces club on saturdays"
}
```

</details>

<details>
<summary><h4>Remove info from a specific member:</h4></summary>

```http
  PUT /digital_medlemsordning/remove_member_info/{auth0ID}/
```

| Parameter | Type        | Description                  |
|:----------|:---------|:--------------------------------|
| `auth0ID` | `string` | **Required**. Auth0ID of member |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "auth0ID": "auth0|661a52a2cad534c6e30e3c37",
    "info": ""
}
```

</details>

<details>
<summary><h4>Retrieve all members with info:</h4></summary>

```http
  GET /digital_medlemsordning/get_members_with_info/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "auth0ID": "auth0|65ef275a34065d2b94cc1d8d",
        "first_name": "John",
        "last_name": "Pilkington",
        "info": "Key to clubhouse"
    },
    {
        "auth0ID": "auth0|661711a8bdf844868576402b",
        "first_name": "Mia",
        "last_name": "Davies",
        "info": "Allowed to access clubhouse on saturdays"
    },
    ...
]
```

</details>

<details>
<summary><h4>Retrieve all unverified members:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_unverified_members/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "auth0ID": "auth0|65ef275a34065d2b94cc1d8d",
        "birthdate": "2004-01-01",
        "first_name": "James",
        "last_name": " Kahn",
        "guardian_name": "",
        "guardian_phone": ""
    },
    {
        "auth0ID": "auth0|65ef289190350a753bf985ae",
        "birthdate": "2011-05-07",
        "first_name": "Lisa",
        "last_name": "Danilson",
        "guardian_name": "Laila Danilson",
        "guardian_phone": "43892312"
    },
    ...
]
```

</details>

<details>
<summary><h4>Verify a member:</h4></summary>

```http
  PUT /digital_medlemsordning/verify_member/{auth0ID}/
```

| Parameter | Type     | Description                     |
|:----------|:---------|:--------------------------------|
| `auth0ID` | `string` | **Required**. Auth0ID of member |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Member successfully verified"
}
```

</details>

<details>
<summary><h4>Register attendence for a specific member:</h4></summary>

```http
  POST /digital_medlemsordning/add_day/{auth0ID}/
```

| Parameter    | Type     | Description                     |
|:-------------|:---------|:--------------------------------|
| `auth0ID`    | `string` | **Required**. Auth0ID of member |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Successfully registred members attendence"
}
```

</details>

<details>
<summary><h4>Upload member porfile picture:</h4></summary>

```http
  PATCH /digital_medlemsordning/upload_profile_picture/{auth0ID}/
```

| Content-Type                      |
|-----------------------------------|
|`application/multipart/form-data`  |

| Parameter    | Type     | Description                     |
|:-------------|:---------|:--------------------------------|
| `auth0ID`    | `string` | **Required**. Auth0ID of member |
| `profile_pic`| `file`   | **Required**. Profile picture   |

##### Example PATCH-Body:
```json
{
    "profile_pic": "profile_pic_.jpg"
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Profile picture updated successfully"
}
```

</details>

<details>
<summary><h4>Upload a member certificate:</h4></summary>

```http
  POST /digital_medlemsordning/upload_member_certificates/{auth0ID}/
```

| Content-Type                      |
|-----------------------------------|
|`application/multipart/form-data`  |

| Parameter           | Type     | Description                     |
|:--------------------|:---------|:--------------------------------|
| `auth0ID`           | `string` | **Required**. Auth0ID of member |
| `certificate_image` | `file`   | **Required**. Certificate image |
| `certificate_name`  | `string` | **Required**. Certificate name  |

##### Example POST-Body:
```json
{
    "certificate_image": "dj_certificate_.jpg",
    "certificate_name": "dj certificate"
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `201 Created`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Certificate uploaded successfully"
}
```

</details>

<details>

<summary><h4>Get a specific members certificates:</h4></summary>

```http
  GET /digital_medlemsordning/get_member_certificates/{auth0ID}/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

| Parameter    | Type     | Description                     |
|:-------------|:---------|:--------------------------------|
| `auth0ID`    | `string` | **Required**. Auth0ID of member |

##### Example Response Body:
```json
[
    {
        "certificateID": 16,
        "certificate_image": "/media/certificates/New-York-Skyline-Big-Bus-Tours-Jan-2018_jaMkaEM.jpg",
        "certificate_name": "test_certificate3"
    },
    {
        "certificateID": 17,
        "certificate_image": "/media/certificates/portofino_2464491k_fue2eAB.jpg",
        "certificate_name": "test_certificate3"
    },
    ...
]
```

</details>

<details>
<summary><h4>Delete a specific certificate</h4></summary>

```http
  DELETE /digital_medlemsordning/delete_member_certificate/{certificateID}/
```

| Parameter       | Type     | Description                       |
|:----------------|:---------|:----------------------------------|
| `certificateID` | `string` | **Required**. ID of a certificate |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Certificate deleted successfully"
}
```

</details>

<details>
<summary><h4>Create a new level:</h4></summary>

```http
  POST /digital_medlemsordning/create_level/
```

| Parameter | Type     | Description                       |
|:----------|:---------|:----------------------------------|
| `name`    | `string` | **Required**. Name of the level   |
| `points`  | `string` | **Required**. Points of the level |

##### Example POST-Body:
```json
{
    "name": "Invincible",
    "points": 120
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "Level successfully created"
}
```

</details>

<details>
<summary><h4>Retrieve all levels:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_levels/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "levelID": 49,
        "name": "Legend",
        "points": 100
    },
    {
        "levelID": 50,
        "name": "Pro",
        "points": 80
    },
    {
        "levelID": 51,
        "name": "Intermediate",
        "points": 60
    },
    {
        "levelID": 52,
        "name": "Rookie",
        "points": 40
    },
    {
        "levelID": 53,
        "name": "Noob",
        "points": 20
    },
    {
        "levelID": 56,
        "name": "Invincible",
        "points": 120
    },
    ...
]
```

</details>

<details>
<summary><h4>Edit a specific level:</h4></summary>

```http
  PUT /digital_medlemsordning/edit_level/{levelID}/
```

| Parameter | Type        | Description                     |
|:----------|:------------|:--------------------------------|
| `auth0ID` | `string`    | **Required**. Auth0ID of member |
| `levelID` | `string`    | **Required**. ID of a level     |

##### Example PUT-Body:
```json
{
    "name": "Invincible",
    "points": 110
}
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Level updated successfully"
}
```

</details>

<details>
<summary><h4>Delete a specific level</h4></summary>

```http
  DELETE /digital_medlemsordning/delete_level/{levelID}/
```

| Parameter | Type        | Description                  |
|:----------|:------------|:-----------------------------|
| `levelID` | `string`    | **Required**. ID of a level  |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Level deleted successfully"
}
```

</details>

<details>
<summary><h4>Create a new suggestion:</h4></summary>

```http
  POST /digital_medlemsordning/create_suggestion/
```

| Parameter      | Type     | Description                              |
|:---------------|:---------|:-----------------------------------------|
| `title`        | `string` | **Required**. Ttile of suggestion        |
| `description`  | `string` | **Required**. Description of suggestion  |

##### Example POST-Body:
```json
{
    "title": "Trip to Tekninsk Museum",
    "description": "It would be great if we could go and visit Teknisk museum during the summer"
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "suggestionID": 56,
    "title": "Trip to Tekninsk Museum",
    "description": "It would be great if we could go and visit Teknisk museum during the summer"
}
```

</details>

<details>
<summary><h4>Retrieve all suggestions:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_suggestions/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
[
    {
        "suggestionID": 15,
        "title": "Celebrate birthday",
        "description": "Marcus has his birthay comming up. I want us to have a party for him."
    },
    {
        "suggestionID": 56,
        "title": "Trip to Tekninsk Museum",
        "description": "It would be great if we could go and visit Teknisk museum during the summer."
    }
    ...
]
```

</details>

<details>
<summary><h4>Delete a specific suggestion:</h4></summary>

```http
  DELETE /digital_medlemsordning/delete_suggestion/{suggestionID}/
```

| Parameter      | Type     | Description                       |
|:---------------|:---------|:----------------------------------|
| `suggestionID` | `string` | **Required**. The Suggestion ID   |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Suggestion deleted successfully"
}
```

</details>

<details>
<summary><h4>Create a new question and corresponding answers:</h4></summary>

```http
  POST /digital_medlemsordning/create_question/
```

| Parameter      | Type       | Description                            |
|:---------------|:-----------|:---------------------------------------|
| `question`     | `string`   | **Required**. Questiion                |
| `answers`      | `[string]` | **Required**. Answers to the question  |

##### Example POST-Body:
```json
{
  "question": "Which month",
  "answers": [
    {"answer": "January"},
    {"answer": "February"},
    {"answer": "March"},
    {"answer": "April"},
    {"answer": "May"}
  ]
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "Question and answers successfully created."
}
```

</details>

<details>
<summary><h4>Retrieve all questions with corresponding answers:</h4></summary>

```http
  GET /digital_medlemsordning/get_all_questions/
```

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "questions": [
        {
            "questionID": 37,
            "question": "Who is the author of 'To Kill a Mockingbird'?",
            "answers": [
                {
                    "answer_id": 109,
                    "answer_text": "Harper Lee"
                },
                {
                    "answer_id": 110,
                    "answer_text": "J.K. Rowling"
                },
                {
                    "answer_id": 111,
                    "answer_text": "Stephen King"
                }
            ]
        },
        {
            "questionID": 42,
            "question": "What is the capital city of Australia?",
            "answers": [
                {
                    "answer_id": 124,
                    "answer_text": "Sydney"
                },
                {
                    "answer_id": 125,
                    "answer_text": "Melbourne"
                },
                {
                    "answer_id": 126,
                    "answer_text": "Canberra"
                },
                {
                    "answer_id": 127,
                    "answer_text": "Perth"
                },
                {
                    "answer_id": 128,
                    "answer_text": "Brisbane"
                }
            ]
        },
        ...
    ]
}
```

</details>

<details>
<summary><h4>Answer a question:</h4></summary>

```http
  POST /digital_medlemsordning/submit_response/{auth0ID}/
```

| Parameter    | Type       | Description                      |
|:-------------|:-----------|:---------------------------------|
| `auth0ID`    | `string`   | **Required**. Auth0ID of member  |
| `question`   | `string`   | **Required**. ID of question     |
| `answers`    | `[string]` | **Required**. ID of answer       |

##### Example POST-Body:
```json
{
    "question": "40",
    "answer": "118"
}
```

#### Response:

| Status Code   | Content-Type       |
|:--------------|:-------------------|
| `201 Created` | `application/json` |

##### Example Response Body:
```json
{
    "message": "User response submitted successfully."
}
```

</details>

<details>
<summary><h4>Retrieve answer count for specific question:</h4></summary>

```http
  GET /digital_medlemsordning/get_question_responses/{questionID}/
```

| Parameter    | Type         | Description                  |
|:-------------|:-------------|:-----------------------------|
| `questionID` | `string`   | **Required**. ID of question   |


#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "message": "Answer counts retrieved successfully",
    "question": "Which state is the largest in the US",
    "answer_counts": {
        "Texas": 15,
        "Alaska": 18,
        "Main": 0,
        "New York": 12,
        "California": 9
    }
}
```

</details>

<details>
<summary><h4>Delete a specific question:</h4></summary>

```http
  DELETE digital_medlemsordning/delete_question/{questionID}/
```

| Parameter   | Type     | Description                       |
|:------------|:---------|:----------------------------------|
| `questionD` | `string` | **Required**. The Question ID     |

#### Response:

| Status Code   | `204 No Content`   |
|:--------------|:-------------------|

##### Example Response Body:
```json
{
    "message": "Question deleted successfully"
}
```

</details>

<details>
<summary><h4>Retrieve member registration status:</h4></summary>

```http
  GET /digital_medlemsordning/check_user_registration_status/?sub={auth0ID}
```

| Parameter    | Type       | Description                      |
|:-------------|:-----------|:---------------------------------|
| `auth0ID`    | `string`   | **Required**. Auth0ID of member  |

#### Response:

| Status Code  | Content-Type       |
|:-------------|:-------------------|
| `200 OK`     | `application/json` |

##### Example Response Body:
```json
{
    "registered": true
}
```

</details>