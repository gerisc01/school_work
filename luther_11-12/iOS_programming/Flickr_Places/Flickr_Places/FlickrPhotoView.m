//
//  FlickrPhotoView.m
//  Flickr_Places
//
//  Created by Scott Gerike on 4/22/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "FlickrPhotoView.h"

@implementation FlickrPhotoView
@synthesize photoDataDelegate = _photoDataDelegate;

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    if (self) {
        // Initialization code
    }
    return self;
}

/*
// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    // Drawing code
}
*/

@end
