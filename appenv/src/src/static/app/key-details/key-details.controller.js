(function () {
    'use strict';

    angular.module('appMain').controller('KeyDetailsController', KeyDetailsController);

    KeyDetailsController.$inject = ['$scope', '$routeParams', 'keysService'];
    function KeyDetailsController($scope, $routeParams, keysService) {
        var service = keysService;

        $scope.keyId = $routeParams.id;

        init();

        function init() {
            service.getItem($scope.keyId).then(function (response) {
                var data = response.data;
                $scope.keyData = JSON.parse(data);
            });
        }
    }
})();