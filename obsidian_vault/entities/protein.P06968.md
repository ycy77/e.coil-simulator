---
entity_id: "protein.P06968"
entity_type: "protein"
name: "dut"
source_database: "UniProt"
source_id: "P06968"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:1311056, ECO:0000305|PubMed:9261872}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dut dnaS sof b3640 JW3615"
---

# dut

`protein.P06968`

## Static

- Type: `protein`
- Source: `UniProt:P06968`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:1311056, ECO:0000305|PubMed:9261872}.

## Enriched Summary

FUNCTION: This enzyme is involved in nucleotide metabolism: it produces dUMP, the immediate precursor of thymidine nucleotides and it decreases the intracellular concentration of dUTP so that uracil cannot be incorporated into DNA. {ECO:0000269|PubMed:9261872}.

## Biological Role

Component of dUTP diphosphatase (complex.ecocyc.DUTP-PYROP-CPLX).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: This enzyme is involved in nucleotide metabolism: it produces dUMP, the immediate precursor of thymidine nucleotides and it decreases the intracellular concentration of dUTP so that uracil cannot be incorporated into DNA. {ECO:0000269|PubMed:9261872}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.DUTP-PYROP-CPLX|complex.ecocyc.DUTP-PYROP-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b3640|gene.b3640]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06968`
- `KEGG:ecj:JW3615;eco:b3640;ecoc:C3026_19725;`
- `GeneID:948607;`
- `GO:GO:0000287; GO:0004170; GO:0005829; GO:0006226; GO:0032991; GO:0042802; GO:0046081; GO:0070207`
- `EC:3.6.1.23`

## Notes

Deoxyuridine 5'-triphosphate nucleotidohydrolase (dUTPase) (EC 3.6.1.23) (dUTP pyrophosphatase)
