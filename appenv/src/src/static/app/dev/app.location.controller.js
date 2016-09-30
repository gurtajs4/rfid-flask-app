var appBaseUrl = angular.element(document.querySelector('base')).attr('href');

function AppLocationController($scope) {
    $scope.label = appBaseUrl;
}

AppLocationController.$inject = ['$scope'];
angular.module('appMain').controller('AppLocationController', AppLocationController);