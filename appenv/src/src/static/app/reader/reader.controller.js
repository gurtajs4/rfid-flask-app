(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', 'readerService'];
    function ReaderController($scope, readerService) {
        var service = readerService;

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                $scope.apply(function () {
                    $scope.tagData = response.data['data'];
                    $scope.message = response.data['message'];
                });
            });
        }
    }
})();