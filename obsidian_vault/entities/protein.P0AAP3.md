---
entity_id: "protein.P0AAP3"
entity_type: "protein"
name: "frmR"
source_database: "UniProt"
source_id: "P0AAP3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frmR yaiN b0357 JW0348"
---

# frmR

`protein.P0AAP3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAP3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Formaldehyde sensor (PubMed:27934966). In the absence of formaldehyde, mediates repression of the frmRAB operon (PubMed:15466022, PubMed:27934966). Acts by binding directly to the frmRAB promoter region (PubMed:27934966). In the presence of formaldehyde, it dissociates from the frmRAB promoter region and allows expression of the formaldehyde detoxification system encoded by frmA and frmB (PubMed:27934966). It senses the toxic chemical formaldehyde directly, with no metal-dependence (PubMed:27934966). {ECO:0000269|PubMed:15466022, ECO:0000269|PubMed:27934966}.

## Biological Role

Component of DNA-binding transcriptional repressor FrmR (complex.ecocyc.CPLX0-8234).

## Annotation

FUNCTION: Formaldehyde sensor (PubMed:27934966). In the absence of formaldehyde, mediates repression of the frmRAB operon (PubMed:15466022, PubMed:27934966). Acts by binding directly to the frmRAB promoter region (PubMed:27934966). In the presence of formaldehyde, it dissociates from the frmRAB promoter region and allows expression of the formaldehyde detoxification system encoded by frmA and frmB (PubMed:27934966). It senses the toxic chemical formaldehyde directly, with no metal-dependence (PubMed:27934966). {ECO:0000269|PubMed:15466022, ECO:0000269|PubMed:27934966}.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8234|complex.ecocyc.CPLX0-8234]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b0355|gene.b0355]] `RegulonDB` `S` - regulator=FrmR; target=frmB; function=-
- `represses` --> [[gene.b0356|gene.b0356]] `RegulonDB` `S` - regulator=FrmR; target=frmA; function=-
- `represses` --> [[gene.b0357|gene.b0357]] `RegulonDB` `S` - regulator=FrmR; target=frmR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0357|gene.b0357]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAP3`
- `KEGG:ecj:JW0348;eco:b0357;ecoc:C3026_01760;`
- `GeneID:86862911;93777098;944986;`
- `GO:GO:0000976; GO:0001217; GO:0005737; GO:0032993; GO:0045892; GO:0046872`

## Notes

Transcriptional repressor FrmR
