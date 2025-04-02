# Project Name
Landbot Challenge 

## Configuration
- Slack token should be in environment variable `SLACK_TOKEN`

## Architecture
- Built using Hexagonal Architecture to maintain isolation from the framework
- Easy portability between frameworks (e.g., current framework to FastAPI)
- Dependencies are managed via dependency_injector in `container.py`
- Custom exception handling implemented through exception filters
- haelth endpoint for health check

## Testing
- API tests: Validate endpoint functionality
    - python3 manage.py test
- APP tests: Cover business logic (framework-independent)
    - pytest

## Performance Considerations
### Slack Integration
Currently implements synchronous requests for simplicity. Two potential optimization paths:

1. **Celery Implementation**
   - Simple queue-based solution
   - ChannelEmitter wrapper prepared for write once celery specific code

2. **Microservices Approach**
   - Event-driven architecture using `SlackAssistanceRequested` domain events
   - Queue-based communication between services
   - Allows for separate Slack handling microservice

## Getting Started
Docker image can be build using `build_docker_image.sh` 

