import os, glob

input_dir = 'imgs'
resolution = 1027

imgs_fns = glob.glob(os.path.join(input_dir, '**', '*.gif'), recursive=True)
print(f'imgs_fns size: {len(imgs_fns)}')

for img_fn in imgs_fns:
    # out_dir = os.path.dirname(img_fn)
    out_fn = img_fn.replace('.gif', 'v2.gif')
    os.system(f'convert {img_fn} -coalesce -resize {resolution}x{resolution} -fuzz 2% +dither -layers Optimize {out_fn}')