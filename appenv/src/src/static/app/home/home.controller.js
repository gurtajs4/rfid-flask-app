function HomeController($scope) {
    $scope.message = 'Welcome! This the web application interface of the keys management system';
}

HomeController.$inject = ['$scope'];
angular.module('appMain').controller('HomeController', HomeController);