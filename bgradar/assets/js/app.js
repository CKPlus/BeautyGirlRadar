var bgradarApp = angular.module('bgradarApp',
	['ngRoute',
   'ngResource',
   'google-maps',
   'mgcrea.ngStrap',
   'bgradarApp.controllers']);

bgradarApp.config(function($routeProvider, $locationProvider) {
		$routeProvider
		.when('/bgradar', {
			templateUrl: '/static/partials/wall.html',
			controller: 'WallController'
		})
    .when('/bgradar/map', {
      templateUrl: '/static/partials/map.html',
      controller: 'RadarController'
    });

		$locationProvider.html5Mode(true);


	}
);


bgradarApp.config(['$resourceProvider', function ($resourceProvider) {
       // Don't strip trailing slashes from calculated URLs
       // $resourceProvider.defaults.stripTrailingSlashes = false;
     }]);

bgradarApp.factory('BGlbs', ['$resource', function($resource) {
   return $resource('/api/bglbsdata/:_id',
        {
          '_id' : '@_id'
        },
        {
           'list' : { method:'GET' },
           'updateData' : { method:'PATCH' }
        });
    }]);

bgradarApp.factory('BGlbs50', ['$resource', function($resource) {
   return $resource('/api/bglbsdata50/:_id',
        {
          '_id' : '@_id'
        },
        {
           'list' : { method:'GET' },
           'updateData' : { method:'PATCH' }
        });
    }]);

