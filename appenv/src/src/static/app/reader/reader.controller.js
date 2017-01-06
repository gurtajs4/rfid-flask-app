(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', '$timeout', 'readerService'];
    function ReaderController($scope, $timeout, readerService) {
        var service = readerService;
        $scope.tagData = "";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                var data = response.data['data'];
                var message = response.data['message'];
                $timeout(function () {
                    $scope.tagData = data;
                    $scope.message = message;
                }, 0);
            });
        }
    }
})();