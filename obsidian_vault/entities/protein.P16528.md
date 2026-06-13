---
entity_id: "protein.P16528"
entity_type: "protein"
name: "iclR"
source_database: "UniProt"
source_id: "P16528"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iclR b4018 JW3978"
---

# iclR

`protein.P16528`

## Static

- Type: `protein`
- Source: `UniProt:P16528`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Regulation of the glyoxylate bypass operon (aceBAK), which encodes isocitrate lyase, malate synthase as well as isocitrate dehydrogenase kinase/phosphorylase. Glyoxylate disrupts the interaction with the promoter by favoring the inactive dimeric form. Pyruvate enhances promoter binding by stabilizing the tetrameric form.

## Biological Role

Component of IclR-pyruvate DNA-binding transcriptional repressor (complex.ecocyc.CPLX0-7605), IclR-glyoxylate (complex.ecocyc.CPLX0-7606).

## Annotation

FUNCTION: Regulation of the glyoxylate bypass operon (aceBAK), which encodes isocitrate lyase, malate synthase as well as isocitrate dehydrogenase kinase/phosphorylase. Glyoxylate disrupts the interaction with the promoter by favoring the inactive dimeric form. Pyruvate enhances promoter binding by stabilizing the tetrameric form.

## Outgoing Edges (6)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7605|complex.ecocyc.CPLX0-7605]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7606|complex.ecocyc.CPLX0-7606]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b4014|gene.b4014]] `RegulonDB` `S` - regulator=IclR; target=aceB; function=-
- `represses` --> [[gene.b4015|gene.b4015]] `RegulonDB` `S` - regulator=IclR; target=aceA; function=-
- `represses` --> [[gene.b4016|gene.b4016]] `RegulonDB` `S` - regulator=IclR; target=aceK; function=-
- `represses` --> [[gene.b4018|gene.b4018]] `RegulonDB` `S` - regulator=IclR; target=iclR; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4018|gene.b4018]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P16528`
- `KEGG:ecj:JW3978;eco:b4018;ecoc:C3026_21705;`
- `GeneID:93777877;948524;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0006097; GO:0006355; GO:0045892`

## Notes

Transcriptional repressor IclR (Acetate operon repressor)
