from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from django.urls import path

# Конфигурируем Django (без отдельного settings.py)
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    SECRET_KEY="supersecret",
    INSTALLED_APPS=["rest_framework"],
    MIDDLEWARE=[],
    REST_FRAMEWORK={},  # Добавляем настройку REST_FRAMEWORK
)

@api_view(["POST"])
def process_numbers(request):
    numbers = request.data.get("numbers", [])

    if not isinstance(numbers, list) or len(numbers) != 3:
        return Response({"error": "Передай три числа в массиве"}, status=400)

    width, height, depth = numbers  # Размеры параллелепипеда

    # Вершины параллелепипеда (с размерами width, height, depth)
    result = [
        0, 0, 0,
        0, height, 0,
        width, height, 0,
        width, 0, 0,
        0, 0, depth,
        0, height, depth,
        width, height, depth,
        width, 0, depth
    ]

    return Response({"success": True, "sent": result})

# Определяем URL-ы
urlpatterns = [
    path("process_numbers/", process_numbers),
]

# Создаем WSGI-приложение
application = get_wsgi_application()
