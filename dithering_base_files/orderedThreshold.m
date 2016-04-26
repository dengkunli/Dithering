function O = orderedThreshold(I, type)
% O = orderedThreshold(I, type)
% Ordered threshold method for image dithering.
% I: The input image
% type: 1,2,3,4 or 5.
%		type = 1: Ordered threshold - Clustered dots
%		type = 2: Ordered matrix with central white point
%		type = 3: Ordered matrix with balanced centered point
%		type = 4: Diagonal ordered matrix with balanced centered points
%		type = 5: Ordered matrix with dispersed dots
%
% Written by Michalis Zervos - All rights reserved
% http://michal.is/projects/image-dithering-in-matlab/

if (type == 1)
	% Ordered threshold - Clustered dots
	S = [34 29 17 21 30 35;
		 28 14 9 16 20 31;
		 13 8 4 5 15 19;
		 12 3 0 1 10 18; 
		 27 7 2 6 23 24;
		 33 26 11 22 25 32];
 
elseif (type == 2)
	% Ordered matrix with central white point

	S = [34 25 21 17 29 33;
		  30 13 9 5 12 24;
		  18 6 1 0 8 20;
		  22 10 2 3 4 16;
		  26 14 7 11 15 28;
		  35 31 19 23 27 32];

elseif (type == 3)	
	% Ordered matrix with balanced centered point
	
	S = [30 22 16 21 33 35;
		  24 11 7 9 26 28;
		  13 5 0 2 14 19;
		  15 3 1 4 12 18;
		  27 8 6 10 25 29;
		  32 20 17 23 31 34];
  
elseif (type == 4)
	% Diagonal ordered matrix with balanced centered points
	
	S1 = [13 9 5 12;
		   6 1 0 8;
		   10 2 3 4;
		   14 7 11 15];
   
	S2 = [18 22 26 19;
		   25 30 31 23;
		   21 29 28 27;
		   17 24 20 16];

	S = [S1 S2; S2 S1];
	
elseif (type == 5)
	% Ordered matrix with dispersed dots
	
	U = ones(3);
	D = [8 4 5;
		  3 0 1;
		  7 2 6];

	S = [4*D 4*D+2*U;
		  4*D+3*U 4*D+U];
else
	fprintf('Error. Type should be one of the following:\n');
	fprintf('1 for ordered threshold with clustered dots\n');
	fprintf('2 for ordered matrix with central white point\n');
	fprintf('3 for ordered matrix with balanced centered point\n');
	fprintf('4 for diagonal ordered matrix with balanced centered point\n');
	fprintf('5 for ordered matrix with dispersed dots\n');
	O = zeros(1,1);
	return;
end



% Size of image and S
si = size(I);
ss = size(S);

% Create an image with the same size as I, 
% which has the matrix S replicated. Replicate it using the ceiling
% of their size ratio and then discard the last extra elements (if any).
ts = ceil(si ./ ss);
SImg = repmat(S, ts);
SImg = SImg(1:si(1), 1:si(2));

% Shift the values by 0.5 so that we can compare without floor.
SImg = SImg + 0.5;

% Number of levels N
N = max(S(:)) - min(S(:)) + 2;
% Quantization step and quantized image (with values in 0,1,2,...,N-1)
D = 255 ./ (N-1);
Q = double(I) ./ D;

% Threshold image 
% Pixels with value greater than that of S (at the same position) become 1,
% the rest 0
O = Q > SImg;

end