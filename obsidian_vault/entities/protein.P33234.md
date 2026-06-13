---
entity_id: "protein.P33234"
entity_type: "protein"
name: "adiY"
source_database: "UniProt"
source_id: "P33234"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "adiY b4116 JW4077"
---

# adiY

`protein.P33234`

## Static

- Type: `protein`
- Source: `UniProt:P33234`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

HTH-type transcriptional regulator AdiY

## Biological Role

Component of DNA-binding transcriptional activator AdiY (complex.ecocyc.CPLX0-13978).

## Annotation

HTH-type transcriptional regulator AdiY

## Outgoing Edges (9)

- `activates` --> [[gene.b1492|gene.b1492]] `RegulonDB` `S` - regulator=AdiY; target=gadC; function=+
- `activates` --> [[gene.b1493|gene.b1493]] `RegulonDB` `S` - regulator=AdiY; target=gadB; function=+
- `activates` --> [[gene.b3212|gene.b3212]] `RegulonDB` `S` - regulator=AdiY; target=gltB; function=+
- `activates` --> [[gene.b3213|gene.b3213]] `RegulonDB` `S` - regulator=AdiY; target=gltD; function=+
- `activates` --> [[gene.b3214|gene.b3214]] `RegulonDB` `S` - regulator=AdiY; target=gltF; function=+
- `activates` --> [[gene.b3516|gene.b3516]] `RegulonDB` `S` - regulator=AdiY; target=gadX; function=+
- `activates` --> [[gene.b3517|gene.b3517]] `RegulonDB` `S` - regulator=AdiY; target=gadA; function=+
- `activates` --> [[gene.b4117|gene.b4117]] `RegulonDB` `S` - regulator=AdiY; target=adiA; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-13978|complex.ecocyc.CPLX0-13978]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b4116|gene.b4116]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33234`
- `KEGG:ecj:JW4077;eco:b4116;ecoc:C3026_22240;`
- `GeneID:948627;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0045893`

## Notes

HTH-type transcriptional regulator AdiY
