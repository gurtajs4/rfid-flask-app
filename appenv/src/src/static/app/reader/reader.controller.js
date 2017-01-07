(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('ReaderController', ReaderController);

    ReaderController.$inject = ['readerService'];
    function ReaderController(readerService) {
        var service = readerService;
        var self = this;
        self.tagData = "";
        self.message = "";

        activate();

        function activate() {
            service.initReader().then(function (response) {
                console.log(response.data);
                var tData = response.data.data.toString();
                setTimeout(function () {
                    self.tagData = tData;
                    self.message = response.data.message;
                    // $scope.$apply(function () {
                    //     $scope.tagData = tData;
                    //     $scope.message = response.data.message;
                    // });
                    // console.log($scope.tagData);
                    // console.log($scope.message);
                    console.log(self.tagData);
                    console.log(self.message);
                }, 0);
            });
        }
    }
})();