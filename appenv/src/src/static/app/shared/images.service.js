(function () {
    'use strict';

    angular
        .module('appMain')
        .service('imagesService', imagesService);

    imagesService.$inject = ['$http', '$log', '$window'];
    function imagesService($http, $log, $window) {
        var service = {
            isImageUrl: isImageUrl,
            readImageFile: readImageFile,
            getDefaultUserProfileImageUrl: getDefaultUserProfileImageUrl,
            getDefaultRoomPhotoUrl: getDefaultRoomPhotoUrl,
            uploadImageToServer: uploadImageToServer
        };

        function isImageUrl(url) {
            $http.get(url).then(function (response) {
                return true;
            }).catch(function (error) {
                $log.error('Log from images service: ', error);
                return false;
            });
        }

        function isImage(file) {
            if ($window.FileReader) {
                return file.type.match('image.*') == true;
            }
        }

        function readImageFile(file) {
            return function () {
                if ($window.FileReader) {
                    var reader = new $window.FileReader();
                    reader.onloadend = function (event) {
                        if (event.target.error === null) {
                            return reader.result;
                        }
                        else {
                            return null;
                        }
                    };
                    reader.readAsDataURL(file);
                }
            }
        }

        function uploader(fileSrc) {
            return function () {
                var reader = new $window.FileReader();
                reader.onloadend = function (event) {
                    if (event.target.error === null) {
                        return reader.result;
                    }
                    else {
                        return null;
                    }
                };
                reader.readAsArrayBuffer(fileSrc);
            }
        }

        function uploadImageToServer(fileSrc) {
            uploader(fileSrc, function (result) {
                if (result != null) {
                    var file = {
                        src: fileSrc,
                        file: result
                    };
                    return $http.post('/api/image/upload', JSON.parse(file));
                }
                else {
                    return null
                }
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