---
entity_id: "protein.P0AG86"
entity_type: "protein"
name: "secB"
source_database: "UniProt"
source_id: "P0AG86"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "secB b3609 JW3584"
---

# secB

`protein.P0AG86`

## Static

- Type: `protein`
- Source: `UniProt:P0AG86`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: One of the proteins required for the normal export of some preproteins out of the cell cytoplasm. It is a molecular chaperone that binds to a subset of precursor proteins, maintaining them in a translocation-competent state. For 2 proteins (MBP, MalE and PhoA) the substrate is wrapped around the homotetramer, which prevents it from folding (PubMed:27501151). It also specifically binds to its receptor SecA. Its substrates include DegP, FhuA, FkpA, GBP, LamB, MalE (MBP), OmpA, OmpF, OmpT, OmpX, OppA, PhoE, TolB, TolC, YbgF, YcgK, YgiW and YncE (PubMed:16352602). {ECO:0000269|PubMed:16352602, ECO:0000269|PubMed:16522795, ECO:0000269|PubMed:27501151}.

## Biological Role

Component of protein export chaperone SecB (complex.ecocyc.CPLX0-8046).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: One of the proteins required for the normal export of some preproteins out of the cell cytoplasm. It is a molecular chaperone that binds to a subset of precursor proteins, maintaining them in a translocation-competent state. For 2 proteins (MBP, MalE and PhoA) the substrate is wrapped around the homotetramer, which prevents it from folding (PubMed:27501151). It also specifically binds to its receptor SecA. Its substrates include DegP, FhuA, FkpA, GBP, LamB, MalE (MBP), OmpA, OmpF, OmpT, OmpX, OppA, PhoE, TolB, TolC, YbgF, YcgK, YgiW and YncE (PubMed:16352602). {ECO:0000269|PubMed:16352602, ECO:0000269|PubMed:16522795, ECO:0000269|PubMed:27501151}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8046|complex.ecocyc.CPLX0-8046]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3609|gene.b3609]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AG86`
- `KEGG:ecj:JW3584;eco:b3609;ecoc:C3026_19570;`
- `GeneID:86861728;86944403;948123;`
- `GO:GO:0005829; GO:0006457; GO:0006605; GO:0008104; GO:0015031; GO:0036506; GO:0043952; GO:0051082; GO:0051262; GO:0070678`

## Notes

Protein-export protein SecB (Chaperone SecB)
