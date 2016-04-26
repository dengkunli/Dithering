%% Test
clear all;
clc;
%% 
I = imread('Images\lena-y.png'); %size:512*512, value:0-255

I = im2double(I);%size:512*512, value:0-1

threshold = 0.5;
% Floyd & Steinberg filter
F = [0 0 7;
	 3 5 1];

F = 1/sum(F(:)) .* F;
sf = size(F); %2 row and 3 colume

% Output image, will be filled pixel by pixel
O = zeros(size(I));%size 512*512, value:all zero

% Zero-padding input image, so that we don't have to deal with edges when
% applying the filter. The extra pixels are removed in the output image
 
I = padarray(I, sf);%size 516*518 after zero padding

padx = sf(2);%value 3
pady = sf(1);%value 2

si = size(I);%value:516*518

%%
for y = pady+1:si(1)-pady %value 3 4 5 ...514 
    for x = padx+1:si(2)-padx %value 4 5 6 ...515
        
        % Threshold image and save to output (taking into account the zero
        % padding introduced)
        oy = y - pady;%value 1 2 3 ...512
        ox = x - padx;%value 1 2 3 ...512
        O(oy,ox) = (I(y,x) > threshold);%if greater than threshold then 1 else 0
        
        % Calculate error
        error = double(I(y,x) - O(oy,ox));
        
        % Get position where the filter should be applied
      
    k = floor(sf(2)/2);%value 1

    ymin = y;
    ymax = y + sf(1) - 1;% value: y+2-1=y+1
    xmin = x - (sf(2) - k - 1);%value:x-(3-1-1)=x-1
    xmax = x + k;%value: x+1
        
        % Distribute error according to the filter
        %I(y:y+1,x-1:x+1)
        I(ymin:ymax, xmin:xmax) = I(ymin:ymax, xmin:xmax) + error * F;%size 2*3
    end
end
%% show image
figure; imshow(O)
