# Music Booking API

## Overview

This is a RESTful API for a music booking platform that facilitates the process of finding, booking, and managing live music performances, gigs, and events. The platform connects **artists**, **event organizers**, and **venues** by enabling them to create profiles, list events, and handle booking transactions.

## Features

- **User Authentication** (Register, Login, JWT-based authentication)
- **Artist Profiles** (Showcase talent, genre, and availability)
- **Event Listings** (Create, view, and manage events)
- **Booking System** (Artists can accept/reject event bookings)
- **Payment Processing** (Secure transactions for bookings)
- **API Documentation** (Swagger and Postman collection for testing)

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** JWT (Simple JWT)
- **Database:** PostgreSQL (or MySQL)
- **Deployment:** Docker, Cloud Hosting (optional)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/music-booking-api.git
   cd music-booking-api
   ```

2. **Install Pipenv and dependencies:**

   ```sh
   pip install pipenv
   pipenv install --dev
   ```

3. **Set up environment variables (.env file):**

   ```sh
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=postgres://username:password@localhost:5432/music_booking_db
   ```

4. **Apply database migrations:**

   ```sh
   pipenv run python manage.py migrate
   ```

5. **Run the development server:**

   ```sh
   pipenv run python manage.py runserver
   ```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/auth/register/` | Register a new user |
| POST | `/auth/login/` | User login (returns JWT tokens) |

### Artists

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/artists/` | List all artists |
| POST | `/artists/` | Create an artist profile |
| GET | `/artists/{id}/` | Get artist details |

### Events

| Method | Endpoint | Description |
|--------|---------|-------------|
| GET | `/events/` | List all events |
| POST | `/events/` | Create an event |
| GET | `/events/{id}/` | Get event details |

### Bookings

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/bookings/` | Book an artist for an event |
| GET | `/bookings/` | View all bookings |
| PUT | `/bookings/{id}/status/` | Update booking status |

### Payments

| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/payments/` | Process payment for a booking |

## Testing

Use **Postman** or **cURL** to test the API. You can also run unit tests:

```sh
pipenv run python manage.py test
```

## API Documentation

- **Swagger UI:** [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- **Postman Collection:** Available in the repository

## Deployment (Optional)

To deploy using **Docker**:

```sh
docker build -t music-booking-api .
docker run -p 8000:8000 music-booking-api
```

## Contributors

- **Your Name** – Developer

## License

This project is licensed under the MIT License.
