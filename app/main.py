from fastapi import FastAPI

#create an instance of FastAPI and customize metadata configurations
app = FastAPI(
        docs_url='/api/docs', #set the URL for the API documentation
        openapi_url='/api/openapi', #set the URL for the OpenAPI schema
        redoc_url=None, #disable the ReDoc documentation
        title='HealthCheck', #set the title of the API
        description='**HealthCheck** used to check if the *API* service works as expected for your [FastAPI](https://fastapi.tiangolo.com).', #set the description of the API
        summary='Health check for your FastAPI.', #set a summary for the API
        version='0.0.1', #set the version of the API
        contact={ #set the contact information for the API
            'name': 'HealthCheck',
            'url': 'https://github.com/antenehbedilu/healthcheck',
            'email': 'hello@antenehbedilu.com'
            }, 
        license_info={ #set the license information for the API
            'name': 'MIT License',
            'url': 'https://raw.githubusercontent.com/antenehbedilu/healthcheck/main/LICENSE'
            }
        )
