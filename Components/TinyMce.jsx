import { Editor } from "@tinymce/tinymce-react";

export default function TinyMce () {
  return (
    <Editor
      initialValue="<p>This is some initial content</p>"
      init={{
        //  Add your TinyMCE configurations here
        plugins: ["text", "link"],
        toolbar: "undo redo | bold italic | link",
      }}
    />
  );
}
