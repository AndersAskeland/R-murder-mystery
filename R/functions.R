hint <- function(id, text) {
    glue::glue("

    <details style='margin-bottom: 1rem'><summary><strong><em>Hint {id}: Click to reveal!</em></strong></summary>
    <blockquote><p>
    {text}
    </p></blockquote>
    </details>
    ")
}

code <- function(id, code) {
    glue::glue("

    <details style='margin-bottom: 1rem'><summary><strong><em>Hint {id}: Click to reveal!</em></strong></summary>
    
    ```
    {code}
    ```

    </details>
    ")
}
