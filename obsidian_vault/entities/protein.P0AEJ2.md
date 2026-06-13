---
entity_id: "protein.P0AEJ2"
entity_type: "protein"
name: "entC"
source_database: "UniProt"
source_id: "P0AEJ2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "entC b0593 JW0585"
---

# entC

`protein.P0AEJ2`

## Static

- Type: `protein`
- Source: `UniProt:P0AEJ2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine). Catalyzes the reversible conversion of chorismate to isochorismate. {ECO:0000269|PubMed:17243787, ECO:0000269|PubMed:20079748, ECO:0000269|PubMed:2139795, ECO:0000269|PubMed:2536681, ECO:0000269|PubMed:8655506, ECO:0000269|PubMed:9795253}. There are two isochorismate synthase enzymes present in E. coli, encoded by entC and menF. EntC is specific to the enterobactin biosynthetic pathway, while MenF is specific to the menaquinone biosynthetic pathway . Macromolecular crowding appears to increase the intrinsic activity of the enzyme by inducing structural changes . The crystal structure of EntC in complex with isochorismate and Mg2+ has been determined at 2.3 Å resolution. Also in this report, activity analysis of the wild-type enzyme and EntC mutants produced by site-directed mutagenesis provided insights into the catalytic mechanism . EntB has been shown to form a specific, intracellular pairwise interaction with EntC, and computational analysis indicates the EntB-EntC complex may provide a substrate channeling surface . Expression of entC is induced by low iron concentration both aerobically and anaerobically...

## Biological Role

Catalyzes ISOCHORSYN-RXN (reaction.ecocyc.ISOCHORSYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of the siderophore enterobactin (macrocyclic trimeric lactone of N-(2,3-dihydroxybenzoyl)-serine). Catalyzes the reversible conversion of chorismate to isochorismate. {ECO:0000269|PubMed:17243787, ECO:0000269|PubMed:20079748, ECO:0000269|PubMed:2139795, ECO:0000269|PubMed:2536681, ECO:0000269|PubMed:8655506, ECO:0000269|PubMed:9795253}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01053` Biosynthesis of siderophore group nonribosomal peptides (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ISOCHORSYN-RXN|reaction.ecocyc.ISOCHORSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0593|gene.b0593]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEJ2`
- `KEGG:ecj:JW0585;eco:b0593;ecoc:C3026_02960;`
- `GeneID:945511;`
- `GO:GO:0000287; GO:0008909; GO:0009239`
- `EC:5.4.4.2`

## Notes

Isochorismate synthase EntC (EC 5.4.4.2) (Isochorismate mutase)
