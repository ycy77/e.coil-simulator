---
entity_id: "protein.P69826"
entity_type: "protein"
name: "cmtA"
source_database: "UniProt"
source_id: "P69826"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmtA b2933 JW2900"
---

# cmtA

`protein.P69826`

## Static

- Type: `protein`
- Source: `UniProt:P69826`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P28008}. CmtA has 52% amino acid identity with the EIICB domain of MltA, the mannitol PTS permease. cmtA may encode a protein with 6 transmembrane regions; a conserved cysteine residue at position 377 may be required for phosphoryl transfer to substrate. Expression of cmtA under the control of heterologous promoter led to mannitol transport in mtlA mutants of E. coli K-12 .

## Biological Role

Component of mannitol-specific PTS enzyme II CmtBA (complex.ecocyc.CPLX-156).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II CmtAB PTS system is involved in D-mannitol transport. {ECO:0000250|UniProtKB:P28008}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-156|complex.ecocyc.CPLX-156]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2933|gene.b2933]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69826`
- `KEGG:ecj:JW2900;eco:b2933;ecoc:C3026_16060;`
- `GeneID:75173039;945256;`
- `GO:GO:0005886; GO:0009401; GO:0016301; GO:0022872`
- `EC:2.7.1.197`

## Notes

PTS system mannitol-specific cryptic EIICB component (EIICB-Mtl) (EII-Mtl) [Includes: Mannitol permease IIC component (PTS system mannitol-specific EIIC component); Mannitol-specific phosphotransferase enzyme IIB component (EC 2.7.1.197) (PTS system mannitol-specific EIIB component)]
