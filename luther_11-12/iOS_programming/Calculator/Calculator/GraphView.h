//
//  GraphView.h
//  Calculator
//
//  Created by Scott Gerike on 3/27/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>

@protocol GraphingData <NSObject>

- (double) getValueForXCoordinate:(float)x;

@end

@interface GraphView : UIView

@property (nonatomic, weak) IBOutlet id <GraphingData> graphingDataDelegate;
@property (nonatomic) CGFloat scale;
@property (nonatomic) CGFloat xtrans;
@property (nonatomic) CGFloat ytrans;
@property (nonatomic) CGFloat transx;
@property (nonatomic) CGFloat transy;
@end
