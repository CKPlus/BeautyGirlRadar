var bgradarApp = angular.module('bgradarApp',
	['ngRoute',
   'ngResource',
   'google-maps',
   'mgcrea.ngStrap',
   // 'pascalprecht.translate', 
   // 'ngDialog', 
   // 'mgcrea.ngStrap.datepicker',
   // 'mgcrea.ngStrap.popover',
   // 'ui.bootstrap.pagination',
   // 'ui.bootstrap.tpls',
   // 'dateFilters',
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

/*
bgradarApp.config(['$datepickerProvider', function($datepickerProvider) {
    angular.extend($datepickerProvider.defaults, {
      dateFormat: 'yyyy-MM-dd',
      dateType: 'string',
      startWeek: 1
    });
  }]);


bgradarApp.factory('Member', ['$resource', function($resource) {
   return $resource('/account/api/member/:_id/',
   	    {
   	    	'_id' : '@_id'
   	    },
        {
           'list' : { method:'GET', isArray:true },
           'get' : { method:'GET'}
        });
    }]);


bgradarApp.factory('Job', ['$resource', function($resource) {
   return $resource('/review/api/job/:_id/',
   	    {
   	    	'_id' : '@_id'
   	    },
        {
          'list' : { 
              method:'GET',
              transformRequest: transformRequest,
              transformResponse: transformResponse,
              interceptor: {
                responseError: function(response){
                  alert(response.data);
                }
              }
          },
          'changeStatus' : { 
            method:'PATCH',
            transformRequest: transformRequest,
            transformResponse: transformResponse,
            interceptor: {
                responseError: function(response){
                  alert(response.data);
                }
            }
          },
          'approvedSelected' : {
            method:'PATCH',
            isArray:true,
            transformRequest: transformRequest,
            transformResponse: transformResponse,
            interceptor: {
                responseError: function(response){
                  alert(response.data);
                }
            }
          }
        });
    }]);


bgradarApp.factory('Queue', ['$resource', function($resource) {
   return $resource('/review/api/queue/:_id/',
   	    {
   	    	'_id' : '@_id'
   	    },
        {
           'update': {method:'PUT' },
           'get'   : {method:'GET' },
           'getJob': {method:'GET'},
           'list'   : { 
              method:'GET',
              isArray:true
           },
           'delete': { method:'DELETE'}
           
        });
    }]);


bgradarApp.factory('QueueJob', ['$resource', function($resource) {
   return $resource('/review/api/queue/:_id/job/',
        {
          '_id' : '@_id'
        },
        {
            'getJob': { 
                method:'GET',
                transformRequest: transformRequest,
                transformResponse: transformResponse,
                interceptor: {
                responseError: function(response){
                  alert(response.data);
                }
              }
            }
        });
    }]);

bgradarApp.factory('Log', ['$resource', function($resource) {
   return $resource('/review/api/log/:_id/',
        {
          '_id' : '@_id'
        },
        {
           'get'   : { method:'GET', isArray: true}
        });
    }]);


bgradarApp.factory('Language', ['$resource', function($resource) {
   return $resource('/account/api/language/',
        null,
        {
           'get'   : { method:'GET'},
           'list': { method:'GET', isArray: true}
        });
    }]);

bgradarApp.config(['$translateProvider', function ($translateProvider) {
  $translateProvider.preferredLanguage(language);
  $translateProvider.useLoader('asyncLoader');
}]);


bgradarApp.factory('asyncLoader', function ($http, $q, $timeout) {
 
  return function (options) {
    var deferred = $q.defer(),
        translations;

    $http({
          method:'GET',
          url: '/general/api/language/',
          params: { 'lang': options['key'] },
        }).success(function (data) {
          deferred.resolve(data);
        }).error(function () {
          deferred.reject(options.key);
        });

    $timeout(function () {
      deferred.resolve(translations);
    }, 2000);
    return deferred.promise;
  };
});
*/

