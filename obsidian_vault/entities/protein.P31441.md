---
entity_id: "protein.P31441"
entity_type: "protein"
name: "ade"
source_database: "UniProt"
source_id: "P31441"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ade yicP b3665 JW3640"
---

# ade

`protein.P31441`

## Static

- Type: `protein`
- Source: `UniProt:P31441`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Adenine deaminase (Adenase) (Adenine aminase) (EC 3.5.4.2) AdeD is a substrate-specific adenine deaminase . In wild-type cells, levels of adenine deaminase are too low to satisfy the cellular purine requirement . Two metal ions per subunit are required for optimal adenine deaminase activity , and either Mn2+ or Fe2+ can satisfy this metal requirement . The catalytically active Fe/Fe enzyme contains two high-spin ferrous iron ions. Site-directed mutagenesis of His92, His214, His235 and Glu185 result in loss of catalytic activity and metal binding, and certain mutations in His90 result in loss of metal binding . A reaction mechanism has been proposed . Ferrous iron-containing enzyme also has catalase activity; exposure to hydrogen peroxide eventually damages the enzyme by oxygenation of various amino acid residues, and its adenine deaminase activity is concurrently lost. Superoxide formation can also be measured . AdeD expression appears to be induced by the presence of high amounts of adenine in the culture medium . Transcription of ade can be activated by various promoter mutations and is repressed more than 10-fold by the H-NS protein in wild type . Adu: Ade: "adenine deaminase"

## Biological Role

Component of adenine deaminase (complex.ecocyc.CPLX0-1683).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

Adenine deaminase (Adenase) (Adenine aminase) (EC 3.5.4.2)

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1683|complex.ecocyc.CPLX0-1683]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3665|gene.b3665]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31441`
- `KEGG:ecj:JW3640;eco:b3665;ecoc:C3026_19865;`
- `GeneID:948210;`
- `GO:GO:0000034; GO:0004096; GO:0006146; GO:0008198; GO:0030145; GO:0042803`
- `EC:3.5.4.2`

## Notes

Adenine deaminase (Adenase) (Adenine aminase) (EC 3.5.4.2)
