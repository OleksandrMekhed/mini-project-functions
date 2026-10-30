services = [
    {"name": "nginx", "status": "OK"},
    {"name": "postgresql", "status": "OK"},
    {"name": "rabbitmq", "status": "WRONG"},
    {"name": "redis", "status": "OK"},
    {"name": "celery", "status": "OK"},
    {"name": "elasticsearch", "status": "WRONG"},
    {"name": "docker", "status": "OK"},
    {"name": "gunicorn", "status": "OK"},
    {"name": "mongodb", "status": "WRONG"},
    {"name": "memcached", "status": "OK"}
]

def get_all_services(services):
    for service in services:
        print(f"{service['name']}: {service['status']}")

def get_one_service(services):
    name = input("Enter service name: ").strip()

    for service in services:
        if service['name'] == name:
            print(f"{service['name']}: {service['status']}")
            return service

    print(f"Service '{name}' not found")