import { AutoProcessor, AutoTokenizer, Moondream1ForConditionalGeneration, RawImage } from 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@3.4.1';

const MODEL_ID = 'Xenova/moondream2';

let processor = null;
let tokenizer = null;
let model = null;

self.onmessage = async (event) => {
  const { type, data } = event.data;

  if (type === 'init') {
    try {
      self.postMessage({ type: 'progress', message: 'Loading tokenizer...' });
      tokenizer = await AutoTokenizer.from_pretrained(MODEL_ID);

      self.postMessage({ type: 'progress', message: 'Loading processor...' });
      processor = await AutoProcessor.from_pretrained(MODEL_ID);

      self.postMessage({ type: 'progress', message: 'Loading model (this may take a moment)...' });
      model = await Moondream1ForConditionalGeneration.from_pretrained(MODEL_ID, {
        dtype: {
          embed_tokens: 'fp16',
          vision_encoder: 'fp16',
          decoder_model_merged: 'q4',
        },
        progress_callback: (progress) => {
          if (progress.status === 'downloading') {
            const percent = progress.progress ? Math.round(progress.progress) : 0;
            self.postMessage({ type: 'progress', message: `Downloading: ${progress.file} (${percent}%)` });
          } else if (progress.status === 'loading') {
            self.postMessage({ type: 'progress', message: 'Loading model into memory...' });
          }
        }
      });

      self.postMessage({ type: 'ready' });
    } catch (error) {
      self.postMessage({ type: 'error', message: error.message });
    }
  }

  if (type === 'ask') {
    try {
      const { imageSource, question } = data;

      // Load the image
      const image = await RawImage.read(imageSource);

      // Moondream prompt format
      const prompt = `<image>\n\nQuestion: ${question}\n\nAnswer:`;

      // Process the image
      const visionInputs = await processor(image);

      // Tokenize the prompt
      const textInputs = tokenizer(prompt);

      // Generate answer
      const outputIds = await model.generate({
        ...visionInputs,
        ...textInputs,
        do_sample: false,
        max_new_tokens: 64,
      });

      // Decode the generated tokens (skip the input tokens)
      const inputLength = textInputs.input_ids.dims[1];
      const generatedIds = outputIds.slice(null, [inputLength, null]);
      const answer = tokenizer.batch_decode(generatedIds, { skip_special_tokens: true })[0].trim();

      self.postMessage({ type: 'answer', answer });
    } catch (error) {
      self.postMessage({ type: 'error', message: error.message });
    }
  }
};
