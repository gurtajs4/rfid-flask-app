(function () {
    'use strict';

    angular.module('appMain').controller('KeyDetailsController', KeyDetailsController);

    KeyDetailsController.$inject = ['$scope', '$routeParams', '$location', 'keysService'];
    function KeyDetailsController($scope, $routeParams, $location, keysService) {
        var service = keysService;

        $scope.keyId = $routeParams.id;
        $scope.deleteItem = deleteItem;

        init();

        function init() {
            service.getItem($scope.keyId).then(function (response) {
                var data = response.data;
                $scope.keyData = JSON.parse(data);
            });
        }

        function deleteItem() {
            if ($scope.userData.isSelected) {
                service.keyDelete($scope.keyId).then(function (response) {
                    $location.url('/keys');
                }).catch(function (error) {
                    window.alert(' error: ' + error);
                });
            }
        }
    }
})();