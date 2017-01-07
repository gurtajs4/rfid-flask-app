(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['$scope', 'readerService'];
    function ReaderController($scope, readerService) {
        var service = readerService;
        $scope.tagData = "Tag ID";
        $scope.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log('Ajax response for activating reader...');
                console.log(response.data);
                console.log(response.data.message);
                console.log($scope.tagData);
                console.log($scope.message);
                setTimeout(function () {
                    $scope.$apply(function () {
                        $scope.tagData = response.data['data'];
                        $scope.message = response.data['message'];
                    });
                    console.log($scope.tagData);
                    console.log($scope.message);
                }, 0);
            });
        }
    }
})();