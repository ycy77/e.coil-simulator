---
entity_id: "protein.P24242"
entity_type: "protein"
name: "ascG"
source_database: "UniProt"
source_id: "P24242"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ascG b2714 JW5434"
---

# ascG

`protein.P24242`

## Static

- Type: `protein`
- Source: `UniProt:P24242`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the asc operon. The cryptic operon is activated by the insertion of IS186 into the ascG gene. The AscG, "Arbutin-salicin-cellibiose," transcriptional regulator represses the expression of a cryptic operon (ascFB) whose genes are involved in transport and utilization of the β-glucoside sugars arbutin, salicin, and cellibiose. This operon is activated only when the repressor is inactivated through the interruption of the gene by an insertion sequence . AscG also regulates prpBC for propionate catabolism . Consistent with a broader in vivo model for many transcription factors (including AscG), regulation is compatible with primary stabilization of RNAP at promoters, with fold-changes scaling approximately as the reciprocal of promoter basal activity and buffering promoter-to-promoter variability across contexts and perturbations . AscG is a GalR-type transcription factor and has a helix-turn-helix motif . AscG recognizes and binds the consensus palindromic sequence TGAAACCGGTTTCA . A high level of AscG is always present in wild-type Escherichia coli cells . A positive correlation between cellular growth and the copy number of the protein AscG has been reported . The ascG gene is transcribed divergently from the operon it regulates . ascG is paralogous to galR...

## Annotation

FUNCTION: Repressor of the asc operon. The cryptic operon is activated by the insertion of IS186 into the ascG gene.

## Outgoing Edges (5)

- `represses` --> [[gene.b0330|gene.b0330]] `RegulonDB` `C` - regulator=AscG; target=prpR; function=-
- `represses` --> [[gene.b0473|gene.b0473]] `RegulonDB` `S` - regulator=AscG; target=htpG; function=-
- `represses` --> [[gene.b0820|gene.b0820]] `RegulonDB` `S` - regulator=AscG; target=ybiT; function=-
- `represses` --> [[gene.b2715|gene.b2715]] `RegulonDB` `C` - regulator=AscG; target=ascF; function=-
- `represses` --> [[gene.b2716|gene.b2716]] `RegulonDB` `C` - regulator=AscG; target=ascB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2714|gene.b2714]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24242`
- `KEGG:ecj:JW5434;eco:b2714;ecoc:C3026_14935;`
- `GeneID:947305;`
- `GO:GO:0000976; GO:0003700; GO:0006351; GO:0006355; GO:0043565; GO:0045892`

## Notes

HTH-type transcriptional regulator AscG (Cryptic asc operon repressor)
