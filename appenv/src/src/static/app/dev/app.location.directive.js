function appLocation() {
    return {
        restrict: 'E',
        scope: true,
        templateUrL: '/dev/app-location.html',
        controller: 'AppLocationController'
    };
}

angular.module('appMain').directive('appLocation', appLocation);