//
//  GraphingViewController.h
//  Calculator
//
//  Created by Scott Gerike on 3/27/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "GraphView.h"
#import "CalculatorViewController.h"

@interface GraphingViewController : UIViewController <UISplitViewControllerDelegate>
@property (weak, nonatomic) IBOutlet UILabel *programText;
@property (weak, nonatomic) NSString *programLabel;
@property (weak, nonatomic) IBOutlet UIToolbar *myToolbar;

@property (weak, nonatomic) IBOutlet CalculatorViewController *graphDataDelegate;

@property (weak, nonatomic) IBOutlet GraphView *aGraphView;

- (void)graphIt;
@end
