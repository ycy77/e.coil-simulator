---
entity_id: "protein.P0AAJ8"
entity_type: "protein"
name: "hybA"
source_database: "UniProt"
source_id: "P0AAJ8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hybA b2996 JW2964"
---

# hybA

`protein.P0AAJ8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAJ8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Participates in the periplasmic electron-transferring activity of hydrogenase 2 during its catalytic turnover. The hybA-encoded protein may be involved in the periplasmic electron-transferring activity of hydrogenase 2 during catalytic turnover . hybA contains a single C-terminal transmembrane helix; HybA is assembled in a Tat-dependent manner . hybA contains 16 cysteines and contains 4 predicted [Fe-S] binding sites (see also ). An hybA in-frame deletion mutant can not grow on glycerol and fumarate as the sole energy sources, and its reduced fumarate-dependent hydrogen uptake activity is comparable to a hybC deletion mutant; however, the HybOHybC complex is correctly targeted to the membrane . HybA is essential for electron transfer from H(2) to the quinone pool; it is also essential for the H(2) evolving redox reaction; it is not required for electron transfer to and from redox active viologen dyes in whole cells of E. coli .

## Biological Role

Component of hydrogenase 2 (complex.ecocyc.CPLX0-8762), hydrogenase 2 (complex.ecocyc.FORMHYDROG2-CPLX).

## Annotation

FUNCTION: Participates in the periplasmic electron-transferring activity of hydrogenase 2 during its catalytic turnover.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8762|complex.ecocyc.CPLX0-8762]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.FORMHYDROG2-CPLX|complex.ecocyc.FORMHYDROG2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2996|gene.b2996]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAJ8`
- `KEGG:ecj:JW2964;eco:b2996;ecoc:C3026_16385;`
- `GeneID:86947880;93778989;944842;`
- `GO:GO:0005886; GO:0009061; GO:0009326; GO:0015944; GO:0019588; GO:0036397; GO:0042597; GO:0046872; GO:0047067; GO:0051539`

## Notes

Hydrogenase-2 operon protein HybA
