(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', '$log', '$timeout', 'readerService'];
    function ReaderController($scope, $log, $timeout, readerService) {
        var service = readerService;
        $scope.tagData = "";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader()
                .then(function (response) {
                    $log.info(response.data);
                    $timeout(function () {
                        var tData = response.data.data;
                        var tMessage = response.data.message;
                        $scope.$apply(function () {
                            $scope.message = tMessage;
                            $scope.tagData = tData;
                        });
                    }, 0);
                })
                .catch(function (error) {
                    $log.error('No data detected, reload page and move your tag closer to reader... ' + error.data);
                });
        }
    }
})();