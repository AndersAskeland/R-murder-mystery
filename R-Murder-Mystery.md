---
title: "R murder mystery"
output:
  html_document:
    df_print: paged
    code_folding: hide
editor_options: 
  markdown: 
    wrap: 72
---



There's been a Murder in R City! The R Murder Mystery is designed to be
both a lesson to learn R concepts and commands and a fun game for R
users to solve an intriguing crime. The mystery is directly based on
[The SQL Murder Mystery](https://mystery.knightlab.com), which again was
inspired by [a crime in the neighboring Terminal
City](https://github.com/veltman/clmystery).

Through the usage of various functions and methods learned during the
course, you'll be able to solve the mystery.

## The mystery

> A crime has taken place and the detective needs your help. The
> detective gave you the crime scene report, but you somehow lost it.
> You vaguely remember that the crime was a murder that occurred
> sometime on Jan.15, 2018 and that it took place in R City. All the
> clues to this mystery are buried in a several files, and you need to
> use R to navigate through this vast network of information. Your first
> step to solving the mystery is to retrieve the corresponding crime
> scene report from the police department's database.

You have the following files at your disposal to solve the mystery:
![File structure](images/file_structure.png) You might notice that
certain variables have a key and arrow associated to them.

![Key](images/paste-27ECAE2C.png)
**Key**: A unique identifier for each row in the table 

![Arrow](images/paste-9621EB24.png){width="82"}
**Arrow**: Used to reference data in one table to those in another table (i.e. they are the same in both tables).

Download the data by running:


```{.r .fold-show}
******
```

PS: The interview data is separated into \*\*\*\* files and is contained
within its own folder.

### Hard

You can in in fact solve the entire mystery based on the information
given above. This can be difficult, and as such, most people are recommended
to follow along with the guided section below.

### Guided

Begin in by revealing part 1. Hereafter reveal new section as you
complete the previous one.

If you at any point get stuck you can reveal hints to help yourselves
along. You can also view a code example, if the hints are not enough.


<details style='margin-bottom: 1rem'><summary><strong><em>Hint 0: Click to reveal!</em></strong></summary>
<blockquote><p>
If you can, try to refrain from using hints. If you are stuck at a section for more than 10 minutes, reveal the first hint and repeat. The last hint in any given sequence is the solution for that given part.
</p></blockquote>
</details>

<button class="collapsible">

Part 1

</button>

::: content
<p>

## Part 1: Investigate the crime scene report

Investigate the crime scene report for any usable information. For this
task you will need to read in the crime scene file, and filter and
select the column the column with the report interesting for you.


<details style='margin-bottom: 1rem'><summary><strong><em>Hint 1: Click to reveal!</em></strong></summary>
<blockquote><p>
You want to look at the crime_scene_report.csv file and look for a murder that happened on jan. 15, 2018 in R City
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 2: Click to reveal!</em></strong></summary>
<blockquote><p>
Read data with vroom() or read_csv()
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 3: Click to reveal!</em></strong></summary>
<blockquote><p>
You should use the dplyr functions filter and select
</p></blockquote>
</details>

#### Solution code


```r
# Read data
crime_scene_report <- vroom::vroom("raw-data/csv/crime_scene_report.csv")

# Find crime scene report
crime_scene_report %>% 
    dplyr::filter(date == "20180115" & 
                      type == "murder" &
                      city == "R City") %>%
    dplyr::select(description)
```

</p>
:::

<button class="collapsible">

Part 2

</button>

::: content
<p>

## Part 2 - Find witnesses

Find the witness statement.


<details style='margin-bottom: 1rem'><summary><strong><em>Hint 1: Click to reveal!</em></strong></summary>
<blockquote><p>
You cant find the witness statement before finding out which persons gave the statmenents.
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 2: Click to reveal!</em></strong></summary>
<blockquote><p>
Look in the person data, and look for person that lives at the last house on Northwestern Dr and a person named Annabel that lives on Franklin Ave
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 3: Click to reveal!</em></strong></summary>
<blockquote><p>
To find the person that lives on Northwestern dr you can use the dplyr function arrange() to sort address numbers
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 4: Click to reveal!</em></strong></summary>
<blockquote><p>
To find Annabel you  can use regular expresions and the stringr function str_detect()
</p></blockquote>
</details>

<details style='margin-bottom: 1rem'><summary><strong><em>Hint 6: Click to reveal!</em></strong></summary>
<blockquote><p>
Look in the person data, and look for person that lives at the last house on Northwestern Dr and a person named Annabel that lives on Franklin Ave
</p></blockquote>
</details>

#### Solution code

```r
# Read person data
person <- vroom::vroom("raw-data/csv/person.csv")

# Find person living on the last house on Northwestern Dr
person %>% 
    dplyr::filter(address_street_name == "Northwestern Dr") %>%
    dplyr::arrange(desc(address_number))

# Find the person named Annabel living on Franklin Ave
person %>% 
    dplyr::filter(address_street_name == "Franklin Ave" &
                     stringr::str_detect(name, "Annabel"))
```

</p>
:::

<button class="collapsible">

Part 3

</button>

::: content
<p>
</p>
:::


<p>
  
</p>

```{=html}
<style>
.collapsible {
  background-color: #777;
  color: white;
  cursor: pointer;
  padding: 18px;
  width: 100%;
  border: none;
  text-align: left;
  outline: none;
  font-size: 15px;
}

.active, .collapsible:hover {
  background-color: #555;
}

.content {
  padding: 0 18px;
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  background-color: #f1f1f1;
}
</style>
```
```{=html}
<script>
var coll = document.getElementsByClassName("collapsible");
var i;
for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "5000px";
    } 
  });
}
</script>
```