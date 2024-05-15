# Person Identifier FYP

This repository contains the code for a person identifier project, which involves identifying individuals based on their walking patterns. The project is an R&D effort and does not include collaborators.

## Data Preprocessing

### Frames Generation
Frames are generated from video sequences capturing individuals walking.

### Silhouettes Generation
Silhouettes of individuals are extracted from the frames.

### Normalize Silhouettes
The extracted silhouettes are normalized to ensure consistency in feature representation.

### Gait Energy Image Generation
Gait energy images (GEIs) are generated from the normalized silhouettes.

## Fine-tune Models

The following pre-trained models were fine-tuned on the dataset:

- VGG16
- ResNet50
- InceptionV3
- MobileNetV2
- EfficientNetB7

## Models Architecture Code

The following models were coded from scratch and trained on the dataset without fine-tuning:

- ResNet18
- ResNet50
- MobileNetV2
- InceptionV3
- EfficientNetB0
- GaitNet (Proposed Model)

## Contact Information

For any inquiries or further information, please contact:

Email: saadmalik4zd@gmail.com
Phone: +923200072098
