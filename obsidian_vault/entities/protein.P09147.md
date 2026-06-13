---
entity_id: "protein.P09147"
entity_type: "protein"
name: "galE"
source_database: "UniProt"
source_id: "P09147"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "galE galD b0759 JW0742"
---

# galE

`protein.P09147`

## Static

- Type: `protein`
- Source: `UniProt:P09147`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the metabolism of galactose. Catalyzes the conversion of UDP-galactose (UDP-Gal) to UDP-glucose (UDP-Glc) through a mechanism involving the transient reduction of NAD. It is only active on UDP-galactose and UDP-glucose. {ECO:0000269|PubMed:14235524}. UDP-glucose 4-epimerase (GalE) catalyzes a hydride transfer in the interconversion of UDP-galactose and UDP-glucose as part of galactose catabolism. The active epimerase contains two molecules of NAD+ per dimer . The monomer may also be catalytically active . The reaction mechanism has been studied extensively. The reaction proceeds via an intermolecular hydrogen transfer . The bound NAD+ is transiently reduced in the course of the reaction and was thought to be accompanied by a change in protein structure . When uridine nucleotides bind to the substrate site, it was thought that a protein conformational change is induced which increases the chemical reactivity of NAD+ . Complexes of UDP-glucose 4-epimerase containing NADH and uridine nucleotide are inactive . A number of crystal structures of the enzyme with a variety of ligands have been solved . They revealed that the active site accommodates a variety of sugars by rearrangement of water molecules rather than changes in side chain conformation . The 4'-ketopyranose reaction intermediate can rotate freely within the active site of the enzyme...

## Biological Role

Catalyzes UDP-glucose 4-epimerase; (reaction.R00291), UDP-N-acetyl-D-glucosamine 4-epimerase (reaction.R00418). Component of UDP-glucose 4-epimerase (complex.ecocyc.UDPGLUCEPIM-CPLX).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Annotation

FUNCTION: Involved in the metabolism of galactose. Catalyzes the conversion of UDP-galactose (UDP-Gal) to UDP-glucose (UDP-Glc) through a mechanism involving the transient reduction of NAD. It is only active on UDP-galactose and UDP-glucose. {ECO:0000269|PubMed:14235524}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01250` Biosynthesis of nucleotide sugars (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00291|reaction.R00291]] `KEGG` `database` - via EC:5.1.3.2
- `catalyzes` --> [[reaction.R00418|reaction.R00418]] `KEGG` `database` - via EC:5.1.3.2
- `is_component_of` --> [[complex.ecocyc.UDPGLUCEPIM-CPLX|complex.ecocyc.UDPGLUCEPIM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0759|gene.b0759]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09147`
- `KEGG:ecj:JW0742;eco:b0759;`
- `GeneID:945354;`
- `GO:GO:0003978; GO:0005737; GO:0005829; GO:0005975; GO:0005996; GO:0006012; GO:0009242; GO:0016857; GO:0033499; GO:0042802; GO:0070403`
- `EC:5.1.3.2`

## Notes

UDP-glucose 4-epimerase (EC 5.1.3.2) (Galactowaldenase) (UDP-galactose 4-epimerase)
