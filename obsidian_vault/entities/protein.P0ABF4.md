---
entity_id: "protein.P0ABF4"
entity_type: "protein"
name: "eutM"
source_database: "UniProt"
source_id: "P0ABF4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000250|UniProtKB:P41791}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutM cchA yffZ b2457 JW2441"
---

# eutM

`protein.P0ABF4`

## Static

- Type: `protein`
- Source: `UniProt:P0ABF4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000250|UniProtKB:P41791}.

## Enriched Summary

FUNCTION: Probably a major component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation (Probable). Each homohexamer has a central pore with an opening of up to 8.6 Angstroms. A positively-charged funnel leads to the pore from each side of the hexamer; a phosphate or sulfate ion is found in the pore. The pore probably allows metabolite passage into and out of the BMC (PubMed:20044574, PubMed:20851901). {ECO:0000269|PubMed:20044574, ECO:0000269|PubMed:20851901, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901}.

## Biological Role

Component of putative ethanolamine catabolic microcompartment shell protein EutM (complex.ecocyc.CPLX0-7835).

## Annotation

FUNCTION: Probably a major component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation (Probable). Each homohexamer has a central pore with an opening of up to 8.6 Angstroms. A positively-charged funnel leads to the pore from each side of the hexamer; a phosphate or sulfate ion is found in the pore. The pore probably allows metabolite passage into and out of the BMC (PubMed:20044574, PubMed:20851901). {ECO:0000269|PubMed:20044574, ECO:0000269|PubMed:20851901, ECO:0000305|PubMed:20044574, ECO:0000305|PubMed:20851901}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7835|complex.ecocyc.CPLX0-7835]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2457|gene.b2457]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABF4`
- `KEGG:ecj:JW2441;eco:b2457;ecoc:C3026_13635;`
- `GeneID:86860588;93774683;946942;`
- `GO:GO:0005198; GO:0031471; GO:0034214; GO:0042802; GO:0046336`

## Notes

Bacterial microcompartment shell protein EutM (Bacterial microcompartment protein homohexamer) (BMC-H) (Ethanolamine utilization protein EutM)
