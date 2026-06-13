---
entity_id: "protein.P39394"
entity_type: "protein"
name: "symE"
source_database: "UniProt"
source_id: "P39394"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:17462020}. Note=Purifies with ribosomes. {ECO:0000269|PubMed:17462020}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "symE dinL sosC yjiW b4347 JW4310"
---

# symE

`protein.P39394`

## Static

- Type: `protein`
- Source: `UniProt:P39394`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:17462020}. Note=Purifies with ribosomes. {ECO:0000269|PubMed:17462020}.

## Enriched Summary

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (PubMed:17462020). Involved in the degradation and recycling of damaged RNA (PubMed:17462020). It is itself a target for degradation by the ATP-dependent protease Lon (PubMed:17462020). {ECO:0000269|PubMed:17462020}.

## Biological Role

Component of nucleoid-associated protein SymE (complex.ecocyc.CPLX0-8618).

## Annotation

FUNCTION: Toxic component of a type I toxin-antitoxin (TA) system (PubMed:17462020). Involved in the degradation and recycling of damaged RNA (PubMed:17462020). It is itself a target for degradation by the ATP-dependent protease Lon (PubMed:17462020). {ECO:0000269|PubMed:17462020}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8618|complex.ecocyc.CPLX0-8618]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4347|gene.b4347]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39394`
- `KEGG:ecj:JW4310;eco:b4347;ecoc:C3026_23485;`
- `GeneID:949088;`
- `GO:GO:0003677; GO:0003723; GO:0004521; GO:0005737; GO:0006974; GO:0009432; GO:0016070; GO:0016788; GO:0036386; GO:0042802; GO:0043590`
- `EC:3.1.-.-`

## Notes

Toxic protein SymE (Putative endoribonuclease SymE) (EC 3.1.-.-)
