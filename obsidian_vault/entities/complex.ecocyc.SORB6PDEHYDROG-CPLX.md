---
entity_id: "complex.ecocyc.SORB6PDEHYDROG-CPLX"
entity_type: "complex"
name: "sorbitol-6-phosphate 2-dehydrogenase"
source_database: "EcoCyc"
source_id: "SORB6PDEHYDROG-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sorbitol-6-phosphate 2-dehydrogenase

`complex.ecocyc.SORB6PDEHYDROG-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SORB6PDEHYDROG-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05707|protein.P05707]]

## Enriched Summary

E. coli K-12 is able to utilize sorbitol as a sole carbon source. Sorbitol is phosphorylated during transport into the cell and then converted into the glycolytic intermediate, fructose-6-phosphate, by sorbitol-6-phosphate dehydrogenase . The enzyme is highly specific for D-sorbitol 6-phosphate as substrate and for NAD+ as cofactor. It cannot utilize NADP+ . srlD, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 . E. coli K-12 is able to utilize sorbitol as a sole carbon source. Sorbitol is phosphorylated during transport into the cell and then converted into the glycolytic intermediate, fructose-6-phosphate, by sorbitol-6-phosphate dehydrogenase . The enzyme is highly specific for D-sorbitol 6-phosphate as substrate and for NAD+ as cofactor. It cannot utilize NADP+ . srlD, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 .

## Biological Role

Catalyzes SORB6PDEHYDROG-RXN (reaction.ecocyc.SORB6PDEHYDROG-RXN).

## Annotation

E. coli K-12 is able to utilize sorbitol as a sole carbon source. Sorbitol is phosphorylated during transport into the cell and then converted into the glycolytic intermediate, fructose-6-phosphate, by sorbitol-6-phosphate dehydrogenase . The enzyme is highly specific for D-sorbitol 6-phosphate as substrate and for NAD+ as cofactor. It cannot utilize NADP+ . srlD, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SORB6PDEHYDROG-RXN|reaction.ecocyc.SORB6PDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P05707|protein.P05707]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:SORB6PDEHYDROG-CPLX`
- `QSPROTEOME:QS00181711`

## Notes

4*protein.P05707
