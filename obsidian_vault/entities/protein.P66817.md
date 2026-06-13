---
entity_id: "protein.P66817"
entity_type: "protein"
name: "diaA"
source_database: "UniProt"
source_id: "P66817"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "diaA yraO b3149 JW3118"
---

# diaA

`protein.P66817`

## Static

- Type: `protein`
- Source: `UniProt:P66817`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for the timely initiation of chromosomal replication via direct interactions with the DnaA initiator protein. {ECO:0000269|PubMed:15326179, ECO:0000269|PubMed:17699754}. Proper amounts of DiaA are required for the timely initiation of chromosomal replication. DiaA interacts directly with the N-terminal domains I-II of PD03831 DnaA in a DNA-independent manner and stimulates the assembly of DnaA on G0-10506 oriC, conformational changes in the initiation complex, and unwinding of oriC . Both DnaA binding and homotetramerization of DiaA are required for stimulation of replication . A crystal structure of DiaA has been solved at 1.8 Å resolution, showing that DiaA forms a homotetramer . Residues required for tetramerization or DnaA binding were identified by mutagenesis . DnaA F46 is the crucial residue that is required for interaction with DiaA as well as DnaB . Timing of replication initiation is disrupted in both a diaA mutant and a DiaA overexpression strain . DiaA: "DnaA initiator-associating factor A" Reviews:

## Biological Role

Component of DnaA initiator-associating protein DiaA (complex.ecocyc.CPLX0-3221).

## Annotation

FUNCTION: Required for the timely initiation of chromosomal replication via direct interactions with the DnaA initiator protein. {ECO:0000269|PubMed:15326179, ECO:0000269|PubMed:17699754}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3221|complex.ecocyc.CPLX0-3221]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3149|gene.b3149]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P66817`
- `KEGG:ecj:JW3118;eco:b3149;ecoc:C3026_17155;`
- `GeneID:86861295;93778835;947661;`
- `GO:GO:0006260; GO:0032298; GO:0042802; GO:0042803; GO:0097367; GO:1901135; GO:1990102`

## Notes

DnaA initiator-associating protein DiaA
