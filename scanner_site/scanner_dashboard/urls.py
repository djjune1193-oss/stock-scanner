from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("refresh-scanner/", views.refresh_scanner, name="refresh_scanner"),
    path('scanner/', views.scanner_view, name='scanner'),  # Scanner tab
    path('flat_bollinger/', views.flat_bollinger_view, name='flat_bollinger'), # flat_bollinger
    path("hot_ten_day/", views.hot_ten_day_view, name="hot_ten_day"),
    path("sector/", views.sector_view, name="sector"),
    path("double-bottom/", views.double_bottom_view, name="double-bottom"),
    path("turtle_soup/", views.turtle_soup_view, name="turtle_soup"),
    path("momentum_strength/", views.calculate_momentum_strength, name="momentum_strength"),
    path("chart/<str:ticker>/", views.equity_chart, name="equity_chart"),
    path("sector-chart/", views.sector_ma_chart, name="sector_chart"),
    path("industry_ranking/", views.get_industry_ranking, name="industry_ranking"),
    path("equity_ranking/", views.get_equity_ranking, name="equity_ranking"),
    path("metrics/", views.metrics_view, name="metrics"),
    path("base_breakout/", views.base_breakout_scanner, name="base_breakout"),
    path("breakout_21/", views.breakout_21_view, name="breakout_21"),
    path("documentation/", views.documentation, name="documentation"),
]
