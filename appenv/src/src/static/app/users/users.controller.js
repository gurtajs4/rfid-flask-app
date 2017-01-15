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
                if (response.status == 200) {
                    var data = response.data;
                    var viewModel = [];
                    for (var i = 0; i < data.length; i++) {
                        viewModel.push(JSON.parse(data[i]));
                    }
                    self.list = viewModel;
                    $log.debug('Sessions loaded are ', viewModel);
                }
                else {
                    $log.debug('Response status is not 200, data is ' + response.data);
                }
            }).catch(function (error) {
                $log.error('Failed to load all stored items ', error);
            });
        }
    }
})();