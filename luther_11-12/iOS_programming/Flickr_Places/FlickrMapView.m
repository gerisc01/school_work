//
//  FlickrMapView.m
//  Flickr_Places
//
//  Created by Scott Gerike on 5/3/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrMapView.h"
#import "FlickrFetcher.h"

@implementation FlickrMapView

@synthesize photo = _photo;

+ (FlickrMapView *)annotationForPhoto:(NSDictionary *)photo
{
    FlickrMapView *annotation = [[FlickrMapView alloc] init];
    annotation.photo = photo;
    return annotation;
}

- (NSString *)title
{
    return [self.photo objectForKey:FLICKR_PHOTO_TITLE];
}

- (NSString *)subtitle
{
    return [self.photo valueForKeyPath:FLICKR_PHOTO_DESCRIPTION];
}

- (CLLocationCoordinate2D)coordinate
{
    CLLocationCoordinate2D coordinate;
    coordinate.latitude = [[self.photo objectForKey:FLICKR_LATITUDE] doubleValue];
    coordinate.longitude = [[self.photo objectForKey:FLICKR_LONGITUDE] doubleValue];
    return coordinate;
}

@end
