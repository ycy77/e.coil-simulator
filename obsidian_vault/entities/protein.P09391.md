---
entity_id: "protein.P09391"
entity_type: "protein"
name: "glpG"
source_database: "UniProt"
source_id: "P09391"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16216077}; Multi-pass membrane protein {ECO:0000269|PubMed:16216077}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "glpG b3424 JW5687"
---

# glpG

`protein.P09391`

## Static

- Type: `protein`
- Source: `UniProt:P09391`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16216077}; Multi-pass membrane protein {ECO:0000269|PubMed:16216077}.

## Enriched Summary

FUNCTION: Rhomboid-type serine protease that catalyzes intramembrane proteolysis. {ECO:0000269|PubMed:16216077, ECO:0000269|PubMed:17099694}. GlpG is an intramembrane protease of the rhomboid family. Rhomboid proteases were first described in Drosophila and rhomboid-like genes are ubiquitous in prokaryotic genomes; rhomboid proteases are intramembrane, non-classical serine proteases which cleave membrane proteins; GlpG catalysis has been intensively studied and described but its physiological role is not well understood. GlpG cleaves the three Drosophila rhomboid substrates Spitz, Keren and Gurken in a mammalian cell transfection assay . Purified GlpG cleaves the model substrate, Drosophila Gurken-TMD; cleavage does not require ATP . GlpG cleaves an engineered, single spanning membrane protein of type I orientation (Nout-Cin) in vitro and in vivo; substrate features and recognition motifs that facilitate GlpG cleavage have been explored . GlpG cleaves truncated forms of a multispanning membrane protein (MdfA) in vivo and in vitro but intact MdfA is resistant to cleavage . GlpG displays low substrate affinity and slow catalysis when analysed in real-time within a membrane environment; GlpG catalysed proteolysis is not driven by substrate affinity but is a kinetically controlled reaction...

## Biological Role

Catalyzes 3.4.21.105-RXN (reaction.ecocyc.3.4.21.105-RXN).

## Annotation

FUNCTION: Rhomboid-type serine protease that catalyzes intramembrane proteolysis. {ECO:0000269|PubMed:16216077, ECO:0000269|PubMed:17099694}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.4.21.105-RXN|reaction.ecocyc.3.4.21.105-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3424|gene.b3424]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09391`
- `KEGG:ecj:JW5687;eco:b3424;ecoc:C3026_18565;`
- `GeneID:86862178;947936;`
- `GO:GO:0004175; GO:0004252; GO:0005886; GO:0006508; GO:0042802`
- `EC:3.4.21.105`

## Notes

Rhomboid protease GlpG (EC 3.4.21.105) (Intramembrane serine protease)
