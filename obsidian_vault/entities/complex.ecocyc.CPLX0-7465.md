---
entity_id: "complex.ecocyc.CPLX0-7465"
entity_type: "complex"
name: "alanine racemase 2"
source_database: "EcoCyc"
source_id: "CPLX0-7465"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# alanine racemase 2

`complex.ecocyc.CPLX0-7465`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7465`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P29012|protein.P29012]]

## Enriched Summary

Alanine racemase 2 (DadX) catalyzes the interconversion of D- and L-alanine. E. coli has two alanine racemases, DadX and ALARACEBIOSYN-MONOMER Alr. DadX is responsible for most of the alanine racemase activity in the cell and is inducible by either form of alanine, and repressible by glucose. Alr, in contrast, is constitutively expressed . DadX expression is regulated by PD00353 in combination with alanine and leucine. Lrp alone binds to repressor sites, inhibiting expression. In the presence of alanine or leucine, Lrp stops binding repressor sites but continues binding activating sites, leading to substantially increased DadX expression . During growth on glucose, dadX expression is regulated by catabolite repression . DadX is functionally active as a dimer . Overexpression of a DadX K35A Y253A double mutant results in growth inhibition. This dominant negative phenotype is presumably due to the sequestration of wild-type enzyme by the formation of inactive wild type-mutant heterodimers . Alanine racemase has been a target for antibacterial drug development . Using liquid chromatography/tandem mass spectrometry, D-cycloserine was shown to be an in vivo inhibitor of D-alanine production by alanine racemase . Elimination of alanine racemase activity in the cell requires the deletion of both alr and dadX; overexpression of metC can suppress alanine racemase deficiency...

## Biological Role

Catalyzes ALARACECAT-RXN (reaction.ecocyc.ALARACECAT-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

Alanine racemase 2 (DadX) catalyzes the interconversion of D- and L-alanine. E. coli has two alanine racemases, DadX and ALARACEBIOSYN-MONOMER Alr. DadX is responsible for most of the alanine racemase activity in the cell and is inducible by either form of alanine, and repressible by glucose. Alr, in contrast, is constitutively expressed . DadX expression is regulated by PD00353 in combination with alanine and leucine. Lrp alone binds to repressor sites, inhibiting expression. In the presence of alanine or leucine, Lrp stops binding repressor sites but continues binding activating sites, leading to substantially increased DadX expression . During growth on glucose, dadX expression is regulated by catabolite repression . DadX is functionally active as a dimer . Overexpression of a DadX K35A Y253A double mutant results in growth inhibition. This dominant negative phenotype is presumably due to the sequestration of wild-type enzyme by the formation of inactive wild type-mutant heterodimers . Alanine racemase has been a target for antibacterial drug development . Using liquid chromatography/tandem mass spectrometry, D-cycloserine was shown to be an in vivo inhibitor of D-alanine production by alanine racemase . Elimination of alanine racemase activity in the cell requires the deletion of both alr and dadX; overexpression of metC can suppress alanine racemase deficiency . dadX and dadA are expressed and show a mutant phenotype within the oxic nutrient-deprived region at mid-height of spatially structured biofilms, where they enable utilization of alanine as a carbon and nitrogen source .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ALARACECAT-RXN|reaction.ecocyc.ALARACECAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P29012|protein.P29012]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7465`
- `QSPROTEOME:QS00049623`

## Notes

2*protein.P29012
