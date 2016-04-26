function O = randomThreshold(I, amplitude)
% O = randomThreshold(I, amplitude)
% Fixed threshold method for image dithering.
% I: Input image
% amplitude: noise amplitude
%
% Written by Michalis Zervos - All rights reserved
% http://michal.is/projects/image-dithering-in-matlab/


% Add noise
noise = uint8(unidrnd(amplitude, size(I)));
Im = I + noise;

% Thresold
O = threshold(Im, 0.5);

end