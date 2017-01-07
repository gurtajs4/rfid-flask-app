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
                tagData: "=?tagData",
                message: "=?message",
                getOuterScope: "&"
            },
            templateUrl: appBaseUrl + '/reader/reader.html',
            controller: 'ReaderController',
            controllerAs: 'rdc',
            bindToController: true
        }
    }
})();