---
entity_id: "protein.P63746"
entity_type: "protein"
name: "eutS"
source_database: "UniProt"
source_id: "P63746"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:20044574}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutS ypfE b2462 JW2446"
---

# eutS

`protein.P63746`

## Static

- Type: `protein`
- Source: `UniProt:P63746`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000305|PubMed:20044574}.

## Enriched Summary

FUNCTION: A component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation. Its unusual hexameric shape may help form the BMC shell (Probable). Targets at least 2 proteins (EutC and EutE) to the interior of the BMC (By similarity). Proteins such as EutS containing circularly permuted BMC domains may play a key role in conferring heterogeneity and flexibility in this BMC (Probable). {ECO:0000250|UniProtKB:Q9ZFV7, ECO:0000305, ECO:0000305|PubMed:20044574}.

## Biological Role

Component of putative ethanolamine catabolic microcompartment shell protein EutS (complex.ecocyc.CPLX0-7836).

## Annotation

FUNCTION: A component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation. Its unusual hexameric shape may help form the BMC shell (Probable). Targets at least 2 proteins (EutC and EutE) to the interior of the BMC (By similarity). Proteins such as EutS containing circularly permuted BMC domains may play a key role in conferring heterogeneity and flexibility in this BMC (Probable). {ECO:0000250|UniProtKB:Q9ZFV7, ECO:0000305, ECO:0000305|PubMed:20044574}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7836|complex.ecocyc.CPLX0-7836]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2462|gene.b2462]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P63746`
- `KEGG:ecj:JW2446;eco:b2462;ecoc:C3026_13660;`
- `GeneID:86860593;946936;`
- `GO:GO:0005198; GO:0031469; GO:0031471; GO:0034214; GO:0042802; GO:0046336`

## Notes

Bacterial microcompartment shell protein EutS (Ethanolamine utilization protein EutS)
