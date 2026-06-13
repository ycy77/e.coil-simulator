---
entity_id: "protein.P0CB39"
entity_type: "protein"
name: "eptC"
source_database: "UniProt"
source_id: "P0CB39"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eptC cptA yijP b3955 JW3927"
---

# eptC

`protein.P0CB39`

## Static

- Type: `protein`
- Source: `UniProt:P0CB39`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the outer membrane lipopolysaccharide core. {ECO:0000250}. EptC is required for the incorporation of phosphoethanolamine (P-EtN) onto the phosphorylated heptose I residue of E. coli K-12 lipopolysaccharide (LPS) . P-EtN modifications are absent on the LPS of E. coli grown under phosphate-rich conditions but are enriched in the LPS from growth under phosphate-limiting conditions . eptC deleted strains have severe growth defects in the presence of SDS (0.25% - 1%) and are more sensitive to Zn2+ than the wild-type . Transcription of an eptC-lacZ fusion is reduced 4-5 fold in a phoR deletion mutant and reduced 2-fold in a basR deletion mutant. Two putative PhoB binding sites are located in the promoter region of eptC . LPS from an E. coli strain lacking all three ept genes (eptA, eptB and eptC) does not contain any P-EtN modifications . EptC (formerly YijP) has similarity to YijP of Ecoli . K1, which is required for that strain to invade brain microvascular endothelial cells and thereby cross the blood-brain barrier . Reviews discuss the role of YijP in meningitis caused by pathogenic E. coli . EptC was identified as a component of a complex in the inner membrane together with an unidentified 36 kDa protein .

## Biological Role

Catalyzes RXN-14363 (reaction.ecocyc.RXN-14363).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the addition of a phosphoethanolamine moiety to the outer membrane lipopolysaccharide core. {ECO:0000250}.

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-14363|reaction.ecocyc.RXN-14363]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3955|gene.b3955]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CB39`
- `KEGG:ecj:JW3927;eco:b3955;ecoc:C3026_21370;`
- `GeneID:948458;`
- `GO:GO:0005886; GO:0009244; GO:0016776`
- `EC:2.7.-.-`

## Notes

Phosphoethanolamine transferase EptC (EC 2.7.-.-)
