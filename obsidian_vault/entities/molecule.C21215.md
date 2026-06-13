---
entity_id: "molecule.C21215"
entity_type: "small_molecule"
name: "Prenylated FMNH2"
source_database: "KEGG"
source_id: "C21215"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Prenylated FMNH2"
  - "Reduced prFMN"
---

# Prenylated FMNH2

`molecule.C21215`

## Static

- Type: `small_molecule`
- Source: `KEGG:C21215`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Prenylated FMNH2; Reduced prFMN CPD-18260 "Prenylated flavin mononucleotide" is a cofactor required by the UbiD family of reversible decarboxylases involved in ubiquinone biosynthesis, biological decomposition of lignin, and biotransformation of aromatic compounds . In archaea the compound serves as a cofactor for EC-4.1.1.126, an essential component of the archaeal mevalonate biosynthesis pathway .

## Biological Role

Produced in 1 reaction(s). Binds 3-octaprenyl-4-hydroxybenzoate decarboxylase (complex.ecocyc.CPLX0-301).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Annotation

KEGG compound: Prenylated FMNH2; Reduced prFMN

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)

## Outgoing Edges (2)

- `binds` --> [[complex.ecocyc.CPLX0-301|complex.ecocyc.CPLX0-301]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_product_of` --> [[reaction.ecocyc.RXN-16937|reaction.ecocyc.RXN-16937]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C21215`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
