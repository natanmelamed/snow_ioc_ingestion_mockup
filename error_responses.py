from fastapi.responses import JSONResponse


class ErrorResponses:
    @staticmethod
    def get_user_authentication() -> JSONResponse:
        return JSONResponse(
            status_code=401,
            content={
                    "error": {
                        "message": "User Not Authenticated",
                        "detail": "Required to provide Auth information"
                    },
                    "status": "failure"
                }
        )

    @staticmethod
    def get_extract_file_details_error_message(error_type: str, file_name: str) -> dict:
        if error_type == 'file_not_present':
            return {"error_message": f'Error: File named {file_name} is not attached'}
        elif error_type == 'unique_file_required':
            return {
                "error_message": "Error: Files with same name found. Unique file name required."
            }

    @staticmethod
    def get_extract_json_error_message(error_type: str) -> dict:
        if error_type == 'missing columns':
            return {"error_message": "Error: 'Type' and 'Value' columns missing in the file"}
        elif error_type == 'missing IOCs':
            return {"error_message": "Error: IP/URL/Domain not present in the file"}




