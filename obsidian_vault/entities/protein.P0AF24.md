---
entity_id: "protein.P0AF24"
entity_type: "protein"
name: "nagD"
source_database: "UniProt"
source_id: "P0AF24"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nagD b0675 JW0661"
---

# nagD

`protein.P0AF24`

## Static

- Type: `protein`
- Source: `UniProt:P0AF24`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of an unusually broad range of substrate including deoxyribo- and ribonucleoside tri-, di-, and monophosphates, as well as polyphosphate and glucose-1-P (Glu1P). {ECO:0000269|PubMed:16430214, ECO:0000269|PubMed:16990279}. UmpH is a ribonucleoside tri-, di-, and monophosphatase with a preference for purines . The enzyme was found to degrade "overflow" UMP nucleotides and is required for optimal growth in response to environmental pyrimidine intermediates . UMP accumulation to levels above the Km of the enzyme, triggered by environmental conditions or artificially induced by mutations in the normal feedback regulation of the pyrimidine biosynthesis pathway, appear to cause the overflow degradation of UMP by UmpH . Though UmpH is a member of the nag N-acetylglucosamine utilization operon, it is a fairly general ribonucleotide monophosphatase . A type IIA member of the HAD protein superfamily, UmpH shows peak activity with UMP, but is also a very effective phosphatase with AMP, GMP and CMP . The structure of UmpH has been solved to 1.8 Å resolution . A umpH null mutant shows somewhat impaired growth upon addition of orotate, an intermediate in the PWY0-162 "pyrimidine biosynthesis pathway", to the growth medium. However, growth recovers, and the final culture density is higher than for wild type cells...

## Biological Role

Catalyzes adenosine 5'-monophosphate phosphohydrolase (reaction.R00183), cytidine-5'-monophosphate phosphohydrolase (reaction.R00511), 5-NUCLEOTID-RXN (reaction.ecocyc.5-NUCLEOTID-RXN).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of an unusually broad range of substrate including deoxyribo- and ribonucleoside tri-, di-, and monophosphates, as well as polyphosphate and glucose-1-P (Glu1P). {ECO:0000269|PubMed:16430214, ECO:0000269|PubMed:16990279}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00183|reaction.R00183]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.R00511|reaction.R00511]] `KEGG` `database` - via EC:3.1.3.5
- `catalyzes` --> [[reaction.ecocyc.5-NUCLEOTID-RXN|reaction.ecocyc.5-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0675|gene.b0675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF24`
- `KEGG:ecj:JW0661;eco:b0675;`
- `GeneID:86863182;93776810;945283;`
- `GO:GO:0000287; GO:0005737; GO:0005829; GO:0008253; GO:0016791; GO:0046050`
- `EC:3.1.3.5`

## Notes

Ribonucleotide monophosphatase NagD (EC 3.1.3.5)
