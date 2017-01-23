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
                    if (!images.isImageUrl(singleViewModel.pic_url)) {
                        singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                    }
                    $log.info('User ' + singleViewModel + 'added at index ' + key);
                    this.push(singleViewModel)
                }, viewModel);
                // for (var i = 0; i < data.length; i++) {
                //     var singleViewModel = JSON.parse(data[i]);
                //     if (!images.isImageUrl(singleViewModel.pic_url)) {
                //         singleViewModel.pic_url = images.getDefaultUserProfileImageUrl();
                //     }
                //     $log.info(singleViewModel);
                //     viewModel.push(singleViewModel);
                // }
                self.list = viewModel;
            });
        }
    }
})();