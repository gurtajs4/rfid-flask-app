function HomeController($scope) {
    $scope.message = 'Home page...';
}

HomeController.$inject = ['$scope'];
angular.module('appMain').controller('HomeController', HomeController);