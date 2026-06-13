---
entity_id: "protein.P06846"
entity_type: "protein"
name: "ebgR"
source_database: "UniProt"
source_id: "P06846"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ebgR b3075 JW3046"
---

# ebgR

`protein.P06846`

## Static

- Type: `protein`
- Source: `UniProt:P06846`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor for beta galactosidase alpha and beta subunits (ebgA and ebgC). Binds lactose as an inducer. EbgR (for "evolved β-galactosidase repressor") negatively regulates genes involved in the evolved β-galactosidase system, which constitutes an alternative for lactose utilization in cells with mutations on the lacZ gene . The wild-type Ebg enzyme, encoded by the ebg operon, is not efficient enough to permit growth on lactose. Mutations in ebgR and ebgA, however, enhance its catalytic activity and enable rapid growth on lactose as a sole carbon source . Inhibition of ebgR expression by CRISPRi reduced cellular fitness under treatment with the antibiotics polymyxin B or pyocyanin . EbgR belongs to the GalR-LacI family of transcriptional regulators. There is strong evidence that the ebg and lac operons share a common origin in evolution . EbgR diverged from other repressors shortly after the divergence of the Gram positive from the Gram negative eubacteria, approximately 2.2 billion years ago . The EbgR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data...

## Annotation

FUNCTION: Repressor for beta galactosidase alpha and beta subunits (ebgA and ebgC). Binds lactose as an inducer.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3075|gene.b3075]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06846`
- `KEGG:ecj:JW3046;eco:b3075;ecoc:C3026_16795;`
- `GeneID:947586;`
- `GO:GO:0000976; GO:0003700; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional regulator EbgR (Ebg operon repressor)
