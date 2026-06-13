---
entity_id: "protein.P0ACL5"
entity_type: "protein"
name: "glcC"
source_database: "UniProt"
source_id: "P0ACL5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glcC yghN b2980 JW2947"
---

# glcC

`protein.P0ACL5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACL5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional activator of the glcDEFGB operon which is associated with glycolate utilization, and encodes malate synthase G and the genes needed for glycolate oxidase activity (PubMed:8606183, PubMed:9880556). Also negatively regulates the transcription of its own gene (PubMed:9880556). Glycolate acts as an effector, but GlcC can also use acetate as an alternative effector (PubMed:9880556). {ECO:0000269|PubMed:8606183, ECO:0000269|PubMed:9880556}. GlcC (for "glycolate utilization") negatively controls the expression of genes involved in the utilization of glycolate as the sole source of carbon . It is negatively autoregulated and coordinately activated by transcription of the divergent operon glc, which is related to the transport and metabolism of glycolate . Synthesis of glc genes is induced when Escherichia coli is grown on glycolate . GlcC features an N-terminal domain containing a helix-turn-helix motif and a putative C-terminal domain that includes the key residues involved in coinducer recognition and oligomerization. Although little is known about the mechanism of regulation of the GlcC transcription factor, Pellicer et al. demonstrated that it is a regulator that acts as a repressor by binding to cis-acting elements, inverted repeat sequences that are not well-conserved, that overlap the ATG sequence...

## Biological Role

Component of GlcC-glycolate DNA-binding transcriptional dual regulator (complex.ecocyc.MONOMER0-562).

## Annotation

FUNCTION: Transcriptional activator of the glcDEFGB operon which is associated with glycolate utilization, and encodes malate synthase G and the genes needed for glycolate oxidase activity (PubMed:8606183, PubMed:9880556). Also negatively regulates the transcription of its own gene (PubMed:9880556). Glycolate acts as an effector, but GlcC can also use acetate as an alternative effector (PubMed:9880556). {ECO:0000269|PubMed:8606183, ECO:0000269|PubMed:9880556}.

## Outgoing Edges (8)

- `activates` --> [[gene.b2975|gene.b2975]] `RegulonDB` `S` - regulator=GlcC; target=glcA; function=+
- `activates` --> [[gene.b2976|gene.b2976]] `RegulonDB` `S` - regulator=GlcC; target=glcB; function=+
- `activates` --> [[gene.b2977|gene.b2977]] `RegulonDB` `S` - regulator=GlcC; target=glcG; function=+
- `activates` --> [[gene.b2979|gene.b2979]] `RegulonDB` `S` - regulator=GlcC; target=glcD; function=+
- `activates` --> [[gene.b4467|gene.b4467]] `RegulonDB` `S` - regulator=GlcC; target=glcF; function=+
- `activates` --> [[gene.b4468|gene.b4468]] `RegulonDB` `S` - regulator=GlcC; target=glcE; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-562|complex.ecocyc.MONOMER0-562]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2980|gene.b2980]] `RegulonDB` `S` - regulator=GlcC; target=glcC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b2980|gene.b2980]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACL5`
- `KEGG:ecj:JW2947;eco:b2980;ecoc:C3026_16305;`
- `GeneID:75205188;947466;`
- `GO:GO:0000987; GO:0003677; GO:0003700; GO:0006355`

## Notes

Glc operon transcriptional activator (Glc regulatory protein) (HTH-type transcriptional regulator GlcC)
