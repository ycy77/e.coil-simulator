---
entity_id: "protein.P28305"
entity_type: "protein"
name: "pabC"
source_database: "UniProt"
source_id: "P28305"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pabC b1096 JW1082"
---

# pabC

`protein.P28305`

## Static

- Type: `protein`
- Source: `UniProt:P28305`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the biosynthesis of p-aminobenzoate (PABA), a precursor of tetrahydrofolate. Converts 4-amino-4-deoxychorismate into 4-aminobenzoate (PABA) and pyruvate. {ECO:0000269|PubMed:1644759, ECO:0000269|PubMed:2251281}.

## Biological Role

Component of aminodeoxychorismate lyase (complex.ecocyc.ADCLY-CPLX).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of p-aminobenzoate (PABA), a precursor of tetrahydrofolate. Converts 4-amino-4-deoxychorismate into 4-aminobenzoate (PABA) and pyruvate. {ECO:0000269|PubMed:1644759, ECO:0000269|PubMed:2251281}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ADCLY-CPLX|complex.ecocyc.ADCLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1096|gene.b1096]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28305`
- `KEGG:ecj:JW1082;eco:b1096;ecoc:C3026_06625;`
- `GeneID:75203682;946647;`
- `GO:GO:0005829; GO:0008153; GO:0008696; GO:0030170; GO:0046654; GO:0046656`
- `EC:4.1.3.38`

## Notes

Aminodeoxychorismate lyase (EC 4.1.3.38) (4-amino-4-deoxychorismate lyase) (ADC lyase) (ADCL)
