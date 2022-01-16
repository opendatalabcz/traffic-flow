import tensorflow as tf


class MobileNetEmbedder(tf.keras.Model):
    """
    MobileNetEmbedder loads a MobileNetV2 pretrained on Imagenet1000, with classification layer removed,
    exposing the bottleneck layer, outputting a feature of size 1280.
    """

    def __init__(self):
        original_inputs = tf.keras.layers.Input([None, None, 3], dtype=tf.uint8, ragged=True)

        inputs = original_inputs.to_tensor()
        inputs = tf.cast(inputs, tf.float32)
        inputs = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)

        mobilenet = tf.keras.applications.mobilenet_v2.MobileNetV2(
            input_tensor=inputs, include_top=False, pooling="avg"
        )

        super().__init__(inputs=original_inputs, outputs=mobilenet.output)

    def predict(self, data, *args, **kwargs):
        """Get feature embeddings for the input image data.

        @param data: list of numpy arrays of (H x W x C)
        @return: features tf.Tensor with (batch_size x 1280)
        """
        tf_data = tf.ragged.stack(data)
        return super().predict(tf_data, *args, **kwargs)
