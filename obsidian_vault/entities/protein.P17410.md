---
entity_id: "protein.P17410"
entity_type: "protein"
name: "chbR"
source_database: "UniProt"
source_id: "P17410"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbR celD b1735 JW1724"
---

# chbR

`protein.P17410`

## Static

- Type: `protein`
- Source: `UniProt:P17410`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dual-function repressor/activator of the chbBCARFG operon. In the absence of the inducing sugar chitobiose, together with NagC, represses the chbBCARFG operon for the uptake and metabolism of chitobiose. In association with Crp, and probably in the presence of chitobiose 6-phosphate, induces the transcription of the chbBCARFG operon. {ECO:0000269|PubMed:18028317}.

## Biological Role

Component of DNA binding transcriptional dual regulator ChbR (complex.ecocyc.CPLX0-8595).

## Annotation

FUNCTION: Dual-function repressor/activator of the chbBCARFG operon. In the absence of the inducing sugar chitobiose, together with NagC, represses the chbBCARFG operon for the uptake and metabolism of chitobiose. In association with Crp, and probably in the presence of chitobiose 6-phosphate, induces the transcription of the chbBCARFG operon. {ECO:0000269|PubMed:18028317}.

## Outgoing Edges (13)

- `activates` --> [[gene.b1733|gene.b1733]] `RegulonDB` `S` - regulator=ChbR; target=chbG; function=-+
- `activates` --> [[gene.b1734|gene.b1734]] `RegulonDB` `S` - regulator=ChbR; target=chbF; function=-+
- `activates` --> [[gene.b1735|gene.b1735]] `RegulonDB` `S` - regulator=ChbR; target=chbR; function=-+
- `activates` --> [[gene.b1736|gene.b1736]] `RegulonDB` `S` - regulator=ChbR; target=chbA; function=-+
- `activates` --> [[gene.b1737|gene.b1737]] `RegulonDB` `S` - regulator=ChbR; target=chbC; function=-+
- `activates` --> [[gene.b1738|gene.b1738]] `RegulonDB` `S` - regulator=ChbR; target=chbB; function=-+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8595|complex.ecocyc.CPLX0-8595]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b1733|gene.b1733]] `RegulonDB` `S` - regulator=ChbR; target=chbG; function=-+
- `represses` --> [[gene.b1734|gene.b1734]] `RegulonDB` `S` - regulator=ChbR; target=chbF; function=-+
- `represses` --> [[gene.b1735|gene.b1735]] `RegulonDB` `S` - regulator=ChbR; target=chbR; function=-+
- `represses` --> [[gene.b1736|gene.b1736]] `RegulonDB` `S` - regulator=ChbR; target=chbA; function=-+
- `represses` --> [[gene.b1737|gene.b1737]] `RegulonDB` `S` - regulator=ChbR; target=chbC; function=-+
- `represses` --> [[gene.b1738|gene.b1738]] `RegulonDB` `S` - regulator=ChbR; target=chbB; function=-+

## Incoming Edges (1)

- `encodes` <-- [[gene.b1735|gene.b1735]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17410`
- `KEGG:ecj:JW1724;eco:b1735;`
- `GeneID:946247;`
- `GO:GO:0000976; GO:0001046; GO:0003700; GO:0006355; GO:0042803; GO:0045892`

## Notes

HTH-type transcriptional regulator ChbR (Chb operon repressor)
