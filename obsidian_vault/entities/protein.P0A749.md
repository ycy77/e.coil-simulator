---
entity_id: "protein.P0A749"
entity_type: "protein"
name: "murA"
source_database: "UniProt"
source_id: "P0A749"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00111, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murA murZ b3189 JW3156"
---

# murA

`protein.P0A749`

## Static

- Type: `protein`
- Source: `UniProt:P0A749`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00111, ECO:0000305}.

## Enriched Summary

FUNCTION: Cell wall formation (PubMed:1512209). Adds enolpyruvyl to UDP-N-acetylglucosamine (PubMed:1512209, PubMed:20392080). Target for the antibiotic fosfomycin. {ECO:0000269|PubMed:1512209, ECO:0000269|PubMed:20392080}. UDP-N-acetylglucosamine enolpyruvoyl transferase (MurA) catalyzes the first committed step in the assembly of peptidoglycan . In exponentially growing cells, the intracellular concentration of UDP-N-acetylglucosamine is approximately 100 µM, while the concentration of the MurA product, UDP-N-acetylglucosamine enolpyruvate is only 2 µM . MurA activity is feedback-inhibited by UDP-MurNAc, the product of the second enzyme in the PWY-6387 pathway . The reaction mechanism of the enzyme has been investigated. A tetrahedral adduct can be formed at the active site of the enzyme during catalyis . However, covalent enzyme adduct formation is not required for catalysis . The stereochemical course of the reaction has been investigated . Catalysis involves conformational transitions within the enzyme . MurA is the site of action for the antibiotic fosfomycin. Inactivation of MurA is dependent on the presence of the substrate UDP-GlcNAc . The antibiotic covalently binds to the active site nucleophile Cys115 of the enzyme . A C115D mutant is active, but resistant to fosfomycin...

## Biological Role

Catalyzes phosphoenolpyruvate:UDP-N-acetyl-D-glucosamine 1-carboxyvinyl-transferase (reaction.R00660), UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN (reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Cell wall formation (PubMed:1512209). Adds enolpyruvyl to UDP-N-acetylglucosamine (PubMed:1512209, PubMed:20392080). Target for the antibiotic fosfomycin. {ECO:0000269|PubMed:1512209, ECO:0000269|PubMed:20392080}.

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00660|reaction.R00660]] `KEGG` `database` - via EC:2.5.1.7
- `catalyzes` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3189|gene.b3189]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A749`
- `KEGG:ecj:JW3156;eco:b3189;`
- `GeneID:93778792;947703;`
- `GO:GO:0005829; GO:0008360; GO:0008760; GO:0009252; GO:0019277; GO:0051301; GO:0071555`
- `EC:2.5.1.7`

## Notes

UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enolpyruvyl transferase) (EPT)
