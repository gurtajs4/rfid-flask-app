(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', '$timeout', 'readerService'];
    function ReaderController($scope, $timeout, readerService) {
        var service = readerService;

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                $timeout(function () {
                    $scope.tagData = response.data['data'];
                    $scope.message = response.data['message'];
                }, 0);
            });
        }
    }
})();