from wfs_trx import (
    insert_point,
    update,
    delete
)


ns = [{
    "key":"xmlns:osm",
    "val": "www.osm.com"
}]
ft = "osm:events"
ps = [{
    "key": "event_id",
    "val": 1001
},{
    "key": "event_type",
    "val": "slogan"
}]
p = (-3.5, -1)


insert_point(
    namespaces=ns,
    featureType=ft,
    props=ps,
    point=p)


update(
    fid="events.51",
    namespaces=ns,
    typeName="osm:events",
    props=ps)


delete(
    fid="events.51",
    namespaces=ns,
    typeName="osm:events")
