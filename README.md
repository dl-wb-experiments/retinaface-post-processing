# RetinaFace Post-Processing

Module for post-processing of [RetinaFaceNet](https://github.com/biubug6/Pytorch_Retinaface) inference results.

Model outputs are floating points tensors:

1. name: `face_rpn_cls_prob`, shape: `1, 16800, 2`, format: `B, A*C, 2`, represents detection scores for 2 classes: background and face.

2. name: `face_rpn_bbox_pred`,  shape: `1, 16800, 4`, format: `B, A*C, 4`, represents *detection box deltas*.

3. name: `face_rpn_landmark_pred`, shape: `1, 16800, 10`, format: `B, A*C, 10`, represents *facial landmarks*.

For each output format:

- `B` - batch size
- `A` - number of anchors
- `C` - sum of products of dimensions for each stride, `C = H32 * W32 + H16 * W16 + H8 * W8`
- `H` - feature height with the corresponding stride
- `W` - feature width with the corresponding stride

Detection box deltas have format `[dx, dy, dh, dw]`, where:

- `(dx, dy)` - regression for center of bounding box
- `(dh, dw)` - regression by height and width of bounding box

Facial landmarks have format `[x1, y1, x2, y2, x3, y3, x4, y4, x5, y5]`, where:

- `(x1, y1)` - coordinates of left eye
- `(x2, y2)` - coordinates of rights eye
- `(x3, y3)` - coordinates of nose
- `(x4, y4)` - coordinates of left mouth corner
- `(x5, y5)` - coordinates of right mouth corner
