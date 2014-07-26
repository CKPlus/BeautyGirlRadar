angular.module('bgradarApp.controllers', [])
  .controller('WallController', ['$scope', '$modal', 'BGlbs',
  	 function($scope, $modal, BGlbs) {
  	 	var init = function(){
  	 		$scope.selectedRecord = {}
  	 		var records = BGlbs.list(function(data){
  	 			$scope.records = data.results;
  	 		});
		}
		init();

		$scope.showModal = function(selectedRecord){
			$('#myModal').modal();

			$scope.website = selectedRecord.fans_url;
			$scope.comment = selectedRecord.comment;

			$scope.selectedRecord = selectedRecord;
		}

		$scope.save = function(){
			

			var patchData = {
				"_id": $scope.selectedRecord.uid,
				"comment": $scope.comment || '',
  				"fans_url": $scope.website || ''
			}

			BGlbs.updateData(patchData, function(){
				alert('感謝眾鄉民的工人智慧！');
				$('#myModal').modal('toggle');
				$scope.website = '';
				$scope.comment = '';
				init();
			});
		}

		
  	}])
  .controller('RadarController', ['$scope', 'BGlbs',
  	 function($scope, BGlbs) {
  	 	var init = function(){

  	 		BGlbs.list(function(data){
  	 			$scope.markers = []

  	 			console.log(data);
				_.each(data.results, function (marker) {
				  var obj = {
				  	id : marker.uid,
					latitude :marker.lat,
					longitude :marker.lng,
					title :'Test Record',
					showWindow :false
				  }
				  // marker.id = marker.uid
				  // marker.latitude = marker.lat;
				  // marker.longitude = marker.lng;
				  // marker.title = 'Test Record';
				  // marker.showWindow = false;
			      obj.closeClick = function () {
			        // marker.showWindow = false;
			        // $scope.$apply();
			      };
			      obj.onClicked = function () {
			        $scope.onMarkerClicked(marker);
			      };
			      $scope.markers.push(obj);
			    });
			 //    var markers = [
			 //        {
			 //          id: 1,
			 //          latitude: 45,
			 //          longitude: -74,
			 //          showWindow: false,
			 //          title: 'Marker 2',
			 //        },
			 //        {
			 //          id: 2,
			 //          latitude: 15,
			 //          longitude: 30,
			 //          showWindow: false,
			 //          title: 'Marker 2'
			 //        },
			 //        {
			 //          id: 3,
			 //          latitude: 37,
			 //          longitude: -122,
			 //          showWindow: false,
			 //          title: 'Plane'
			 //        },
			 //        {
			 //          id: 4,
			 //          latitude: 37,
			 //          longitude: -122,
			 //          showWindow: false,
			 //          title: 'Plane'
			 //        }
				// ]

				

  	 		});

var markers = [
			        {
			          id: 1,
			          latitude: 45,
			          longitude: -74,
			          showWindow: false,
			          title: 'Marker 2',
			        },
			        {
			          id: 2,
			          latitude: 15,
			          longitude: 30,
			          showWindow: false,
			          title: 'Marker 2'
			        },
			        {
			          id: 3,
			          latitude: 37,
			          longitude: -122,
			          showWindow: false,
			          title: 'Plane'
			        },
			        {
			          id: 4,
			          latitude: 37,
			          longitude: -122,
			          showWindow: false,
			          title: 'Plane'
			        }
				]
				
		    	$scope.map = {
				    'center': {
				        latitude: 45,
				        longitude: -73
				    },
				    'zoom': 14,
				    'markers': markers
				    
				};



			// for(var i=0, l=$scope.map.markers.length; i<l; i+=1){
			// 	var marker = $scope.map.markers[i]
				

			// 	marker.onClicked = function (marker){
			// 		console.log(marker);
			// 		// $scope.onMarkerClicked(marker);
			// 	}
			// }
		}

		$scope.onMarkerClicked = function (marker) {
			//    if (markerToClose) {
			//      markerToClose.showWindow = false;
			//    }
			    markerToClose = marker; // for next go around
			    marker.showWindow = true;
			    $scope.$apply();
			    //window.alert("Marker: lat: " + marker.latitude + ", lon: " + marker.longitude + " clicked!!")
		}

		init();
  	}])