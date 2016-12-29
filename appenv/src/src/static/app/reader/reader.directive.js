(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('reader', reader);

    reader.$inject = ['templateService'];

    function reader(templateService) {
        var appBaseUrl = templateService.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                tagData: "=",
                message: "="
            },
            templateUrl: appBaseUrl+'/reader/reader.html',
            controller: 'ReaderController',
            controllerAs: 'rdc'
        }
    }
})();