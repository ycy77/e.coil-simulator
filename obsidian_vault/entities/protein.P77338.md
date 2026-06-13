---
entity_id: "protein.P77338"
entity_type: "protein"
name: "mscK"
source_database: "UniProt"
source_id: "P77338"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mscK aefA kefA b0465 JW0454"
---

# mscK

`protein.P77338`

## Static

- Type: `protein`
- Source: `UniProt:P77338`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Mechanosensitive channel that opens in response to membrane tension and specific ionic conditions. Requires high concentrations of external K(+), NH(4)(+), Rb(+) or Cs(+) to gate. May participate in the regulation of osmotic pressure changes within the cell, although it does not appear to have a major role in osmolarity regulation. Forms an ion channel of 1.0 nanosiemens conductance. The channel can remain active for between 30 seconds and over 3 minutes; it does not desensitize upon extended pressure. Its activity is masked in wild-type cells by the MscS channel. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:12374733}. MscK is a potassium-dependent, mechanosensitive channel of small conductance. mscK encodes a mechanosensitive channel with similar or slightly lower conductance to the EG11160-MONOMER "MscS" channel of small conductance (0.8 - 1nS) ; MscK does not desensitize upon extended pressure application; ΔmscK cells survive the transition to low osmolarity media as do Δ(mscK mscS) double mutants . E. coli strain RQ2 carrying the kefA2 allele is unable to grow in high (0.6M) K+ medium in the presence of compatible solutes; the mutant strain exhibits a complex K+ specific phenotype that likely results from aberrant gating of the MscK channel (see further )...

## Biological Role

Catalyzes TRANS-RXN-86 (reaction.ecocyc.TRANS-RXN-86).

## Annotation

FUNCTION: Mechanosensitive channel that opens in response to membrane tension and specific ionic conditions. Requires high concentrations of external K(+), NH(4)(+), Rb(+) or Cs(+) to gate. May participate in the regulation of osmotic pressure changes within the cell, although it does not appear to have a major role in osmolarity regulation. Forms an ion channel of 1.0 nanosiemens conductance. The channel can remain active for between 30 seconds and over 3 minutes; it does not desensitize upon extended pressure. Its activity is masked in wild-type cells by the MscS channel. {ECO:0000269|PubMed:10202137, ECO:0000269|PubMed:11985727, ECO:0000269|PubMed:12374733}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-86|reaction.ecocyc.TRANS-RXN-86]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0465|gene.b0465]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77338`
- `KEGG:ecj:JW0454;eco:b0465;ecoc:C3026_02280;`
- `GeneID:945132;`
- `GO:GO:0005886; GO:0006813; GO:0008381; GO:0009992; GO:0035864`

## Notes

Mechanosensitive channel MscK (Potassium efflux system KefA)
