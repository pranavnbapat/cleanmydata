from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load the pre-trained T5 model and tokenizer for text correction
model_name = "prithivida/grammar_error_correcter_v1"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)


def correct_text(text: str) -> str:
    """
    Function to perform contextual spell checking and grammar correction using T5.
    :param text: Input text string with potential errors.
    :return: Corrected text string.
    """
    # Preprocessing text for T5 model by framing as a 'grammar correction' task
    input_text = f"grammar correction: {text}"

    # Tokenize input text and check its contents
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    print(f"Tokenized Inputs: {inputs}")

    # Generate corrected text using model
    outputs = model.generate(inputs, max_length=512, num_beams=4, early_stopping=True)
    print(f"Model Outputs: {outputs}")

    # Decode the output from model to get corrected text
    corrected_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"Decoded Output: {corrected_text}")

    return corrected_text


# Test the spell checker with an example
# input_document = """
# This is a smple sentence with sme spelling mistakes. We are going to run it thrugh the T5 model to corect all errors.
# """

# corrected_document = correct_text(input_document)
# print("Original Document:")
# print(input_document)
# print("\nCorrected Document:")
# print(corrected_document)
