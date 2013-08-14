from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from launder.views import (
	DailyOperationsView,
	WashFoldCreate,
	WashFoldUpdate,
	WashFoldList,
	WashFoldDetail,
	DryCleaningCreate,
	DryCleaningUpdate,
	DryCleaningList,
	DryCleaningDetail,
	LaundryShirtsOrderCreate,
	LaundryShirtsOrderUpdate,
	LaundryShirtsOrderList,
	LaundryShirtsOrderDetail,
)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	#daily_operations urls
	url(r'^$', DailyOperationsView.as_view()),
	#wash_fold_generic_views
	url(r'^wash_fold/add/(?P<pk>\d+)/$', WashFoldUpdate.as_view(), name='wash_fold_update'),
	url(r'^wash_fold/add/$', WashFoldCreate.as_view(), name='wash_fold_add'),
	url(r'^wash_fold/(?P<pk>\d+)/$', WashFoldDetail.as_view(), name='wash_fold_detail'),
	url(r'^wash_fold/$', WashFoldList.as_view(), name='wash_fold_list'),
	#dry_clean urls
	url(r'^dry_cleaning/add/(?P<pk>\d+)/$', DryCleaningUpdate.as_view(), name='dry_cleaning_update'),
	url(r'^dry_cleaning/add/$', DryCleaningCreate.as_view(), name='dry_cleaning_add'),
	url(r'^dry_cleaning/(?P<pk>\d+)/$', DryCleaningDetail.as_view(), name='dry_cleaning_detail'),
	url(r'^dry_cleaning/$', DryCleaningList.as_view(), name='dry_cleaning_list'),
	#shirts urls
	url(r'^shirts/add/(?P<pk>\d+)/$', LaundryShirtsOrderUpdate.as_view(), name='shirts_update'),
	url(r'^shirts/add/$', LaundryShirtsOrderCreate.as_view(), name='shirts_add'),
	url(r'^shirts/(?P<pk>\d+)/$', LaundryShirtsOrderDetail.as_view(), name='shirts_detail'),
	url(r'^shirts/$', LaundryShirtsOrderList.as_view(), name='shirts_list'),
	#index
	#url(r'^$', 'launder.views.index')
)
