function MainController($scope) {
//    $scope.tab = 0;
    $scope.message = "At least AngularJS is working in main controller...";
}

MainController.$inject = ['$scope'];
angular.module('appMain').controller('MainController', MainController);