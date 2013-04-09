//
//  GraphView.m
//  Calculator
//
//  Created by Scott Gerike on 3/27/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//



#import "GraphView.h"
#import "AxesDrawer.h"

@implementation GraphView

@synthesize scale = _scale;
@synthesize xtrans = _xtrans;
@synthesize ytrans = _ytrans;
@synthesize transy = _transy;
@synthesize transx = _transx;


@synthesize graphingDataDelegate= _graphingDataDelegate;

- (id)initWithFrame:(CGRect)frame
{
    self = [super initWithFrame:frame];
    self.xtrans = 0.0;
    self.ytrans = 0.0;
    if (self) {
        // Initialization code
    }
    return self;
}

- (CGFloat)scale
{
    if (!_scale) {
        return 0.90; // don't allow zero scale
    } else {
        return _scale;
    }
}

- (void)setScale:(CGFloat)scale
{
    if (scale != _scale) {
        _scale = scale;
        [self setNeedsDisplay]; // any time our scale changes, call for redraw
    }
}
- (void)pinch:(UIPinchGestureRecognizer *)gesture
{
    if ((gesture.state == UIGestureRecognizerStateChanged) ||
        (gesture.state == UIGestureRecognizerStateEnded)) {
        self.scale *= gesture.scale; // adjust our scale
        gesture.scale = 1;
        // reset gestures scale to 1 (so future changes are incremental, not cumulative)
        [self setNeedsDisplay];
    }
}
-(void)pan:(UIPanGestureRecognizer *)gesture{
    if ((gesture.state == UIGestureRecognizerStateChanged) ||
        (gesture.state == UIGestureRecognizerStateEnded)) {
        CGPoint translation = [gesture translationInView:self];
        
        CGFloat aX = translation.x;
        self.transx += aX;
        CGFloat aY = translation.y;
        self.transy += aY;
        
        //self.xtrans +=translation.y;
        //self.ytrans += translation.y;
        
        CGPoint resetp = CGPointMake(0.0, 0.0);
        [gesture setTranslation:resetp inView:self];
        
        
        //[gesture setTranslation:CGPointMake(self.xtrans,self.ytrans) inView:self];
        [self setNeedsDisplay];
    }
}

-(void)recenter:(UITapGestureRecognizer *)gesture{
    CGPoint touch = [gesture locationInView:self];
    CGPoint midpoint;
    midpoint.x = self.bounds.size.width/2.0;
    midpoint.y = self.bounds.size.height/2.0;
    
    self.transx = touch.x - midpoint.x;
    self.transy = touch.y - midpoint.y;
    
    [self setNeedsDisplay];
}

// Only override drawRect: if you perform custom drawing.
// An empty implementation adversely affects performance during animation.
- (void)drawRect:(CGRect)rect
{
    if (self.scale ==0) self.scale = 1.0;
    
    CGFloat xscale = self.scale;
    CGFloat yscale = -self.scale;
    CGFloat xtrans = self.bounds.size.width/2.0 + self.transx;
    CGFloat ytrans = self.bounds.size.height/2.0 + self.transy;
    CGPoint midPoint;
    midPoint.x = self.bounds.origin.x + xtrans;
    midPoint.y = self.bounds.origin.y + ytrans;
    
    [AxesDrawer drawAxesInRect:CGRectMake(0, 0, self.bounds.size.width, self.bounds.size.height) originAtPoint:midPoint scale:self.scale];
    
    CGFloat y;
    CGContextBeginPath(UIGraphicsGetCurrentContext());
    
    CGFloat xmin = -xtrans * 1.0/xscale;
    CGFloat ymin = [self.graphingDataDelegate getValueForXCoordinate:xmin] * yscale+ytrans;
    CGContextMoveToPoint(UIGraphicsGetCurrentContext(), xmin*xscale+self.xtrans,ymin);
    
    CGFloat xmax = xmin + self.bounds.size.width * 1.0/xscale;
    CGFloat xplot = 0.0; //xplot used so the looping value is not destroyed
    CGFloat incr = (xmax - xmin) / (self.bounds.size.width * xscale);
    for (CGFloat x = xmin; x < xmax; x+= incr) {
        y = [self.graphingDataDelegate getValueForXCoordinate:x];
        y = y * yscale + ytrans; //scaling first, then translation
        xplot = x * xscale + xtrans;
        CGContextAddLineToPoint(UIGraphicsGetCurrentContext(), xplot, y);
    }
    CGContextStrokePath(UIGraphicsGetCurrentContext());
}


@end 
