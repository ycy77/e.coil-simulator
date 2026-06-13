---
entity_id: "protein.P0A8Y8"
entity_type: "protein"
name: "entH"
source_database: "UniProt"
source_id: "P0A8Y8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00907, ECO:0000269|PubMed:17675380}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entH ybdB b0597 JW0589"
---

# entH

`protein.P0A8Y8`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Y8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00907, ECO:0000269|PubMed:17675380}.

## Enriched Summary

FUNCTION: Required for optimal enterobactin synthesis. Acts as a proofreading enzyme that prevents EntB misacylation by hydrolyzing the thioester bound existing between EntB and wrongly charged molecules. Displays esterase activity toward a wide range of substrates, including acyl-CoAs and aryl-CoAs. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:17675380, ECO:0000269|PubMed:19119850, ECO:0000269|PubMed:19193103, ECO:0000269|PubMed:24992697}. EntH is a thioesterase that is involved in the biosynthesis of enterobactin . It acts as a proofreading enzyme that hydrolyzes misacylated EntB aryl intermediates . reports that the catalytic activity of EntH is sensitive to the pattern of hydroxyl groups on the aryl-CoA substrates , while saw no such effect. Although EntH can utilize both CoA and holo-EntB as the substrate thioester, holo-ACP is a very poor substrate . While EntH is not required for enterobactin synthesis in vitro , it is required for optimal synthesis in vivo . EntH interacts with phosphopantetheine-modified ENTB-CPLX EntB in vivo . Esterase activity of EntH was first discovered in a high-throughput screen of purified proteins . Benzoyl-CoA was found to be a good substrate, with a Km of 82 µM . Crystal structures of EntH have been determined . The quarternary structure is best described as a dimer of dimers...

## Biological Role

Component of proofreading thioesterase in enterobactin biosynthesis (complex.ecocyc.CPLX0-7766).

## Enriched Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Annotation

FUNCTION: Required for optimal enterobactin synthesis. Acts as a proofreading enzyme that prevents EntB misacylation by hydrolyzing the thioester bound existing between EntB and wrongly charged molecules. Displays esterase activity toward a wide range of substrates, including acyl-CoAs and aryl-CoAs. {ECO:0000269|PubMed:15808744, ECO:0000269|PubMed:17675380, ECO:0000269|PubMed:19119850, ECO:0000269|PubMed:19193103, ECO:0000269|PubMed:24992697}.

## Pathways

- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7766|complex.ecocyc.CPLX0-7766]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b0597|gene.b0597]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Y8`
- `KEGG:ecj:JW0589;eco:b0597;ecoc:C3026_02980;`
- `GeneID:86863118;945215;`
- `GO:GO:0005829; GO:0009239; GO:0016289; GO:0016788; GO:0016790; GO:0042802; GO:0061522`
- `EC:3.1.2.-`

## Notes

Proofreading thioesterase EntH (EC 3.1.2.-) (Enterobactin synthase component H) (p15)
