from typing import Optional
from fastapi import APIRouter, Request

from common import string_parser
from common.response_data_handler import ResponseDataHandler
from common.data_generator import random_from_list
from error_responses import ErrorResponses
from snow_ioc_ingestion_resources import get_ioc_ingestion_result

router: APIRouter = APIRouter()
_response_data_handler: ResponseDataHandler = ResponseDataHandler(mongo=True,
                                                                      collection_name="snow_ioc_ingestion")

request_id_list: list = ['REQ0650001', 'REQ0650002', 'REQ0650003', 'REQ0650004', 'REQ0650005']
request_id: str = random_from_list(request_id_list)


@router.post('/wols2/cdc_ioc_ingestion')
async def snow_ioc_ingestion(request: Request) -> dict:
    request_data: bytes = await request.body()
    request_data: Optional[str] = string_parser.convert_byte_stream_to_string(request_data)
    if request_data:
        request_response: dict = {
            "result": "Successfully submitted request: {}".format(request_id)
        }
        return request_response


@router.get('/result/wols2/cdc_ioc_ingestion')
async def snow_ioc_ingestion_result() -> dict:
    request_response: dict = {
        "result": "Successfully submitted request: {}".format(request_id)
    }
    return request_response


@router.get('/result/extract_file_details/{file_name}')
async def extract_file_details_result(file_name: str) -> dict:
    return _response_data_handler.get_response_data_by_source(
        extract_file_details_result.__name__.replace('_', '-'),
        file_name.split('.')[0], required_query=True)


@router.get('/result/extract_json')
async def extract_json_result() -> dict:
    return _response_data_handler.get_response_data_by_source(
        extract_json_result.__name__.replace('_', '-'))


@router.get('/result/extract_file_details/{error_type}/{file_name}')
async def extract_file_details_error_result(error_type: str, file_name: str) -> dict:
    return ErrorResponses.get_extract_file_details_error_message(
        error_type=error_type, file_name=file_name)


@router.get('/result/extract_json/{error_type}')
async def extract_json_error_result(error_type: str) -> dict:
    return ErrorResponses.get_extract_json_error_message(error_type=error_type)


@router.get('/result/ioc_ingestion/{file_name}')
async def expected_ioc_ingestion_result(file_name) -> dict:
    return get_ioc_ingestion_result(file_name, request_id)