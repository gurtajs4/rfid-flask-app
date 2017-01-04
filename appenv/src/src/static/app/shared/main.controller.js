(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('MainController', MainController);

    MainController.$inject = ['$scope'];
    function MainController($scope) {
        $scope.message = "Keys storage management system - RFID tag reader application interface";
    }
})();