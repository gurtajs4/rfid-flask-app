function MainController($scope) {
    $scope.tab = 0;
}

MainController.$inject = ['$scope'];
angular.module('appMain').controller('MainController', MainController);