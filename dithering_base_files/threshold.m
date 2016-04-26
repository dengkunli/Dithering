function O = threshold(I, thr)
% O = threshold(I, thr)
% Fixed threshold method for image dithering.
% I: Input image
% thr: The threshold in [0, 1]
%
% Written by Michalis Zervos - All rights reserved
% http://michal.is/projects/image-dithering-in-matlab/


I = im2double(I);

% Threshold images
% Those pixels that have value greater than threshold become 1, the rest 0
O = (I > thr);

% Reshape back to original size
O = reshape(O, size(I));

end