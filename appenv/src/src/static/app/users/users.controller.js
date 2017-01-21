(function () {
    'use strict';

    angular
        .module('appMain')
        .controller('UsersController', UsersController);

    UsersController.$inject = ['$log', 'usersService', imagesService];
    function UsersController($log, usersService, imagesService) {
        var self = this;
        var service = usersService;
        var images = imagesService;

        activate();

        function activate() {
            service.getItems(function (response) {
                var data = response.data;
                $log.info(data);
                var viewModel = [];
                for (var i = 0; i < data.length; i++) {
                    var singleViewModel = data[i];
                    if (!images.isImage(singleViewModel.pic_url)) {
                        singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                    }
                    $log.info(singleViewModel);
                    viewModel.push(JSON.parse(singleViewModel));
                }
                self.list = viewModel;
            });
        }
    }
})();