---
entity_id: "protein.Q47141"
entity_type: "protein"
name: "hcaR"
source_database: "UniProt"
source_id: "Q47141"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaR phdR yfhT b2537 JW2521"
---

# hcaR

`protein.Q47141`

## Static

- Type: `protein`
- Source: `UniProt:Q47141`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional activator of the hca operon for 3-phenylpropionic acid catabolism.

## Biological Role

Component of DNA-binding transcriptional dual regulator HcaR-3-phenylpropanoate (complex.ecocyc.MONOMER0-2081).

## Annotation

FUNCTION: Transcriptional activator of the hca operon for 3-phenylpropionic acid catabolism.

## Outgoing Edges (8)

- `activates` --> [[gene.b2538|gene.b2538]] `RegulonDB` `S` - regulator=HcaR; target=hcaE; function=+
- `activates` --> [[gene.b2539|gene.b2539]] `RegulonDB` `S` - regulator=HcaR; target=hcaF; function=+
- `activates` --> [[gene.b2540|gene.b2540]] `RegulonDB` `S` - regulator=HcaR; target=hcaC; function=+
- `activates` --> [[gene.b2541|gene.b2541]] `RegulonDB` `S` - regulator=HcaR; target=hcaB; function=+
- `activates` --> [[gene.b2542|gene.b2542]] `RegulonDB` `S` - regulator=HcaR; target=hcaD; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2081|complex.ecocyc.MONOMER0-2081]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2537|gene.b2537]] `RegulonDB` `S` - regulator=HcaR; target=hcaR; function=-
- `represses` --> [[gene.b4706|gene.b4706]] `RegulonDB` `S` - regulator=HcaR; target=iroK; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2537|gene.b2537]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47141`
- `KEGG:ecj:JW2521;eco:b2537;ecoc:C3026_14055;`
- `GeneID:947000;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0032993; GO:0045892; GO:0045893`

## Notes

Hca operon transcriptional activator HcaR
