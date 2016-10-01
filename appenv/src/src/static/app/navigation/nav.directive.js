function navBar() {
    return {
        restrict: 'E',
        scope: true,
        templateUrl: '/navigation/navigation.html',
        controller: 'NavController'
    };
}

angular.module('appMain').directive('navBar', navBar);