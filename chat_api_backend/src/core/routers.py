from rest_framework import routers
from src.message_control.urls import router as message_router
from src.user_control.urls import router as user_router


router = routers.DefaultRouter()
router.registry.extend(message_router.registry)
router.registry.extend(user_router.registry)
