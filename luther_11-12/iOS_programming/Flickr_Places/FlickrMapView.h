//
//  FlickrMapView.h
//  Flickr_Places
//
//  Created by Scott Gerike on 5/3/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <Foundation/Foundation.h>
#import <MapKit/MapKit.h>

@interface FlickrMapView : NSObject <MKAnnotation>

+ (FlickrMapView *)annotationForPhoto:(NSDictionary *)photo; //Flickr photo dictionary
//- (void)isLocations:(BOOL)ans;
@property (nonatomic, strong) NSDictionary *photo;

@end
