---
entity_id: "protein.P0AGM9"
entity_type: "protein"
name: "xanP"
source_database: "UniProt"
source_id: "P0AGM9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16096267}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xanP yicE b3654 JW3629"
---

# xanP

`protein.P0AGM9`

## Static

- Type: `protein`
- Source: `UniProt:P0AGM9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16096267}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Specific, proton motive force-dependent high-affinity transporter for xanthine. {ECO:0000269|PubMed:16096267}. The XanP protein (formerly YicE) is a member of the NCS2 (Nucleobase-Cation Symport-2) family of transporters. XanP is a specific, high-affinity, proton motive force-dependent xanthine transporter with a Km of 2.9 to 3.8 μM . XanP is unable to transport guanine, hypoxanthine, uric acid, and uracil, or to efficiently recognize certain xanthine or uric acid analogues .

## Biological Role

Catalyzes xanthine:proton symport (reaction.ecocyc.RXN-5076).

## Annotation

FUNCTION: Specific, proton motive force-dependent high-affinity transporter for xanthine. {ECO:0000269|PubMed:16096267}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3654|gene.b3654]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGM9`
- `KEGG:ecj:JW3629;eco:b3654;ecoc:C3026_19795;`
- `GeneID:93778369;948172;`
- `GO:GO:0005886; GO:0042906; GO:0042907`

## Notes

Xanthine permease XanP
