import time
import traceback
import logging
from fastapi import Request
from datetime import datetime
from fastapi.responses import JSONResponse


# Set up the logging configuration

#It get the 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  
ch = logging.StreamHandler()  # Logs to the console
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

async def global_exception_handler(request: Request, call_next):
    
    start_time = time.time()
    try:
        # Process the request
        response = await call_next(request)
        # return response
    except Exception as e:
        # Capture the exception and traceback
        tb = traceback.format_exc()
        error_type = type(e).__name__
        
        #It return the error 
        logger.error(
            f"Error occurred while processing {request.method} request to {request.url.path}: "
            f"{error_type} - {str(e)}\nTraceback: {tb}"
        )


        # Return JSON response with error details
        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal Server Error",
                "error_type": error_type,
                "error_message": str(e),
                "trace": tb,
            },
        )
    # Calculate the response time in seconds
    duration = time.time() - start_time
    log_entry = {
        "path": request.url.path,
        "method": request.method,
        "response_time_seconds": round(duration, 2)  # Response time in seconds
    }
    
    
    #It gives the basic info of particular request
    logger.info(
            f"Processed {request.method} request to {request.url.path} in {round(duration, 2)} seconds"
        )

    return response
