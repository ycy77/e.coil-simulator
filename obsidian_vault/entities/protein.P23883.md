---
entity_id: "protein.P23883"
entity_type: "protein"
name: "puuC"
source_database: "UniProt"
source_id: "P23883"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuC aldH b1300 JW1293"
---

# puuC

`protein.P23883`

## Static

- Type: `protein`
- Source: `UniProt:P23883`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of 3-hydroxypropionaldehyde (3-HPA) to 3-hydroxypropionic acid (3-HP) (PubMed:18668238). It acts preferentially with NAD but can also use NADP (PubMed:18668238). 3-HPA appears to be the most suitable substrate for PuuC followed by isovaleraldehyde, propionaldehyde, butyraldehyde, and valeraldehyde (PubMed:18668238). It might play a role in propionate and/or acetic acid metabolisms (PubMed:18668238). Also involved in the breakdown of putrescine through the oxidation of gamma-Glu-gamma-aminobutyraldehyde to gamma-Glu-gamma-aminobutyrate (gamma-Glu-GABA) (PubMed:15590624). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18668238, ECO:0000305|PubMed:1840553}. The puuC gene was first reported as a gene encoding a putative aldehyde dehydrogenase of unknown function. The product of the gene shares 40% identity and over 60% similarity, with both the cytosolic and the mitochondrial forms of mammalian aldehyde dehydrogenases . It was later inferred to be the γ-glutamyl-γ-aminobutyraldehyde dehydrogenase in a putrescine utilization pathway; together with PuuB, γ-glutamyl-γ-aminobutyrate is produced from γ-glutamylputrescine . The purified enzyme was shown to have somewhat promiscuous aldehyde dehydrogenase activity, acting on several aldehydes including HYDROXYPROPANAL; γ-glutamyl-γ-aminobutyraldehyde was not tested as a substrate in that study...

## Biological Role

Catalyzes AMINOBUTDEHYDROG-RXN (reaction.ecocyc.AMINOBUTDEHYDROG-RXN), RXN-10715 (reaction.ecocyc.RXN-10715), RXN0-3922 (reaction.ecocyc.RXN0-3922), RXN0-5455 (reaction.ecocyc.RXN0-5455), SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN (reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of 3-hydroxypropionaldehyde (3-HPA) to 3-hydroxypropionic acid (3-HP) (PubMed:18668238). It acts preferentially with NAD but can also use NADP (PubMed:18668238). 3-HPA appears to be the most suitable substrate for PuuC followed by isovaleraldehyde, propionaldehyde, butyraldehyde, and valeraldehyde (PubMed:18668238). It might play a role in propionate and/or acetic acid metabolisms (PubMed:18668238). Also involved in the breakdown of putrescine through the oxidation of gamma-Glu-gamma-aminobutyraldehyde to gamma-Glu-gamma-aminobutyrate (gamma-Glu-GABA) (PubMed:15590624). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:18668238, ECO:0000305|PubMed:1840553}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.AMINOBUTDEHYDROG-RXN|reaction.ecocyc.AMINOBUTDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-10715|reaction.ecocyc.RXN-10715]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-3922|reaction.ecocyc.RXN0-3922]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5455|reaction.ecocyc.RXN0-5455]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN|reaction.ecocyc.SUCCINATE-SEMIALDEHYDE-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1300|gene.b1300]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23883`
- `KEGG:ecj:JW1293;eco:b1300;ecoc:C3026_07630;`
- `GeneID:947003;`
- `GO:GO:0004029; GO:0004030; GO:0009447; GO:0033721`
- `EC:1.2.1.5`

## Notes

NADP/NAD-dependent aldehyde dehydrogenase PuuC (ALDH) (EC 1.2.1.5) (3-hydroxypropionaldehyde dehydrogenase) (Gamma-glutamyl-gamma-aminobutyraldehyde dehydrogenase) (Gamma-Glu-gamma-aminobutyraldehyde dehydrogenase)
