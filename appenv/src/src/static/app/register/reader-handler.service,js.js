(function () {
    'use strict';
    angular.module('appMain').service('readerHandlerService', readerHandlerService);

    function readerHandlerService() {
        var tagData = '';
        var service = {
            tagData: tagData,
            getTagData: getTagData,
            storeTagData: storeTagData
        };

        return service;

        function getTagData() {
            return service.tagData;
        }

        function storeTagData(tData) {
            service.tagData = tData;
        }
    }
})();