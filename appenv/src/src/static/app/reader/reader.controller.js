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
                var data = response.data['data'];
                var message = response.data['message'];
                console.log(data);
                console.log(message);
                setTimeout(function () {
                    $scope.tagData = data;
                    $scope.message = message;
                }, 10);
            });
        }
    }
})();