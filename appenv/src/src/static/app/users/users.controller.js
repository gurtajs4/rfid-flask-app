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
            service.getItems(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    var singleViewModel = JSON.stringify(data[i]);
                    if (!images.isImageUrl(singleViewModel.pic_url)) {
                        singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                    }
                    $log.info(singleViewModel);
                    viewModel.push(singleViewModel);
                }
                self.list = viewModel;
            });
        }
    }
})();