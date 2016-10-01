function AppLocationController($scope) {
    var appBaseUrl = angular.element(document.querySelector('base')).attr('href');
    $scope.label = appBaseUrl;
}

AppLocationController.$inject = ['$scope'];
angular.module('appMain').controller('AppLocationController', AppLocationController);