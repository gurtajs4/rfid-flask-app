(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', 'readerService'];
    function ReaderController($scope, readerService) {
        var service = readerService;
        $scope.tagData = "";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log(response.data);
                setTimeout(function () {
                    $scope.$apply(function () {
                        $scope.tagData = response.data.data.toString();
                        $scope.message = response.data.message;
                    });
                    console.log($scope.tagData);
                    console.log($scope.message);
                }, 0);
            });
        }
    }
})();