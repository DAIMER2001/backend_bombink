from django.urls import path
from rest_framework.routers import SimpleRouter
from products.serializers import ProductFilter
from products.views import HistoryViewSet, ImagesViewSet, ProductsSearchViewSet, ProductsViewSet

router = SimpleRouter()

router.register(r'products', ProductsViewSet)
router.register(r'productsSearch', ProductsSearchViewSet)
router.register(r'historyProducts', HistoryViewSet)
router.register(r'images', ImagesViewSet)


urlpatterns = router.urls + [
    path('productsTop/', HistoryViewSet.as_view({'get':'productsTop'})),
    # path('products/', product_list.as_view(), name='products'),
]
