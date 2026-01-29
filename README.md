# StayNear

StayNear is a Django-based web application for managing property listings and landlord information.

## Features
- Property listings management
- Landlord management
- User authentication
- Admin interface

## Project Structure
- `main/` - Main app logic
- `landlords/` - Landlord-related features
- `listings/` - Property listings features
- `staynear/` - Project configuration

## Setup
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd StayNear
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Requirements
- Python 3.10+
- Django 5.2.6

## License
MIT License
