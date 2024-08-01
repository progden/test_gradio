import gradio as gr

from readpdf import read_files_to_text


def process_multi_file(txt, slid, multiple_files):
    texts = read_files_to_text(multiple_files)

    return "\n\n".join(texts)


demo = gr.Interface(
    fn=process_multi_file,
    inputs=["text","slider", gr.UploadButton("Upload a file", file_count="multiple")],
    outputs=["text"],
)

if __name__ == "__main__":
    demo.launch()
