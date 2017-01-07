(function () {
    'use strict';

    angular
        .module('appMain')
        .directive('reader', reader);

    reader.$inject = ['templateServiceProvider'];

    function reader(templateServiceProvider) {
        var appBaseUrl = templateServiceProvider.appBaseUrl();
        return {
            restrict: 'EA',
            scope: {
                tagData: "=?",
                message: "=?"
            },
            templateUrl: appBaseUrl + '/reader/reader.html',
            controller: 'ReaderController'
        }
    }
})();