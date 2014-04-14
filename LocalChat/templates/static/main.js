var myMap;

ymaps.ready(init);

function init () {
    myMap = new ymaps.Map('map', {
        center:[55.76, 37.64],
        zoom:10
    });

    myCollection = new ymaps.GeoObjectCollection({}, {});
    myMap.geoObjects.add(myCollection);

    myMap.events.add('click', function(e) {
        myCollection.add(new ymaps.Placemark(e.get('coordPosition')));
    });
}