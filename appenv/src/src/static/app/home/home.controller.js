(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('HomeController', HomeController);

    HomeController.$inject = ['$scope'];
    function HomeController($scope) {
        $scope.message = 'Welcome! This the web application interface of the keys management system';
    }
})();
