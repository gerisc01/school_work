//
//  CalculatorBrain.h
//  Calculator
//
//  Created by Scott Gerike on 2/9/12.
//  Copyright (c) 2012 Luther College. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface CalculatorBrain : NSObject

- (void)pushOperand:(double)operand;
- (void)pushStringOperand:(NSString *)operand;
- (double)performOperation:(NSString *)operation;
- (void)clearOperands;
- (NSString *)updateDescription;
- (NSString *)popAndClearOperand;

@property (readonly) id program;

+ (double)runProgram:(id)program usingVariableValues:(NSMutableDictionary *)variableValues;
+ (NSString *)descriptionOfProgram:(id)program dict:(NSDictionary *)operatorDict;

@end
