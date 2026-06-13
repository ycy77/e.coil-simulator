---
entity_id: "gene.b0407"
entity_type: "gene"
name: "yajC"
source_database: "NCBI RefSeq"
source_id: "gene-b0407"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0407"
  - "yajC"
---

# yajC

`gene.b0407`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0407`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yajC (gene.b0407) is a gene entity. It encodes yajC (protein.P0ADZ7). Encoded protein function: FUNCTION: The SecYEG-SecDF-YajC-YidC holo-translocon (HTL) protein secretase/insertase is a supercomplex required for protein secretion, insertion of proteins into membranes, and assembly of membrane protein complexes (PubMed:27435098). The SecYEG complex is essential for assembly of a number of proteins and complexes, assembly is facilitated in the presence of the SecDF-YajC-YidC subcomplex (PubMed:27435098). {ECO:0000269|PubMed:27435098}. EcoCyc product frame: EG11096-MONOMER. Genomic coordinates: 427287-427619. EcoCyc protein note: YajC is is part of the heterotrimeric Sec translocon accessory complex. Early studies characterized the secD locus (composed of yajC-secD-secF), implicating the products of secD and secF in protein export and defining YajC as a dispensable membrane protein with unknown function . Under conditions of over production YajC forms a complex with both SecYEG and SecDF . YajC is not essential for cell viability or protein export . Membrane topology experiments indicate that the C-terminus of YajC is located in the cytoplasm and the N-terminus is buried in the membrane . The purified C-terminal portion of YajC exists as a trimer and forms a structure rich in β-strands .

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)
- `eco03060` Protein export (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADZ7|protein.P0ADZ7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001415,ECOCYC:EG11096,GeneID:945374`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:427287-427619:+; feature_type=gene
