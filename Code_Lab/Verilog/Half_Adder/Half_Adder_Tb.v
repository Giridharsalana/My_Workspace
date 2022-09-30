module Half_Adder_Tb;
reg a,b;
wire sum,carry;

half_adder Tb(a,b,sum,carry);
initial begin
    $dumpfile("Half_Adder.vcd");
    $dumpvars(0,Half_Adder_Tb);
    #50 a=1'b0; b=1'b0;
    #50 a=1'b0; b=1'b1;
    #50 a=1'b1; b=1'b0;
    #50 a=1'b1; b=1'b1;
end 
initial 
    #200 $finish;
endmodule