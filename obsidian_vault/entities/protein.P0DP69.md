---
entity_id: "protein.P0DP69"
entity_type: "protein"
name: "phnE1"
source_database: "UniProt"
source_id: "P0DP69"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phnE1 b4104 JW4065"
---

# phnE1

`protein.P0DP69`

## Static

- Type: `protein`
- Source: `UniProt:P0DP69`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: N-terminal fragment of the PhnE protein, part of a phosphonate usage operon that is cryptic in K12 strains. Growth of K12 strains on phosphonate can be observed when it is used as the sole phosphorus source after a 60 hour lag period, suggesting the operon is activated (PubMed:2155195). An intact PhnE in strain B is (AC A0A140NFA3). Part of the binding-protein-dependent transport system for phosphonates; probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:2155195}. phnE1 is the first fragment of an interrupted gene in E. coli K-12 MG1655. The functional phnE gene (present in E. coli B and in mutants of K-12 that can metabolize phosphonates) encodes the integral membrane subunit of an ATP-dependent phosphonate/phosphate uptake system. E. coli K-12 is considered to be cryptic for phosphonate utilization - it is unable to use phosphonates as a source of phosphorus; however, (phn+) mutants [denoted phn (EcoK+)] can be obtained when the wild type is grown with phosphonates as the sole phosphorus source . The molecular basis of crypticity in phosphonate metabolism is associated with phnE: in Phn- strains of K-12, the phnE gene contains a triple octomer repeat which generates a frameshift mutation and a premature stop codon when compared to the sequence in E...

## Biological Role

Component of phosphonate/phosphate ABC transporter (complex.ecocyc.ABC-23-CPLX).

## Annotation

FUNCTION: N-terminal fragment of the PhnE protein, part of a phosphonate usage operon that is cryptic in K12 strains. Growth of K12 strains on phosphonate can be observed when it is used as the sole phosphorus source after a 60 hour lag period, suggesting the operon is activated (PubMed:2155195). An intact PhnE in strain B is (AC A0A140NFA3). Part of the binding-protein-dependent transport system for phosphonates; probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000305|PubMed:2155195}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-23-CPLX|complex.ecocyc.ABC-23-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (0)

_None._

## External IDs

- `UniProt:P0DP69`
- `GO:GO:0005886; GO:0015716; GO:0055085`

## Notes

Putative cryptic phosphonate transport system permease protein PhnE1
