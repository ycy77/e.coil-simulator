---
entity_id: "protein.P0AF20"
entity_type: "protein"
name: "nagC"
source_database: "UniProt"
source_id: "P0AF20"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagC nagR b0676 JW0662"
---

# nagC

`protein.P0AF20`

## Static

- Type: `protein`
- Source: `UniProt:P0AF20`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Acts as a repressor of the nagEBACD operon and acts both as an activator and a repressor for the transcription of the glmSU operon (PubMed:7545108). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:7545108}. The NagC, "N-acetylglucosamine," transcriptional dual regulator participates in regulating the phosphotransferase system (PTS) . Its function is to coordinate the biosynthesis of the amino sugars, D-glucosamine (GlcN) and N-acetylglucosamine (GlcNAc) with their catabolism . The specific inducer for NagC is GlcNAc-6-P, the product of GlcNAc transport by the PTS . NagC is displaced from its DNA targets by interacting with GlcNAc-6-P . Mutation in the first two amino acids of the recognition helix of the DNA-binding motif causes GlcNAc6P to act with NagC as a corepressor instead of as an inducer . Proline at the first position of this helix seems to contribute to the distinction between the NagC binding sites and suboptimal sites . Based on the structure of PD01896, models for the three-dimensional structure of NagC and for the binding of GlcNAc-6-P were developed . This protein has a helix-turn-helix motif in its N-terminal part . The Nag regulon consists of two divergent operons, nagE and nagBACD...

## Biological Role

Component of NagC-N-acetyl-D-glucosamine 6-phosphate (complex.ecocyc.MONOMER0-2261).

## Annotation

FUNCTION: Acts as a repressor of the nagEBACD operon and acts both as an activator and a repressor for the transcription of the glmSU operon (PubMed:7545108). Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair (PubMed:36326440). {ECO:0000269|PubMed:7545108}.

## Outgoing Edges (26)

- `activates` --> [[gene.b3729|gene.b3729]] `RegulonDB` `C` - regulator=NagC; target=glmS; function=-+
- `activates` --> [[gene.b3730|gene.b3730]] `RegulonDB` `C` - regulator=NagC; target=glmU; function=-+
- `activates` --> [[gene.b4312|gene.b4312]] `RegulonDB` `C` - regulator=NagC; target=fimB; function=+
- `is_component_of` --> [[complex.ecocyc.MONOMER0-2261|complex.ecocyc.MONOMER0-2261]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0675|gene.b0675]] `RegulonDB` `C` - regulator=NagC; target=umpH; function=-
- `represses` --> [[gene.b0676|gene.b0676]] `RegulonDB` `C` - regulator=NagC; target=nagC; function=-
- `represses` --> [[gene.b0677|gene.b0677]] `RegulonDB` `C` - regulator=NagC; target=nagA; function=-
- `represses` --> [[gene.b0678|gene.b0678]] `RegulonDB` `C` - regulator=NagC; target=nagB; function=-
- `represses` --> [[gene.b0679|gene.b0679]] `RegulonDB` `C` - regulator=NagC; target=nagE; function=-
- `represses` --> [[gene.b0681|gene.b0681]] `RegulonDB` `S` - regulator=NagC; target=chiP; function=-
- `represses` --> [[gene.b0682|gene.b0682]] `RegulonDB` `S` - regulator=NagC; target=chiQ; function=-
- `represses` --> [[gene.b1733|gene.b1733]] `RegulonDB` `C` - regulator=NagC; target=chbG; function=-
- `represses` --> [[gene.b1734|gene.b1734]] `RegulonDB` `C` - regulator=NagC; target=chbF; function=-
- `represses` --> [[gene.b1735|gene.b1735]] `RegulonDB` `S` - regulator=NagC; target=chbR; function=-
- `represses` --> [[gene.b1736|gene.b1736]] `RegulonDB` `S` - regulator=NagC; target=chbA; function=-
- `represses` --> [[gene.b1737|gene.b1737]] `RegulonDB` `C` - regulator=NagC; target=chbC; function=-
- `represses` --> [[gene.b1738|gene.b1738]] `RegulonDB` `S` - regulator=NagC; target=chbB; function=-
- `represses` --> [[gene.b1817|gene.b1817]] `RegulonDB` `S` - regulator=NagC; target=manX; function=-
- `represses` --> [[gene.b1819|gene.b1819]] `RegulonDB` `S` - regulator=NagC; target=manZ; function=-
- `represses` --> [[gene.b2943|gene.b2943]] `RegulonDB` `C` - regulator=NagC; target=galP; function=-
- `represses` --> [[gene.b3729|gene.b3729]] `RegulonDB` `C` - regulator=NagC; target=glmS; function=-+
- `represses` --> [[gene.b3730|gene.b3730]] `RegulonDB` `C` - regulator=NagC; target=glmU; function=-+
- `represses` --> [[gene.b4309|gene.b4309]] `RegulonDB` `C` - regulator=NagC; target=nanS; function=-
- `represses` --> [[gene.b4310|gene.b4310]] `RegulonDB` `C` - regulator=NagC; target=nanM; function=-
- `represses` --> [[gene.b4311|gene.b4311]] `RegulonDB` `C` - regulator=NagC; target=nanC; function=-
- `represses` --> [[gene.b4808|gene.b4808]] `RegulonDB` `S` - regulator=NagC; target=chiZ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0676|gene.b0676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF20`
- `KEGG:ecj:JW0662;eco:b0676;ecoc:C3026_03360;`
- `GeneID:93776809;945285;`
- `GO:GO:0003677; GO:0003700; GO:0006355`

## Notes

DNA-binding transcriptional dual regulator NagC (N-acetylglucosamine repressor) (NagC repressor)
