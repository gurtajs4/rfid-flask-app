function appLocation() {
    return {
        restrict: 'E',
        scope: true,
        templateUrL: '/dev/app-location.html',
        controller: 'AppLocationController',
        controllerAs: 'appLoc'
    };
}

angular.module('appMain').directive('appLocation', appLocation);