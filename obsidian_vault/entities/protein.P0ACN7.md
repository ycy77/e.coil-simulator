---
entity_id: "protein.P0ACN7"
entity_type: "protein"
name: "cytR"
source_database: "UniProt"
source_id: "P0ACN7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cytR b3934 JW3905"
---

# cytR

`protein.P0ACN7`

## Static

- Type: `protein`
- Source: `UniProt:P0ACN7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: This protein negatively controls the transcription initiation of genes such as deoCABD, udp, and cdd encoding catabolizing enzymes and nupC, nupG, and tsx encoding transporting and pore-forming proteins. Binds cytidine and adenosine as effectors.

## Biological Role

Component of DNA-binding transcriptional repressor CytR (complex.ecocyc.CPLX0-7740).

## Annotation

FUNCTION: This protein negatively controls the transcription initiation of genes such as deoCABD, udp, and cdd encoding catabolizing enzymes and nupC, nupG, and tsx encoding transporting and pore-forming proteins. Binds cytidine and adenosine as effectors.

## Outgoing Edges (12)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7740|complex.ecocyc.CPLX0-7740]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0411|gene.b0411]] `RegulonDB` `C` - regulator=CytR; target=tsx; function=-
- `represses` --> [[gene.b2143|gene.b2143]] `RegulonDB` `C` - regulator=CytR; target=cdd; function=-
- `represses` --> [[gene.b2964|gene.b2964]] `RegulonDB` `S` - regulator=CytR; target=nupG; function=-
- `represses` --> [[gene.b3363|gene.b3363]] `RegulonDB` `S` - regulator=CytR; target=ppiA; function=-
- `represses` --> [[gene.b3461|gene.b3461]] `RegulonDB` `S` - regulator=CytR; target=rpoH; function=-
- `represses` --> [[gene.b3831|gene.b3831]] `RegulonDB` `C` - regulator=CytR; target=udp; function=-
- `represses` --> [[gene.b3934|gene.b3934]] `RegulonDB` `S` - regulator=CytR; target=cytR; function=-
- `represses` --> [[gene.b4381|gene.b4381]] `RegulonDB` `C` - regulator=CytR; target=deoC; function=-
- `represses` --> [[gene.b4382|gene.b4382]] `RegulonDB` `C` - regulator=CytR; target=deoA; function=-
- `represses` --> [[gene.b4383|gene.b4383]] `RegulonDB` `C` - regulator=CytR; target=deoB; function=-
- `represses` --> [[gene.b4384|gene.b4384]] `RegulonDB` `C` - regulator=CytR; target=deoD; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3934|gene.b3934]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACN7`
- `KEGG:ecj:JW3905;eco:b3934;`
- `GeneID:93777964;948427;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional repressor CytR
