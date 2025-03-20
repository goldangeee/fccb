from django.shortcuts import render
from django.http import JsonResponse

import requests

def get_game_data(request):
    api_key = ''  # 여기에 API 키를 입력하세요.
    url = 'https://open.api.nexon.com/static/fconline/meta/spid.json'  # 실제 엔드포인트로 변경하세요.
    
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)
