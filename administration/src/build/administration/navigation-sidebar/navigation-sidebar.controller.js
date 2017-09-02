(function () {
    'use-strict';

    angular
        .module('administration')
        .controller('SidebarController', SidebarController);

    SidebarController.$inject = ['$scope', '$log'];
    function SidebarController($scope, $log) {
        $scope.common = {label: 'Korisničke opcije'};
        $scope.extended = {label: 'Korisničke opcije'};
        $scope.settings = {label: 'Korisničke opcije'};

        /* {id: 0, route: '/', name: 'Naslovnica'}*/

        $scope.commonRoutes = [
            {id: 7, route: '/users/search', name: 'Pretraga korisnika'},
            {id: 2, route: '/keys/search', name: 'Pretraga ključeva'}
        ];
        $scope.extendedRoutes = [
            {id: 1, route: '/sessions', name: 'Preuzimanja ključeva'},
            {id: 6, route: '/users', name: 'Korisnici'},
            {id: 5, route: '/keys', name: 'Prostorije'}
        ];
        $scope.settingsRoutes = [
            {id: 4, route: '/keys/register', name: 'Registracija ključa'},
            {id: 3, route: '/keys/seed', name: 'Uvoz ključeva'}
        ];

        /*
         function displayOptions() {
         if ($scope.common.showOptions) {
         // getCommonOptions
         }
         if ($scope.extended.showOptions) {
         // getCommonOptions
         }
         if ($scope.settings.showOptions) {
         // getCommonOptions
         }
         }*/
    }
})();