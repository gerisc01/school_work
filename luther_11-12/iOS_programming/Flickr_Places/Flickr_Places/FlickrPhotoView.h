//
//  FlickrPhotoView.h
//  Flickr_Places
//
//  Created by Scott Gerike on 4/22/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol PhotoData <NSObject>

-(NSURL *)getPhotoData;

@end
@interface FlickrPhotoView : UIImageView
@property (nonatomic, weak) IBOutlet id <PhotoData> photoDataDelegate;
@end
