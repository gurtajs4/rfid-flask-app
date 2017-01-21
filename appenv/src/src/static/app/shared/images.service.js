(function () {
    'use strict';

    angular
        .module('appMain')
        .service('imagesService', imagesService);

    imagesService.$inject = ['$http', '$log'];
    function imagesService($http, $log) {
        var service = {
            isImage: isImage,
            getDefaultUserProfileImageUrl: getDefaultUserProfileImageUrl,
            getDefaultRoomPhotoUrl: getDefaultRoomPhotoUrl
        };

        function isImage(url) {
            $http.get(url).then(function (response) {
                return true;
            }).catch(function (error) {
                $log.error('Log from images service: ', error);
                return false;
            });
        }

        function getDefaultUserProfileImageUrl() {
            return '/images/default.png';
        }

        function getDefaultRoomPhotoUrl() {
            return '/images/default-room.png';
        }
    }
})();