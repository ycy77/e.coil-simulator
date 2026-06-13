---
entity_id: "protein.P0AC51"
entity_type: "protein"
name: "zur"
source_database: "UniProt"
source_id: "P0AC51"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zur yjbK b4046 JW5714"
---

# zur

`protein.P0AC51`

## Static

- Type: `protein`
- Source: `UniProt:P0AC51`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as a negative controlling element, employing Zn(2+) as a cofactor to bind the operator of the repressed genes (znuACB).

## Biological Role

Component of DNA-binding transcriptional repressor Zur (complex.ecocyc.CPLX0-7679).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Acts as a negative controlling element, employing Zn(2+) as a cofactor to bind the operator of the repressed genes (znuACB).

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7679|complex.ecocyc.CPLX0-7679]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1178|gene.b1178]] `RegulonDB` `S` - regulator=Zur; target=pliG; function=-
- `represses` --> [[gene.b1857|gene.b1857]] `RegulonDB` `S` - regulator=Zur; target=znuA; function=-
- `represses` --> [[gene.b1858|gene.b1858]] `RegulonDB` `S` - regulator=Zur; target=znuC; function=-
- `represses` --> [[gene.b1859|gene.b1859]] `RegulonDB` `S` - regulator=Zur; target=znuB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4046|gene.b4046]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC51`
- `KEGG:ecj:JW5714;eco:b4046;ecoc:C3026_21865;`
- `GeneID:93777785;948552;`
- `GO:GO:0000976; GO:0001217; GO:0003700; GO:0005829; GO:0006351; GO:0008270; GO:0032993; GO:0042802; GO:0045892; GO:1900376`

## Notes

Zinc uptake regulation protein (Zinc uptake regulator)
