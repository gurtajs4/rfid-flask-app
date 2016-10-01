function appLocation() {
    return {
        restrict: 'E',
        scope: {
            label: '='
        },
        templateUrL: 'app-location.html',
        controller: 'AppLocationController',
    };
}

angular.module('appMain').directive('appLocation', appLocation);