---
entity_id: "protein.P11446"
entity_type: "protein"
name: "argC"
source_database: "UniProt"
source_id: "P11446"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00150}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "argC b3958 JW3930"
---

# argC

`protein.P11446`

## Static

- Type: `protein`
- Source: `UniProt:P11446`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00150}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of N-acetyl-5-glutamyl phosphate to yield N-acetyl-L-glutamate 5-semialdehyde. {ECO:0000255|HAMAP-Rule:MF_00150, ECO:0000269|PubMed:13863980}. N-acetylglutamylphosphate reductase (ArgC) carries out the third step in arginine biosynthesis and its subpathway, ornithine biosynthesis. ArgC catalyzes the NADPH-dependent reduction of N-acetylglutamyl-phosphate to yield N-acetyl-L-glutamate 5-semialdehyde . Evolution and recruitment of promiscuous enzymes have been studied using ProA and its ability to replace ArgC .

## Biological Role

Catalyzes N-acetyl-L-glutamate-5-semialdehyde:NADP+ 5-oxidoreductase (phosphrylating) (reaction.R03443), N-ACETYLGLUTPREDUCT-RXN (reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of N-acetyl-5-glutamyl phosphate to yield N-acetyl-L-glutamate 5-semialdehyde. {ECO:0000255|HAMAP-Rule:MF_00150, ECO:0000269|PubMed:13863980}.

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01210` 2-Oxocarboxylic acid metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03443|reaction.R03443]] `KEGG` `database` - via EC:1.2.1.38
- `catalyzes` --> [[reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN|reaction.ecocyc.N-ACETYLGLUTPREDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3958|gene.b3958]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11446`
- `KEGG:ecj:JW3930;eco:b3958;ecoc:C3026_21390;`
- `GeneID:75169402;75203212;948455;`
- `GO:GO:0003942; GO:0005737; GO:0006526; GO:0051287; GO:0070401`
- `EC:1.2.1.38`

## Notes

N-acetyl-gamma-glutamyl-phosphate reductase (AGPR) (EC 1.2.1.38) (N-acetyl-glutamate semialdehyde dehydrogenase) (NAGSA dehydrogenase)
