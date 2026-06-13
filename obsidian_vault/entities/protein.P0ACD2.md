---
entity_id: "protein.P0ACD2"
entity_type: "protein"
name: "wcaF"
source_database: "UniProt"
source_id: "P0ACD2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "wcaF b2054 JW2039"
---

# wcaF

`protein.P0ACD2`

## Static

- Type: `protein`
- Source: `UniProt:P0ACD2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Putative colanic acid biosynthesis acetyltransferase WcaF (EC 2.3.1.-) WcaF is the acetyltransferase that catalyzes acetylation of the fucosyl residue in the UPP-linked disaccharide during biosynthesis of the extracellular polysaccharide CPD-21504 "colanic acid" (CA) . wcaF is located within a cluster of genes that are responsible for production of CA; wcaF was predicted to encode an acetyltransferase responsible for O-acetylation of the first fucosyl group of the CA hexasaccharide . wcaF is required for the production of colanic acid in a CA+ strain of E. coli K-12; a wcaF mutant (CA+wcaF31::cam) has significantly reduced CA production and additionally shows impaired biofilm architecture . Repression of wcaF (using CRISPRi/dCas9) in K-12 MG1655 at the beginning of biofilm culturing significantly inhibits biofilm formation with minimal effect on growth; regulation of wcaF expression allows spatial control of biofilm formation . Expression of wcaF is higher in wild-type biofilms than in biofilms formed by an rpoS mutant . Nomenclature for genes involved in bacterial polysaccharide synthesis is discussed in .

## Biological Role

Catalyzes RXN0-7342 (reaction.ecocyc.RXN0-7342).

## Enriched Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Annotation

Putative colanic acid biosynthesis acetyltransferase WcaF (EC 2.3.1.-)

## Pathways

- `eco00543` Exopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7342|reaction.ecocyc.RXN0-7342]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2054|gene.b2054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACD2`
- `KEGG:ecj:JW2039;eco:b2054;ecoc:C3026_11560;`
- `GeneID:93775137;946578;`
- `GO:GO:0008374; GO:0009103; GO:0009242; GO:0016413; GO:0044010; GO:0045228`
- `EC:2.3.1.-`

## Notes

Putative colanic acid biosynthesis acetyltransferase WcaF (EC 2.3.1.-)
