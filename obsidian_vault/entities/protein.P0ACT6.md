---
entity_id: "protein.P0ACT6"
entity_type: "protein"
name: "uidR"
source_database: "UniProt"
source_id: "P0ACT6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uidR gusR b1618 JW1610"
---

# uidR

`protein.P0ACT6`

## Static

- Type: `protein`
- Source: `UniProt:P0ACT6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor for the uidRABC (gusRABC) operon. The "β-d-glucuronides repressor," UidR, is a transcriptional repressor. UidR negatively regulates its own synthesis and represses transcription of the uid operon, which is involved in transport and degradation of β-glucosides . This regulator is involved in the degradation of sugar acids and is subject to catabolic repression in the presence of glucose and at low levels of cyclic AMP. Although little is known about the regulating mechanism of UidR, it has been shown to act as a repressor, binding to a putative inverted repeat sequence in a cooperative process with UxuR . In 1986, Blanco et al. proposed that total repression of UidR is achieved in the presence of UxuR, suggesting the possibility that UidR and UxuR form a complex. Independently, each repressor binds to DNA separately . In the BL21 strain, UidR (GusR) can be inhibited by the presence of glucuronides, as they can bind to the protein GusR to release the DNA . The UidR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu .

## Annotation

FUNCTION: Repressor for the uidRABC (gusRABC) operon.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1618|gene.b1618]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACT6`
- `KEGG:ecj:JW1610;eco:b1618;ecoc:C3026_09305;`
- `GeneID:75171678;946150;`
- `GO:GO:0000976; GO:0003700; GO:0006351; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional regulator UidR (Gus operon repressor) (Uid operon repressor)
