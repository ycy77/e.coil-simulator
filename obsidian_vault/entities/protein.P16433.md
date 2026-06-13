---
entity_id: "protein.P16433"
entity_type: "protein"
name: "hycG"
source_database: "UniProt"
source_id: "P16433"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycG hevG b2719 JW2689"
---

# hycG

`protein.P16433`

## Static

- Type: `protein`
- Source: `UniProt:P16433`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Formate hydrogenlyase subunit 7 (FHL subunit 7) (Hydrogenase-3 component G) The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycG has similarity to small subunits of hydrogenases . HycG is absent in extracts of a slyD mutant strain grown anaerobically in the absence of nickel; however, this phenotype was restored upon addition of nickel to the growth medium . The HycG protein was undetectable in a hypA mutant and a hypA slyD double mutant .

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

Formate hydrogenlyase subunit 7 (FHL subunit 7) (Hydrogenase-3 component G)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2719|gene.b2719]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16433`
- `KEGG:ecj:JW2689;eco:b2719;ecoc:C3026_14960;`
- `GeneID:947191;`
- `GO:GO:0006007; GO:0008137; GO:0009061; GO:0009326; GO:0015944; GO:0016491; GO:0019645; GO:0046872; GO:0048038; GO:0051539`

## Notes

Formate hydrogenlyase subunit 7 (FHL subunit 7) (Hydrogenase-3 component G)
