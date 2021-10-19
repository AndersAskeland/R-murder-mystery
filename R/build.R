# Message
message("Creating index.html")

# Build
rmarkdown::render(input = "R-Murder-Mystery.Rmd", output_format = "html_document", output_file = "index.html")