import os

from sanic import response, Blueprint
from jinja2 import Environment, PackageLoader

from pubgate.db.boxes import Outbox, Inbox

gettogether_v1 = Blueprint('gettogether')


gt_dir = os.path.dirname(os.path.abspath(__file__))
gettogether_v1.static('/static', f'{gt_dir}/static')

jinja_env = Environment(
    loader=PackageLoader("gettogether", "templates"), trim_blocks=True, lstrip_blocks=True
)

# @gettogether_v1.route('/', methods=['GET'])
# async def home(request, **kwargs):
#     data = await Outbox.find(filter={
#                 "deleted": False,
#                 "activity.type": "Create"
#             },
#             sort="activity.published desc")
#     posts = Outbox.activity_clean(data.objects, striptags=True)
#
#     feddata = await Inbox.find(filter={
#                 "deleted": False,
#                 "activity.type": "Create"
#             },
#             sort="activity.published desc")
#     fedposts = Inbox.activity_clean(feddata.objects, striptags=True)
#
#     return response.html(
#         # html_minify(
#             jinja_env.get_template("home.jinja").render(
#                 static_url="static/",
#                 conf=request.app.config,
#                 localposts=posts,
#                 fedposts=fedposts
#
#             # )
#         )
#     )

@gettogether_v1.route('/', methods=['GET'])
def home(request, *args, **kwards):
    context = {}
#
#     near_distance = int(request.GET.get("distance", DEFAULT_NEAR_DISTANCE))
#     context['distance'] = near_distance
    context['geoip_lookup'] = False
    context['city_search'] = False
    context['setting']
#
#     city=None
#     ll = None
#     if "city" in request.GET and request.GET.get("city"):
#         try:
#             city_id = int(request.GET.get("city"))
#             city = City.objects.get(id=city_id)
#             context['city'] = city
#             ll = [city.latitude, city.longitude]
#             ga.add_event(request, 'homepage_search', category='search', label=city.short_name)
#             context['city_search'] = True
#         except:
#             messages.add_message(request, messages.ERROR, message=_('Could not locate the City you requested.'))
#             context['city_search'] = False
#
#     if context['city_search'] == False:
#         try:
#             g = location.get_geoip(request)
#             if g.latlng is not None and len(g.latlng) >= 2 and g.latlng[0] is not None and g.latlng[1] is not None:
#                 ll = g.latlng
#                 context['geoip_lookup'] = True
#
#                 try:
#                     city_distance = 1 #km
#                     while city is None and city_distance < 100:
#                         minlat = ll[0]-(city_distance/KM_PER_DEGREE_LAT)
#                         maxlat = ll[0]+(city_distance/KM_PER_DEGREE_LAT)
#                         minlng = ll[1]-(city_distance/(KM_PER_DEGREE_LNG*math.cos(math.radians(ll[0]))))
#                         maxlng = ll[1]+(city_distance/(KM_PER_DEGREE_LNG*math.cos(math.radians(ll[0]))))
#                         nearby_cities = City.objects.filter(latitude__gte=minlat, latitude__lte=maxlat, longitude__gte=minlng, longitude__lte=maxlng)
#                         if len(nearby_cities) == 0:
#                             city_distance += 1
#                         else:
#                             city = sorted(nearby_cities, key=lambda city: location.city_distance_from(ll, city))[0]
#
#                     if request.user.is_authenticated and request.user.profile.city is None:
#                         profile = request.user.profile
#                         profile.city = city
#                         profile.save()
#                 except Exception as err:
#                     print("City lookup failed", err)
#                     raise Exception('City lookup filed')
#             else:
#                 raise Exception('Geocoder result has no latlng')
#         except Exception as err:
#             context['geoip_lookup'] = False
#             print("Geocoder lookup failed for %s" % request.META.get('REMOTE_ADDR'), err)
#
#
#     if ll is not None:
#         context['latitude'] = ll[0]
#         context['longitude'] = ll[1]
#         try:
#             minlat = ll[0]-(near_distance/KM_PER_DEGREE_LAT)
#             maxlat = ll[0]+(near_distance/KM_PER_DEGREE_LAT)
#             minlng = ll[1]-(near_distance/(KM_PER_DEGREE_LNG*math.cos(math.radians(ll[0]))))
#             maxlng = ll[1]+(near_distance/(KM_PER_DEGREE_LNG*math.cos(math.radians(ll[0]))))
#             context['minlat'] = minlat
#             context['maxlat'] = maxlat
#             context['minlng'] = minlng
#             context['maxlng'] = maxlng
#
#             near_events = Searchable.objects.filter(latitude__gte=minlat,
#                                                     latitude__lte=maxlat,
#                                                     longitude__gte=minlng,
#                                                     longitude__lte=maxlng,
#                                                     end_time__gte=datetime.datetime.now())
#             context['near_events'] = sorted(near_events, key=lambda searchable: location.searchable_distance_from(ll, searchable))
#
# #            # If there aren't any teams in the user's geoip area, show them the closest ones
#             if context['geoip_lookup'] and len(near_events) < 1:
#                 context['closest_events'] = sorted(Searchable.objects.filter(end_time__gte=datetime.datetime.now()),
#                                                   key=lambda searchable: location.searchable_distance_from(ll, searchable))[:3]
#
#             near_teams = Team.public_objects.filter(city__latitude__gte=minlat,
#                                              city__latitude__lte=maxlat,
#                                              city__longitude__gte=minlng,
#                                              city__longitude__lte=maxlng
#                                              ).filter(Q(access=Team.PUBLIC) | Q(access=Team.PRIVATE,
#                                                                                 owner_profile=request.user.profile))
#             context['near_teams'] = sorted(near_teams, key=lambda team: location.team_distance_from(ll, team))
#
# #            # If there aren't any teams in the user's geoip area, show them the closest ones
#             if context['geoip_lookup'] and len(near_teams) < 1:
#                 context['closest_teams'] = sorted(Team.public_objects.all(), key=lambda team: location.team_distance_from(ll, team))[:3]
#         except Exception as err:
#             print("Error looking up nearby teams and events", err)
#             traceback.print_exc()
#
#     initial_search = {'distance': near_distance}
#     if city is not None and city.id > 0:
#         initial_search['city'] = city.id
#     search_form = SearchForm(initial=initial_search)
#     context['search_form'] = search_form
    # return render(request, 'get_together/index.html', context)

    return response.html(
        # html_minify(
            jinja_env.get_template("get_together/index.html").render(
                static_url="static/",
                **context
            # )
        )
    )
