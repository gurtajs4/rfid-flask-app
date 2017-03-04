(function () {
    'use strict';
    angular.module('appMain').controller('KeyEditController', KeyEditController);

    KeyEditController.$inject = ['$scope', '$log', '$location'];
    function KeyEditController($scope, $log, $location) {
        var service = null; // treba service za edit

        $scope.title = "Stranica za uređivanje podataka o ključu";
        $scope.note = "Uredite podatke o ključu i prostoriji pridjeljujući broj prostorije s ostalim podacima poput odjela.";

        $scope.tagData = "";
        $scope.message = "";

        $scope.update = update;
        $scope.cancel = cancel;

        function update() {
            var key = {
                id: -1,
                tag_id: $scope.tagData,
                room_id: $scope.roomId,
                block_name: $scope.blockName,
                sector_name: $scope.sectorName,
                floor: $scope.floor
            };
            $log.info('Key: ', key);
            service.registerKey(key)
                .then(function (response) {
                    if (response.status == 200) {
                        $location.url('/home');
                    }
                    else {
                        $log.debug('Response status is not 200 on registering key: ' + response.data);
                    }
                })
                .catch(function (error) {
                    $log.error('Failed to create key... ' + error.data);
                });
        }

        function cancel() {
            $location.url('/home');
        }
    }
})();