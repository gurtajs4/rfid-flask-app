(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersController', UsersController);

    UsersController.$inject = ['$log', 'usersService'];
    function UsersController($log, usersService) {
        var self = this;
        var service = usersService;

        activate();

        function activate() {
            service.getItems(function (response) {
                self.list = response.data;
            }).catch(function (error) {
                $log.error('Failed to load all stored items ', error);
            });
        }
    }
})();