function e = msei(I, D)
%	e = msei(I, D)
%	Computes the mean squared error between images I and D
%
% Written by Michalis Zervos - All rights reserved
% http://michal.is/projects/image-dithering-in-matlab/

I = im2double(I);
D = im2double(D);

sqdif = (I - D).^2;

e = mean( sqdif(:) );

end