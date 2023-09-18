var markdownText = "# This is a heading\n\nThis is some **bold** and *italic* text.";

// 将Markdown文本转换为HTML
var htmlContent = marked(markdownText);

// 将HTML内容插入到div元素中
document.getElementById("markdown-content").innerHTML = htmlContent;
