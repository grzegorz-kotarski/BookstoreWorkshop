
## Database

### Run

    docker run -e POSTGRES_DB=dev_database -e POSTGRES_USER=dev_user -e POSTGRES_PASSWORD=dev_user -p 5432:5432 -d postgres:14

### Enter bash

    docker exec -ti <container_id> /bin/bash

### Stop database

    docker stop <container_id>

### Start stopped database

    docker start <container_id>

## Application

### Run

#### Development mode

    WORKSHOP_DB_URL="postgresql+psycopg2://dev_user:dev_user@0.0.0.0/dev_database" uvicorn workshop:app --reload 

#### Production mode

    WORKSHOP_DB_URL="postgresql+psycopg2://dev_user:dev_user@0.0.0.0/dev_database" python -m workshop <parameters>
