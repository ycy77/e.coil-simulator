---
entity_id: "protein.P0ACQ0"
entity_type: "protein"
name: "rbsR"
source_database: "UniProt"
source_id: "P0ACQ0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rbsR b3753 JW3732"
---

# rbsR

`protein.P0ACQ0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACQ0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional repressor for the ribose rbsDACBK operon. RbsR binds to a region of perfect dyad symmetry spanning the rbs operon transcriptional start site. The affinity for the rbs operator is reduced by addition of ribose, consistent with ribose being the inducer of the operon. The transcription factor RbsR, for "Ribose Repressor," is negatively autoregulated and controls the transcription of the operon involved in ribose catabolism and transport . Transcription of this operon is induced when E. coli is grown in the absence of glucose and when the physiological inducer D-ribose binds to the RbsR repressor . When D-ribose binds to RbsR, the protein becomes inactive because the binding affinity of RbsR decreases . RbsR represses not only the rbs operon for transport and utilization of D-ribose but also the de novo synthesis of purine nucleotides from D-ribose 5-phosphate. In the presence of the inducer D-ribose, RbsR activates the salvage pathway of purine nucleotide synthesis . Although little is known about the mechanism of regulation of the RbsR transcription factor, Mauzy et al. in 1992 demonstrated that this regulator acts as a repressor by binding to cis-acting elements, which have a conserved inverted repeat sequence and overlap the rbsD promoter...

## Biological Role

Component of RbsR-D-ribose (complex.ecocyc.MONOMER-60).

## Annotation

FUNCTION: Transcriptional repressor for the ribose rbsDACBK operon. RbsR binds to a region of perfect dyad symmetry spanning the rbs operon transcriptional start site. The affinity for the rbs operator is reduced by addition of ribose, consistent with ribose being the inducer of the operon.

## Outgoing Edges (13)

- `activates` --> [[gene.b1623|gene.b1623]] `RegulonDB` `C` - regulator=RbsR; target=add; function=+
- `activates` --> [[gene.b2065|gene.b2065]] `RegulonDB` `S` - regulator=RbsR; target=dcd; function=+
- `activates` --> [[gene.b2066|gene.b2066]] `RegulonDB` `S` - regulator=RbsR; target=udk; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER-60|complex.ecocyc.MONOMER-60]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3748|gene.b3748]] `RegulonDB` `C` - regulator=RbsR; target=rbsD; function=-
- `represses` --> [[gene.b3749|gene.b3749]] `RegulonDB` `C` - regulator=RbsR; target=rbsA; function=-
- `represses` --> [[gene.b3750|gene.b3750]] `RegulonDB` `C` - regulator=RbsR; target=rbsC; function=-
- `represses` --> [[gene.b3751|gene.b3751]] `RegulonDB` `C` - regulator=RbsR; target=rbsB; function=-
- `represses` --> [[gene.b3752|gene.b3752]] `RegulonDB` `C` - regulator=RbsR; target=rbsK; function=-
- `represses` --> [[gene.b3753|gene.b3753]] `RegulonDB` `C` - regulator=RbsR; target=rbsR; function=-
- `represses` --> [[gene.b4005|gene.b4005]] `RegulonDB` `C` - regulator=RbsR; target=purD; function=-
- `represses` --> [[gene.b4006|gene.b4006]] `RegulonDB` `C` - regulator=RbsR; target=purH; function=-
- `represses` --> [[gene.b4804|gene.b4804]] `RegulonDB` `C` - regulator=RbsR; target=rbsZ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3753|gene.b3753]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACQ0`
- `KEGG:ecj:JW3732;eco:b3753;`
- `GeneID:75173987;948266;`
- `GO:GO:0000976; GO:0000987; GO:0001216; GO:0003700; GO:0006355; GO:0045893; GO:0048029`

## Notes

Ribose operon repressor
