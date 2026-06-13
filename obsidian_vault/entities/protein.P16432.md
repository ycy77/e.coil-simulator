---
entity_id: "protein.P16432"
entity_type: "protein"
name: "hycF"
source_database: "UniProt"
source_id: "P16432"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycF hevF b2720 JW2690"
---

# hycF

`protein.P16432`

## Static

- Type: `protein`
- Source: `UniProt:P16432`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable electron transfer protein for hydrogenase 3. The hycBCDEFG genes in E.coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase complex. HycF is thought to be a 4Fe-4S ferredoxin type protein, an intermediate electron carrier protein . In the cryo-EM structures of FHL reported by , HycF interacts with HycB and with FdhF, and it coordinates an unpredicted metal ion (tentatively assigned as an iron).

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

FUNCTION: Probable electron transfer protein for hydrogenase 3.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2720|gene.b2720]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16432`
- `KEGG:ecj:JW2690;eco:b2720;ecoc:C3026_14965;`
- `GeneID:947048;`
- `GO:GO:0006007; GO:0009060; GO:0009061; GO:0009326; GO:0015944; GO:0016020; GO:0016651; GO:0019645; GO:0046872; GO:0051539`

## Notes

Formate hydrogenlyase subunit 6 (FHL subunit 6) (Hydrogenase-3 component F)
