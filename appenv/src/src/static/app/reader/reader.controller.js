(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', '$log', '$timeout', 'readerService'];
    function ReaderController($scope, $log, $timeout, readerService) {
        var service = readerService;
        // var self = this;
        // self.tagData = "";
        // self.message = "";
        $scope.tagData = "";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                $log.info(response.data);
                $timeout(function () {
                    // var tData = response.data.data.toString();
                    var tData = response.data.data;
                    var tMessage = response.data.message;
                    // $scope.$apply(function () {
                    //     self.tagData = tData;
                    //     self.message = tMessage;
                    //     $scope.tagData = tData;
                    //     $scope.message = tMessage;
                    // });
                    $scope.$apply(function () {
                        $scope.message = tMessage;
                        $scope.tagData = tData;
                    });
                    // console.log(self.tagData);
                    // console.log(self.message);
                    $log.info($scope.tagData);
                    $log.info($scope.message);
                }, 0);
            });
        }
    }
})();