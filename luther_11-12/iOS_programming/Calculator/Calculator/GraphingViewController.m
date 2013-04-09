//
//  GraphingViewController.m
//  Calculator
//
//  Created by Scott Gerike on 3/27/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import "GraphingViewController.h"
#import "GraphView.h"
#import "CalculatorBrain.h"

@implementation GraphingViewController
@synthesize programText;
@synthesize programLabel = _programLabel;
@synthesize aGraphView = _aGraphView;
@synthesize graphDataDelegate = _graphDataDelegate;
@synthesize myToolbar;

- (void)setProgramLabel:(NSString *)programLabel
{
    _programLabel = @"y = ";
    _programLabel = [_programLabel stringByAppendingString:programLabel];
}

- (void) awakeFromNib {
    [super awakeFromNib];
    self.splitViewController.delegate = self;
}

- (void) setGraphDataDelegate:(CalculatorViewController *)graphDataDelegate
{
    _graphDataDelegate = graphDataDelegate;
}

-(void)graphIt {
	self.aGraphView.graphingDataDelegate = self.graphDataDelegate;
	[self.aGraphView setNeedsDisplay];
}

-(void) setAGraphView:(GraphView *)aGraphView
{
    _aGraphView = aGraphView;
}

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)didReceiveMemoryWarning
{
    // Releases the view if it doesn't have a superview.
    [super didReceiveMemoryWarning];
    
    // Release any cached data, images, etc that aren't in use.
}

#pragma mark - View lifecycle

- (void)viewDidLoad
{
    [super viewDidLoad];
    [self.aGraphView addGestureRecognizer:[[UIPinchGestureRecognizer alloc] initWithTarget:self.aGraphView action:@selector(pinch:)]];
    [self.aGraphView addGestureRecognizer:[[UIPanGestureRecognizer alloc] initWithTarget:self.aGraphView action:@selector(pan:)]];
    self.aGraphView.graphingDataDelegate = self.graphDataDelegate;
    UITapGestureRecognizer *tapper = [[UITapGestureRecognizer alloc] initWithTarget:self.aGraphView action:@selector(recenter:)];
    tapper.numberOfTapsRequired = 3;
    tapper.numberOfTouchesRequired = 1; //number of fingers
    [self.aGraphView addGestureRecognizer:tapper];
    // Do any additional setup after loading the view, typically from a nib.
    self.programText.text = self.programLabel;
    
} 

- (void)viewDidUnload
{
    [self setProgramText:nil];
    [self setMyToolbar:nil];
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    return YES;
}

- (void) setSplitViewBarButtonItem:(UIBarButtonItem *)splitViewBarButtonItem
{
    NSMutableArray *toolbarItems = [self.myToolbar.items mutableCopy];
    if (splitViewBarButtonItem) [toolbarItems insertObject:splitViewBarButtonItem atIndex:0];
    self.myToolbar.items = toolbarItems;
}

- (void) removeSplitViewBarButtonItem:(UIBarButtonItem *)splitViewBarButtonItem
{
    NSMutableArray *toolbarItems = [self.myToolbar.items mutableCopy];
    
    [toolbarItems removeObject:splitViewBarButtonItem];
    self.myToolbar.items = toolbarItems;
}

-(BOOL) splitViewController:(UISplitViewController *)svc shouldHideViewController:(UIViewController *)vc inOrientation:(UIInterfaceOrientation)orientation {
    return UIInterfaceOrientationIsPortrait(orientation);
}

-(void)splitViewController:(UISplitViewController *)svc willHideViewController:(UIViewController *)aViewController withBarButtonItem:(UIBarButtonItem *)barButtonItem forPopoverController:(UIPopoverController *)pc
{    
    barButtonItem.title = @"Calculator";
    //tell detail view controlle rto put this button up
    
    [self setSplitViewBarButtonItem:barButtonItem];
}

-(void)splitViewController:(UISplitViewController *)svc willShowViewController:(UIViewController *)aViewController invalidatingBarButtonItem:(UIBarButtonItem *)barButtonItem
{
    [self removeSplitViewBarButtonItem:barButtonItem];
}

@end
