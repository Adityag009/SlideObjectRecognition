# SlideObjectRecognition

The project aimed to develop a solution for automatic detection of various elements within PowerPoint presentations. The dataset used in this project consisted of more than 800 annotated images of PowerPoint slides, with each image containing one or more elements belonging to ten different classes. The classes represented distinct types of elements found in PowerPoint slides, such as body text, bullet points, headers, images, logos, subtitles, titles, and more.

The project workflow involved several steps. Firstly, the dataset was meticulously annotated, ensuring that each element in the images was labeled with the appropriate class. This process enabled the creation of a comprehensive and accurately labeled dataset.

Next, the annotated dataset was divided into training, testing, and validation sets. The training set was used to train a YOLOv8 segmentation model. The YOLOv8 model is known for its excellent object detection capabilities and was well-suited for this project's requirements. The model was trained on the training set, with each image resized to a resolution of 640x640 pixels to maintain consistency.

During the training process, the model learned to identify and classify different elements within the PowerPoint presentations. The training was carried out for 100 epochs, allowing the model to refine its predictions and improve its performance over time. The training process involved forward and backward passes, optimization, and monitoring of metrics such as loss.

Following the training phase, the model's performance was evaluated using the validation set. Metrics such as precision, recall, mean average precision (mAP), and others were calculated to assess the model's accuracy and ability to detect different element classes within the PowerPoint slides.

The trained model achieved promising results, with an overall mAP of 0.674. The model demonstrated strong performance across different element classes, including body text, bullet points, headers, images, logos, subtitles, titles, and more.

To provide visual insights, several images were generated during the training and validation processes. These images included confusion matrices, detection results, and predicted bounding boxes on sample images, offering a visual representation of the model's performance.

Finally, the model was further evaluated using the testing set to assess its generalization and ability to detect elements in unseen PowerPoint presentations. The model showed consistent and reliable detection performance, demonstrating its effectiveness in identifying various elements within PowerPoint slides.

In summary, this project successfully developed a YOLOv8-based solution for automated detection of elements within PowerPoint presentations. The trained model showcased accurate detection across multiple element classes, enabling efficient analysis and processing of PowerPoint content. The project's outcome opens doors for various applications, such as content analysis, slide categorization, and automation of PowerPoint-related tasks.
