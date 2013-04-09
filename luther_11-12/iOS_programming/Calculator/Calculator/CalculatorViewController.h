//
//  CalculatorViewController.h
//  Calculator
//
//  Created by Scott Gerike on 2/7/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GraphView.h"

@interface CalculatorViewController : UIViewController <GraphingData>

@property (weak, nonatomic) IBOutlet UILabel *display;
@property (weak, nonatomic) IBOutlet UILabel *recentEntries;

@end
