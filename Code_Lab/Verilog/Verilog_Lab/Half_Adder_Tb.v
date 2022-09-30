module Half_Adder_Tb;
reg a,b;
wire sum,carry;

half_adder Tb(a,b,sum,carry);
initial begin
    #5 a=1'b0; b=1'b0;
    #5 a=1'b0; b=1'b1;
    #5 a=1'b1; b=1'b0;
    #5 a=1'b1; b=1'b1;
end 
initial 
    #5000000 $finish;
initial 
    begin
    $monitor("time = %d ,A = %b, B = %b, Sum = %b, Carry = %b", $time,a,b,sum,carry);
    end
endmodule