from controller import Robot
robo=Robot()
time_step=32
max_speed=6.28

left_motor = robo.getDevice('motor_l')
right_motor = robo.getDevice('motor_r')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
mid_ir = robo.getDevice('sensor_m')
left_ir = robo.getDevice('sensor_l')
right_ir = robo.getDevice('sensor_r')
left_ir.enable(time_step)
right_ir.enable(time_step)
mid_ir.enable(time_step)

while robo.step(time_step) != -1:
    left_speed=0.5*max_speed
    right_speed=0.5*max_speed
    left_ir_val = left_ir.getValue()
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    print('left= {} mid= {} right= {}'.format(left_ir_val,mid_ir_val,right_ir_val))
    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)