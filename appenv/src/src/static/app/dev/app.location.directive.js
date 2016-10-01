function appLocation() {
    return {
        restrict: 'E',
        scope: false,
        templateUrL: 'app-location.html',
        controller: 'AppLocationController',
    };
}

angular.module('appMain').directive('appLocation', appLocation);