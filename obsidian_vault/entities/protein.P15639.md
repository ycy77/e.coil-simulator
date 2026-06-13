---
entity_id: "protein.P15639"
entity_type: "protein"
name: "purH"
source_database: "UniProt"
source_id: "P15639"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purH b4006 JW3970"
---

# purH

`protein.P15639`

## Static

- Type: `protein`
- Source: `UniProt:P15639`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)] In bacteria and eukaryotes the last two reactions of the de novo purine biosynthetic pathway for IMP biosynthesis are sequentially catalyzed by a bifunctional enzyme containing aminoimidazole carboxamide ribonucleotide (AICAR) transformylase and IMP cyclohydrolase activities. To date, much of the biochemical and structural characterization has been done on the enzyme from organisms other than E. coli (see for example ). In E. coli early studies suggested an association between AICAR transformylase and IMP cyclohydrolase . Later studies concluded that AICAR transformylase and IMP cyclohydrolase form a bifunctional enzyme with both activities residing on a single polypeptide . Complementation studies suggested that the N-terminal domain contains the IMP cyclohydrolase activity and the C-terminal domain contains the AICAR transformylase activity . More recently recombinant, N-terminally His6-tagged enzyme from E. coli has been expressed, purified, crystallized, and subjected to preliminary X-ray diffraction analysis . The transformylation reaction is the second of two such reactions in the de novo biosynthesis of purine nucleotides...

## Biological Role

Catalyzes AICARTRANSFORM-RXN (reaction.ecocyc.AICARTRANSFORM-RXN), IMPCYCLOHYDROLASE-RXN (reaction.ecocyc.IMPCYCLOHYDROLASE-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)]

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.AICARTRANSFORM-RXN|reaction.ecocyc.AICARTRANSFORM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.IMPCYCLOHYDROLASE-RXN|reaction.ecocyc.IMPCYCLOHYDROLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4006|gene.b4006]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15639`
- `KEGG:ecj:JW3970;eco:b4006;ecoc:C3026_21635;`
- `GeneID:948503;`
- `GO:GO:0003937; GO:0004643; GO:0005829; GO:0006189`
- `EC:2.1.2.3; 3.5.4.10`

## Notes

Bifunctional purine biosynthesis protein PurH [Includes: Phosphoribosylaminoimidazolecarboxamide formyltransferase (EC 2.1.2.3) (AICAR transformylase); IMP cyclohydrolase (EC 3.5.4.10) (ATIC) (IMP synthase) (Inosinicase)]
