(function () {
    'use strict';

    angular
        .module('appMain')
        .service('imagesService', imagesService);

    imagesService.$inject = ['$http', '$log', '$window'];
    function imagesService($http, $log, $window) {
        var service = {
            isImage: isImage,
            isImageUrl: isImageUrl,
            readImageFile: readImageFile,
            readImageFileBuffer: readImageFileBuffer,
            getDefaultUserProfileImageUrl: getDefaultUserProfileImageUrl,
            getDefaultRoomPhotoUrl: getDefaultRoomPhotoUrl,
            uploadImageToServer: uploadImageToServer
        };

        return service;

        function isImage(file) {
            if ($window.FileReader) {
                return file.type.match('image.*') == true;
            }
        }

        function isImageUrl(url) {
            $http.get(url).then(function (response) {
                return true;
            }).catch(function (error) {
                $log.error('Log from images service: ', error);
                return false;
            });
        }

        function readImageFile(file, callback) {
            return function () {
                if ($window.FileReader) {
                    var reader = new $window.FileReader();
                    reader.onloadend = function (event) {
                        if (event.target.error === null) {
                            callback(reader.result);
                        }
                        else {
                            callback(null);
                        }
                    };
                    reader.readAsDataURL(file);
                }
            }
        }

        function readImageFileBuffer(fileSrc) {
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
            var file = {
                src: fileSrc
            };
            return $http.post('/api/image/upload', JSON.parse(file));
            // return uploader(fileSrc, function (result) {
            //     var file = {
            //             src: fileSrc,
            //             file: result
            //         };
            //         return $http.post('/api/image/upload', JSON.parse(file));
            // });
        }

        function getDefaultUserProfileImageUrl() {
            return '/images/default.png';
        }

        function getDefaultRoomPhotoUrl() {
            return '/images/default-room.png';
        }
    }
})();