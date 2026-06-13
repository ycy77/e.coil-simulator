---
entity_id: "protein.P67444"
entity_type: "protein"
name: "xanQ"
source_database: "UniProt"
source_id: "P67444"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16096267}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xanQ ygfO b2882 JW2850"
---

# xanQ

`protein.P67444`

## Static

- Type: `protein`
- Source: `UniProt:P67444`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16096267}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Specific, proton motive force-dependent high-affinity transporter for xanthine. {ECO:0000269|PubMed:16096267}. XanQ (formerly YgfO) is a member of the NCS2 (Nucleobase-Cation Symport-2) family of transporters. XanQ is a specific, high-affinity, proton motive force-dependent xanthine transporter; XanQ is unable to transport guanine, hypoxanthine, uric acid, and uracil, or to efficiently recognize certain xanthine or uric acid analogues . XanQ is predicted to contain 12-14 transmembrane (TM) regions and contains a nucleobase-ascorbate transporter (NAT) signature motif . XanQ has been subject to extensive cysteine scanning and site-directed mutagenesis . xanQ is located within a cluster of genes that have putative purine catabolic functions . Xanthine is converted to xanthosine-5-phosphate as part of the SALVPURINE2-PWY "xanthine salvage pathway". Review:

## Biological Role

Catalyzes xanthine:proton symport (reaction.ecocyc.RXN-5076).

## Annotation

FUNCTION: Specific, proton motive force-dependent high-affinity transporter for xanthine. {ECO:0000269|PubMed:16096267}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-5076|reaction.ecocyc.RXN-5076]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2882|gene.b2882]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67444`
- `KEGG:ecj:JW2850;eco:b2882;ecoc:C3026_15805;`
- `GeneID:75172982;75205281;949075;`
- `GO:GO:0005886; GO:0042906; GO:0042907`

## Notes

Xanthine permease XanQ
