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
                var data = response.data;
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    viewModel.push(JSON.parse(data[i]));
                }
                self.list = viewModel;
            }).catch(function (error) {
                $log.error('Failed to load all stored items ', error);
            });
        }
    }
})();