---
entity_id: "protein.P15877"
entity_type: "protein"
name: "gcd"
source_database: "UniProt"
source_id: "P15877"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Periplasmic side {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcd b0124 JW0120"
---

# gcd

`protein.P15877`

## Static

- Type: `protein`
- Source: `UniProt:P15877`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}; Periplasmic side {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: GDH is probably involved in energy conservation rather than in sugar metabolism. {ECO:0000305|PubMed:8509415}. Glucose dehydrogenase (Gcd) is a membrane-bound enzyme. Its role in glucose utilization is not fully clear, because under ordinary conditions it exists as an apoprotein. The enzyme requires the cofactor pyrroloquinoline quinone (PQQ) for activity, yet E. coli lacks the ability to synthesize PQQ . However, E. coli exhibits chemotaxis towards environmental PQQ , and may thus use an externally supplied cofactor. PQQ is transported across the outer membrane by the TonB-dependent transporter G6762-MONOMER PqqU . Once functional, the enzyme is able to oxidize glucose and feed electrons into the respiratory chain , but does not generate a proton motive force . The topological structure of Gcd within the membrane has been investigated and revealed five N-terminal membrane-spanning segments, with the N-terminus located in the cytoplasm and the C-terminus is located in the periplasm . The C-terminal periplasmic domain binds PQQ, contains the catalytic activity and is able to interact with ubiquinone in the cytoplasmic membrane . A ubiquinone-interacting site is located close to the membrane surface . Further experiments showed that Gcd contains two ubiquinone binding sites...

## Biological Role

Catalyzes RXN0-6373 (reaction.ecocyc.RXN0-6373). Bound by Magnesium cation (molecule.C00305), pyrroloquinoline quinone (molecule.ecocyc.PQQ), ubiquinone-8 (molecule.ecocyc.UBIQUINONE-8).

## Enriched Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: GDH is probably involved in energy conservation rather than in sugar metabolism. {ECO:0000305|PubMed:8509415}.

## Pathways

- `eco00030` Pentose phosphate pathway (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6373|reaction.ecocyc.RXN0-6373]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.PQQ|molecule.ecocyc.PQQ]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.UBIQUINONE-8|molecule.ecocyc.UBIQUINONE-8]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0124|gene.b0124]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P15877`
- `KEGG:ecj:JW0120;eco:b0124;ecoc:C3026_00525;`
- `GeneID:944830;`
- `GO:GO:0000287; GO:0005886; GO:0008876; GO:0016020; GO:0019595; GO:0030288; GO:0048039; GO:0070968`
- `EC:1.1.5.2`

## Notes

Quinoprotein glucose dehydrogenase (EC 1.1.5.2) (Glucose dehydrogenase [pyrroloquinoline-quinone])
