# vml

_A Visual Introduction to Machine Learning_

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/mbforbes/vml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](blob/master/LICENSE.txt)

This is a work in progress.

## Chapters

1. Matrices — basic arrays and matrices, visualized

## Viewing

You have two choices:

- Click the `launch binder` button above to view the chapters as interactive
  Jupyter notebooks. The raw source is available in `notebooks/`.

- Download a static rendering of the notebooks in some format. Formats are
  available in `static/` (e.g. `HTML`).

## Acknowledgments

Thanks to Nelson Liu for reading drafts of these chapters. Thanks to Colin
Lockard, Elizabeth Clark, John Thickstun, and Lucy Lin for their feedback on
preliminary versions of this material.

### TODOs

- [x] make `list` vs `ndarray` distinction more clear in notebook
- [x] pull visualization helpers into some kinda `util.py`
- [x] wrap plain text at smaller width
- [x] investigate script (w/ `jupyter`?) to generate HTML
- [x] debug Jupyter `nbconvert` PDF generation---not feasible to do
  programmatically; javascript plots don't play well.
- [ ] Remove `numpy` intro crap from `1_matrices` into some kinda snippets
  folder; this isn't "a numpy intro to ML"
- [ ] Revise `1_matrices` to have text output, focus on visuals, more side-by-
  side plots, and possibly add more matrix operations (can always add more later
  too).
- [ ] make conversion target `hide_code_html`
- [ ] Remove chapter number markings. Change grouping to 'basic', etc.
- [ ] Make generic header for each notebook (could be some kinda header()
  function which outputs HTML?)---include title, name, github, website probably.
- [ ] check if `mybinder.org` auto-builds new versions. If not, see if there's
  some hook (e.g. github) to do this.
