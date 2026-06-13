---
entity_id: "protein.P33030"
entity_type: "protein"
name: "yeiR"
source_database: "UniProt"
source_id: "P33030"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeiR b2173 JW2161"
---

# yeiR

`protein.P33030`

## Static

- Type: `protein`
- Source: `UniProt:P33030`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Zinc chaperone that directly transfers zinc cofactor to target proteins, thereby activating them (By similarity). Zinc is transferred from the CXCC motif in the GTPase domain to the zinc binding site in target proteins in a process requiring GTP hydrolysis (By similarity). {ECO:0000250|UniProtKB:Q8VEH6}. YeiR belongs to the G3E family of P-loop GTPases. The protein binds Zn2+ in vitro; metal binding leads to oligomerization and enhances its GTPase activity. A yeiR deletion mutant shows increased sensitivity to the metal chelator EDTA .

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: Zinc chaperone that directly transfers zinc cofactor to target proteins, thereby activating them (By similarity). Zinc is transferred from the CXCC motif in the GTPase domain to the zinc binding site in target proteins in a process requiring GTP hydrolysis (By similarity). {ECO:0000250|UniProtKB:Q8VEH6}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2173|gene.b2173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33030`
- `KEGG:ecj:JW2161;eco:b2173;ecoc:C3026_12160;`
- `GeneID:946701;`
- `GO:GO:0003924; GO:0005525; GO:0005737; GO:0008270`
- `EC:3.6.5.-`

## Notes

Zinc chaperone YeiR (EC 3.6.5.-)
