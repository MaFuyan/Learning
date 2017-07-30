imgPath = '/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/data/gt_line/'
resultPath = '/home/chen/Pictures/dataset/icdar/icdar2017rctw_train_v1.2/data/gt_line_result/'
imgData = dir([imgPath,'*.jpg']);
nImg = length(imgData);
for i=1:nImg
    [~, name, ~] = fileparts(imgData(i).name);
    img_path = [imgPath, imgData(i).name];
    save_path = [resultPath,name,'.jpg'];
    BW = im2bw(imread(img_path));
    img = imfill(BW,'holes');
    imwrite(img,save_path);
end