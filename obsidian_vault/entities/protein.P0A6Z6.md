---
entity_id: "protein.P0A6Z6"
entity_type: "protein"
name: "nikR"
source_database: "UniProt"
source_id: "P0A6Z6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nikR yhhG b3481 JW3446"
---

# nikR

`protein.P0A6Z6`

## Static

- Type: `protein`
- Source: `UniProt:P0A6Z6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional repressor of the nikABCDE operon. Is active in the presence of excessive concentrations of intracellular nickel.

## Biological Role

Component of DNA-binding transcriptional repressor NikR-Ni2+ (complex.ecocyc.CPLX0-7707), NikR-Ni transcriptional repressor (complex.ecocyc.MONOMER0-1781).

## Annotation

FUNCTION: Transcriptional repressor of the nikABCDE operon. Is active in the presence of excessive concentrations of intracellular nickel.

## Outgoing Edges (8)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7707|complex.ecocyc.CPLX0-7707]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` --> [[complex.ecocyc.MONOMER0-1781|complex.ecocyc.MONOMER0-1781]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3476|gene.b3476]] `RegulonDB` `S` - regulator=NikR; target=nikA; function=-
- `represses` --> [[gene.b3477|gene.b3477]] `RegulonDB` `S` - regulator=NikR; target=nikB; function=-
- `represses` --> [[gene.b3478|gene.b3478]] `RegulonDB` `S` - regulator=NikR; target=nikC; function=-
- `represses` --> [[gene.b3479|gene.b3479]] `RegulonDB` `S` - regulator=NikR; target=nikD; function=-
- `represses` --> [[gene.b3480|gene.b3480]] `RegulonDB` `S` - regulator=NikR; target=nikE; function=-
- `represses` --> [[gene.b3481|gene.b3481]] `RegulonDB` `S` - regulator=NikR; target=nikR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3481|gene.b3481]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6Z6`
- `KEGG:ecj:JW3446;eco:b3481;ecoc:C3026_18850;`
- `GeneID:86862123;93778510;947995;`
- `GO:GO:0000976; GO:0001046; GO:0001217; GO:0003677; GO:0005667; GO:0006355; GO:0010045; GO:0016151; GO:0032993; GO:0042802; GO:0043565; GO:2000143`

## Notes

Nickel-responsive regulator
