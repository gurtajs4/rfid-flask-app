(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersController', UsersController);

    UsersController.$inject = ['$log', 'usersService', 'imagesService'];
    function UsersController($log, usersService, imagesService) {
        var self = this;
        var service = usersService;
        var images = imagesService;

        init();

        function init() {
            service.getItems().then(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                angular.forEach(data, function (value, key) {
                    var singleViewModel = JSON.parse(value);
                    if ("" === singleViewModel.pic_url) {
                        singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                    }
                    this.push(singleViewModel)
                }, viewModel);
                self.list = viewModel;
            });
        }
    }
})();