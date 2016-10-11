function MainController($scope) {
    $scope.message = "Keys storage management system - RFID tag reader application interface";
}

MainController.$inject = ['$scope'];
angular.module('appMain').controller('MainController', MainController);