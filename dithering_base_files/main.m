% Image dithering library
% Written by Michalis Zervos - All rights reserved
% http://michal.is/projects/image-dithering-in-matlab/


%%

clear all;
close all;
clc;



%% "Error diffusion method
I1 = imread('Images\lena-y.png');


% Compute the images with both filters
T1F1 = errorDiffusion(I1, 1);

%T1F2 = errorDiffusion(I1, 2);


% Compute Mean Squared Error
e1f1 = msei(I1, T1F1);

%e1f2 = msei(I1, T1F2);

%me1 = mean([e1f1 e2f1]);

%fprintf('Error diffusion method - Floyd & Steinberg filter\n');

%fprintf('Mean: %f\n\n', me1);
%fprintf('Error diffusion method - Stucki filter\n');



% Show images
figure; imshow(T1F1); title(['Lena - Error diffusion with Floyd-Steinberg filter - MSE: ', num2str(e1f1)]);
%figure; imshow(T2F1); title(['Wool - Error diffusion with Floyd-Steinberg filter - MSE: ', num2str(e1f1)]);
%figure; imshow(T1F2); title(['Lena - Error diffusion with Stucki filter - MSE: ', num2str(e1f2)]);
%figure; imshow(T2F2); title(['Wool - Error diffusion with Stucki filter - MSE: ', num2str(e1f2)]);

 
%imwrite(T1F1, 'ErrorDiffusionFloyd_Lena.png');
%imwrite(T2F1, 'ErrorDiffusionFloyd_Wool.png');
%imwrite(T1F2, 'ErrorDiffusionStucki_Lena.png');
%imwrite(T2F2, 'ErrorDiffusionStucki_Wool.png');


%%