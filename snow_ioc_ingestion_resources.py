import options


def get_ioc_ingestion_result(file_name: str, request_id: str):
    if file_name == options.VALID_FILE_NAME:
        return {
            "rawData": {
                "meta": {
                    'image_url': 'https://www.servicenow.com/content/dam/servicenow-assets/images/'
                                 'meganav/servicenow-header-logo.svg',
                    "title": options.VALID_FILE_RESULT.format(request_id)
                }
            }}
    elif file_name == options.INVALID_FILE_NAME:
        return {"text": options.INVALID_FILE_RESULT}
    if file_name == options.NO_REQRD_FIELDS_FILE_NAME:
        return {"text": options.NO_FIELDS_REQRD_FILE_RESULT}
