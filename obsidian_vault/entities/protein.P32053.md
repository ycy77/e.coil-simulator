---
entity_id: "protein.P32053"
entity_type: "protein"
name: "intA"
source_database: "UniProt"
source_id: "P32053"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "intA intX slpA b2622 JW2602"
---

# intA

`protein.P32053`

## Static

- Type: `protein`
- Source: `UniProt:P32053`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. Part of the cryptic P4-like prophage CP4-57, it excises the prophage when overexpressed, which also requires integration host factor (encoded by ihfA and ihfB) (PubMed:7511583). Overexpression of AlpA leads to excision of the CP4-57 prophage, which inactivates ssrA (the gene upstream of the prophage) that encodes tmRNA which is required to rescue stalled ribosomes in a process known as trans-translation (PubMed:7511582). {ECO:0000269|PubMed:7511583}. IntA (SlpA) is a prophage integrase. It is part of the CP4-57 cryptic prophage that is similar to bacteriophage P4. Overexpression of IntA leads to excision and loss of CP4-57 . Expression of intA is transcriptionally regulated by AlpA . Increased synthesis of IntA results in excision of the CP4-57 cryptic prophage, an event which inactivates the gene upstream of intA, ssrA, encoding SSRA-RNA . CP4-57: "cryptic P4-like prophage at min 57" SlpA: "suppressor of Lon-like protease"

## Annotation

FUNCTION: Integrase is necessary for integration of the phage into the host genome by site-specific recombination. In conjunction with excisionase, integrase is also necessary for excision of the prophage from the host genome. Part of the cryptic P4-like prophage CP4-57, it excises the prophage when overexpressed, which also requires integration host factor (encoded by ihfA and ihfB) (PubMed:7511583). Overexpression of AlpA leads to excision of the CP4-57 prophage, which inactivates ssrA (the gene upstream of the prophage) that encodes tmRNA which is required to rescue stalled ribosomes in a process known as trans-translation (PubMed:7511582). {ECO:0000269|PubMed:7511583}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2622|gene.b2622]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32053`
- `KEGG:ecj:JW2602;eco:b2622;`
- `GeneID:946160;`
- `GO:GO:0003677; GO:0006310; GO:0008979; GO:0032359; GO:0044826; GO:0046718`

## Notes

Prophage integrase IntA (Prophage CP4-57 integrase SlpA)
