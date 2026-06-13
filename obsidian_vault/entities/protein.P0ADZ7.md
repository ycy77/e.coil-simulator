---
entity_id: "protein.P0ADZ7"
entity_type: "protein"
name: "yajC"
source_database: "UniProt"
source_id: "P0ADZ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27435098}; Single-pass membrane protein {ECO:0000269|PubMed:16079137}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yajC b0407 JW0397"
---

# yajC

`protein.P0ADZ7`

## Static

- Type: `protein`
- Source: `UniProt:P0ADZ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:16079137, ECO:0000269|PubMed:27435098}; Single-pass membrane protein {ECO:0000269|PubMed:16079137}.

## Enriched Summary

FUNCTION: The SecYEG-SecDF-YajC-YidC holo-translocon (HTL) protein secretase/insertase is a supercomplex required for protein secretion, insertion of proteins into membranes, and assembly of membrane protein complexes (PubMed:27435098). The SecYEG complex is essential for assembly of a number of proteins and complexes, assembly is facilitated in the presence of the SecDF-YajC-YidC subcomplex (PubMed:27435098). {ECO:0000269|PubMed:27435098}. YajC is is part of the heterotrimeric Sec translocon accessory complex. Early studies characterized the secD locus (composed of yajC-secD-secF), implicating the products of secD and secF in protein export and defining YajC as a dispensable membrane protein with unknown function . Under conditions of over production YajC forms a complex with both SecYEG and SecDF . YajC is not essential for cell viability or protein export . Membrane topology experiments indicate that the C-terminus of YajC is located in the cytoplasm and the N-terminus is buried in the membrane . The purified C-terminal portion of YajC exists as a trimer and forms a structure rich in β-strands .

## Biological Role

Component of Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX), Sec translocon accessory complex (complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

FUNCTION: The SecYEG-SecDF-YajC-YidC holo-translocon (HTL) protein secretase/insertase is a supercomplex required for protein secretion, insertion of proteins into membranes, and assembly of membrane protein complexes (PubMed:27435098). The SecYEG complex is essential for assembly of a number of proteins and complexes, assembly is facilitated in the presence of the SecDF-YajC-YidC subcomplex (PubMed:27435098). {ECO:0000269|PubMed:27435098}.

## Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX|complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0407|gene.b0407]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADZ7`
- `KEGG:ecj:JW0397;eco:b0407;ecoc:C3026_01980;`
- `GeneID:86862952;93777053;945374;`
- `GO:GO:0005886; GO:0016020; GO:0031522; GO:0043952`

## Notes

Sec translocon accessory complex subunit YajC
