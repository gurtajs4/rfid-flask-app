function navBar() {
    return {
        restrict: 'E',
        scope: {
            tab: "="
        },
        templateUrl: '/navigation/navigation.html',
        controller: 'NavController'
    };
}

angular.module('appMain').directive('navBar', navBar);