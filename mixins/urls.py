from rest_framework.routers import SimpleRouter
from products.views import ProductsViewSet

router = SimpleRouter()

router.register(r'type_list', ProductsViewSet)

urlpatterns = router.urls