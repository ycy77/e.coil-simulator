---
entity_id: "protein.P0A8N0"
entity_type: "protein"
name: "matP"
source_database: "UniProt"
source_id: "P0A8N0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01073, ECO:0000269|PubMed:18984159}. Note=Accumulates in the cell as a discrete focus that colocalizes with the Ter macrodomain."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "matP ycbG b0956 JW0939"
---

# matP

`protein.P0A8N0`

## Static

- Type: `protein`
- Source: `UniProt:P0A8N0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01073, ECO:0000269|PubMed:18984159}. Note=Accumulates in the cell as a discrete focus that colocalizes with the Ter macrodomain.

## Enriched Summary

FUNCTION: Required for spatial organization of the terminus region of the chromosome (Ter macrodomain) during the cell cycle. Prevents early segregation of duplicated Ter macrodomains during cell division. Binds specifically to matS, which is a 13 bp signature motif repeated within the Ter macrodomain. {ECO:0000255|HAMAP-Rule:MF_01073, ECO:0000269|PubMed:18984159}. The MatP protein colocalizes with the chromosomal terminus region in a discrete focus in the cell. MatP binds specifically to matS sites within the Ter macrodomain (MD) both in vitro and in vivo, preventing early segregation of that domain during cell division . Segregation of the dif region depends on MatP and G6464-MONOMER FtsK . After cell division, the Ter MD migrates from the cell pole to mid-cell, where it is anchored via the interaction of MatP with the Z ring-associated protein CPLX0-7686 ZapB . MatP interacts with the CPLX0-2561 complex and displaces it from ter . A contact map of the E. coli chromosome and a quantitative fluorescence microscopy study show that MatP is responsible for the formation of a specific chromosomal domain through restricting the long-range contact-promoting activity of MukBEF in ter and, thus directs MukBEF localization along the chromosome . MatP works together with ZapA and ZapB to localize the divisome ; EG10347-MONOMER, ZapA, ZapB and MatP form a multilayered protein network...

## Biological Role

Component of macrodomain Ter protein (complex.ecocyc.CPLX0-7789).

## Annotation

FUNCTION: Required for spatial organization of the terminus region of the chromosome (Ter macrodomain) during the cell cycle. Prevents early segregation of duplicated Ter macrodomains during cell division. Binds specifically to matS, which is a 13 bp signature motif repeated within the Ter macrodomain. {ECO:0000255|HAMAP-Rule:MF_01073, ECO:0000269|PubMed:18984159}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7789|complex.ecocyc.CPLX0-7789]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0956|gene.b0956]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8N0`
- `KEGG:ecj:JW0939;eco:b0956;ecoc:C3026_05845;`
- `GeneID:93776458;945570;`
- `GO:GO:0005543; GO:0005737; GO:0006355; GO:0007059; GO:0042803; GO:0043565; GO:0051276; GO:0051289; GO:0051301; GO:0097047`

## Notes

Macrodomain Ter protein
