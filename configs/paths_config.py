dataset_paths = {
	'ffhq': '',
	'celeba_test': '',

	'cars_train': '',
	'cars_test': '',

	'church_train': '',
	'church_test': '',

	'horse_train': '',
	'horse_test': '',

	'afhq_wild_train': '',
	'afhq_wild_test': '',

	'anime_train': r"C:\Users\Aravind\OneDrive - Nanyang Technological University\FYP\GitHub\CLIP2StyleGAN\PCA_images\0",
	'anime_test': r"C:\Users\Aravind\OneDrive - Nanyang Technological University\FYP\GitHub\CLIP2StyleGAN\PCA_images\1",

}

model_paths = {
	'tadne': r"C:\Users\Aravind\OneDrive - Nanyang Technological University\FYP\GitHub\CLIP2StyleGAN\network-tadne-stylegan2.pt.pkl",
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'resnet34': 'pretrained_models/resnet34-333f7ec4.pth',
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'stylegan_cars': 'pretrained_models/stylegan2-car-config-f.pt',
	'stylegan_church': 'pretrained_models/stylegan2-church-config-f.pt',
	'stylegan_horse': 'pretrained_models/stylegan2-horse-config-f.pt',
	'stylegan_ada_wild': 'pretrained_models/afhqwild.pt',
	'stylegan_toonify': 'pretrained_models/ffhq_cartoon_blended.pt',
	'shape_predictor': 'pretrained_models/shape_predictor_68_face_landmarks.dat',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pt'
}



#python scripts/train_restyle_psp.py --dataset_type=anime --encoder_type=ResNetBackboneEncoder --exp_dir=experiment/restyle_psp_ffhq_encode --workers=8 --batch_size=8 --test_batch_size=8 --test_workers=8 --val_interval=5000 --save_interval=10000 --start_from_latent_avg --lpips_lambda=0.8 --l2_lambda=1 --w_norm_lambda=0 --id_lambda=0.1 --input_nc=6 --n_iters_per_batch=5 --output_size=512 --stylegan_weights=tadne