(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', '$timeout', 'readerService'];
    function ReaderController($scope, $timeout, readerService) {
        var service = readerService;
        // var self = this;
        // self.tagData = "";
        // self.message = "";
        $scope.tagData = "";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log(response.data);
                $timeout(function () {
                    var tData = response.data.data.toString();
                    var tMessage = response.data.message;
                    // $scope.$apply(function () {
                    //     self.tagData = tData;
                    //     self.message = tMessage;
                    //     $scope.tagData = tData;
                    //     $scope.message = tMessage;
                    // });
                    $scope.$apply(function () {
                        $scope.tagData = tData;
                        $scope.message = tMessage;
                    });
                    // console.log(self.tagData);
                    // console.log(self.message);
                    console.log($scope.tagData);
                    console.log($scope.message);
                }, 0);
            });
        }
    }
})();