---
entity_id: "protein.P08202"
entity_type: "protein"
name: "araA"
source_database: "UniProt"
source_id: "P08202"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "araA b0062 JW0061"
---

# araA

`protein.P08202`

## Static

- Type: `protein`
- Source: `UniProt:P08202`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the conversion of L-arabinose to L-ribulose. L-arabinose isomerase catalyzes the first step in the degradation of L-arabinose, its isomerization to L-ribulose. A reaction mechanism was proposed by . In vitro, the enzyme can also catalyze the conversion of D-galactose to D-tagatose, which is used commercially as a low-calorie substitute for sucrose . Electron micrographs showed that the subunits of L-arabinose isomerase are arranged in a stack of two trimers . Crystal structures of the enzyme alone and with a bound Mn2+ ion have been solved; they confirm that the enzyme forms a dimer of trimers . Most studies of the enzyme and its genetics were done in E. coli B/r. Transcription of the araBAD operon is induced in the presence of L-arabinose by the transcription factor AraC . araBAD expression can also induced by L-lyxose . araA mutants can not utilize L-arabinose for growth .

## Biological Role

Component of L-arabinose isomerase (complex.ecocyc.ARABISOM-CPLX).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the conversion of L-arabinose to L-ribulose.

## Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ARABISOM-CPLX|complex.ecocyc.ARABISOM-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b0062|gene.b0062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08202`
- `KEGG:ecj:JW0061;eco:b0062;`
- `GeneID:947511;`
- `GO:GO:0005829; GO:0008733; GO:0019568; GO:0019569; GO:0030145`
- `EC:5.3.1.4`

## Notes

L-arabinose isomerase (EC 5.3.1.4)
