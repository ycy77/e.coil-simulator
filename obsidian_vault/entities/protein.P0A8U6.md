---
entity_id: "protein.P0A8U6"
entity_type: "protein"
name: "metJ"
source_database: "UniProt"
source_id: "P0A8U6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metJ b3938 JW3909"
---

# metJ

`protein.P0A8U6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8U6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This regulatory protein, when combined with SAM (S-adenosylmethionine) represses the expression of the methionine regulon and of enzymes involved in SAM synthesis. It is also autoregulated.

## Biological Role

Component of DNA-binding transcriptional repressor MetJ-S-adenosyl-L-methionine (complex.ecocyc.CPLX0-7796), MetJ-MTA (complex.ecocyc.CPLX0-8026), MetJ-adenine (complex.ecocyc.CPLX0-8027), MetJ-S-adenosylmethionine (complex.ecocyc.MONOMER0-157).

## Annotation

FUNCTION: This regulatory protein, when combined with SAM (S-adenosylmethionine) represses the expression of the methionine regulon and of enzymes involved in SAM synthesis. It is also autoregulated.

## Outgoing Edges (10)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7796|complex.ecocyc.CPLX0-7796]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8026|complex.ecocyc.CPLX0-8026]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8027|complex.ecocyc.CPLX0-8027]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.MONOMER0-157|complex.ecocyc.MONOMER0-157]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b2152|gene.b2152]] `RegulonDB` `S` - regulator=MetJ; target=yeiB; function=-
- `represses` --> [[gene.b2153|gene.b2153]] `RegulonDB` `S` - regulator=MetJ; target=folE; function=-
- `represses` --> [[gene.b3008|gene.b3008]] `RegulonDB` `S` - regulator=MetJ; target=metC; function=-
- `represses` --> [[gene.b3828|gene.b3828]] `RegulonDB` `S` - regulator=MetJ; target=metR; function=-
- `represses` --> [[gene.b3829|gene.b3829]] `RegulonDB` `S` - regulator=MetJ; target=metE; function=-
- `represses` --> [[gene.b4013|gene.b4013]] `RegulonDB` `C` - regulator=MetJ; target=metA; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3938|gene.b3938]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8U6`
- `KEGG:ecj:JW3909;eco:b3938;ecoc:C3026_21280;`
- `GeneID:86861664;93777954;948435;`
- `GO:GO:0003677; GO:0003700; GO:0005829; GO:0009086; GO:0045892`

## Notes

Met repressor (Met regulon regulatory protein MetJ)
