---
entity_id: "protein.P69931"
entity_type: "protein"
name: "hda"
source_database: "UniProt"
source_id: "P69931"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12618445}. Note=More protein is found in the inner than outer membrane fractions. {ECO:0000269|PubMed:12618445}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hda idaB yfgE b2496 JW5397 f248c"
---

# hda

`protein.P69931`

## Static

- Type: `protein`
- Source: `UniProt:P69931`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:12618445}. Note=More protein is found in the inner than outer membrane fractions. {ECO:0000269|PubMed:12618445}.

## Enriched Summary

FUNCTION: Mediates the interactions of DNA replication initiator protein DnaA with DNA polymerase subunit beta sliding clamp (dnaN) (PubMed:15150238). Stimulates hydrolysis of ATP-DnaA to ADP-DnaA, rendering DnaA inactive for reinitiation, a process called regulatory inhibition of DnaA or RIDA (PubMed:9674428, PubMed:18977760, PubMed:12730188, PubMed:22716942). ADP-binding activates Hda to hydrolyze DnaA-ATP; Hda monomers bind to ADP with about 200-fold greater affinity than for ATP (PubMed:18977760). RIDA function can be genetically separated from viability, suggesting this protein has another function as well (PubMed:22716942). {ECO:0000269|PubMed:11483528, ECO:0000269|PubMed:12730188, ECO:0000269|PubMed:15150238, ECO:0000269|PubMed:18977760, ECO:0000269|PubMed:22716942, ECO:0000269|PubMed:9674428}.; FUNCTION: Suppresses the toxic effect of overexpressing a TrfA N-terminal 163 residue fragment. Inhibits inner membrane-associated plasmid IncP-alpha RK2 replication probably by interacting with plasmid-encoded TrfA. {ECO:0000269|PubMed:12618445}. Hda is a member of the AAA+ chaperone-like family of ATPases that inhibits the reinitiation of DNA replication in concert with the CPLX0-3761 in a process termed RIDA (regulatory inactivation of DnaA)...

## Biological Role

Component of Hda-β-clamp complex (complex.ecocyc.CPLX0-10342).

## Annotation

FUNCTION: Mediates the interactions of DNA replication initiator protein DnaA with DNA polymerase subunit beta sliding clamp (dnaN) (PubMed:15150238). Stimulates hydrolysis of ATP-DnaA to ADP-DnaA, rendering DnaA inactive for reinitiation, a process called regulatory inhibition of DnaA or RIDA (PubMed:9674428, PubMed:18977760, PubMed:12730188, PubMed:22716942). ADP-binding activates Hda to hydrolyze DnaA-ATP; Hda monomers bind to ADP with about 200-fold greater affinity than for ATP (PubMed:18977760). RIDA function can be genetically separated from viability, suggesting this protein has another function as well (PubMed:22716942). {ECO:0000269|PubMed:11483528, ECO:0000269|PubMed:12730188, ECO:0000269|PubMed:15150238, ECO:0000269|PubMed:18977760, ECO:0000269|PubMed:22716942, ECO:0000269|PubMed:9674428}.; FUNCTION: Suppresses the toxic effect of overexpressing a TrfA N-terminal 163 residue fragment. Inhibits inner membrane-associated plasmid IncP-alpha RK2 replication probably by interacting with plasmid-encoded TrfA. {ECO:0000269|PubMed:12618445}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10342|complex.ecocyc.CPLX0-10342]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2496|gene.b2496]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69931`
- `KEGG:ecj:JW5397;eco:b2496;`
- `GeneID:86947384;946977;`
- `GO:GO:0005829; GO:0005886; GO:0006260; GO:0006270; GO:0016020; GO:0030174; GO:0032297; GO:0042802; GO:0043531; GO:1990078; GO:1990085`

## Notes

DnaA regulatory inactivator Hda (DnaA paralog) (Dp) (Protein IdaB)
