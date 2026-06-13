---
entity_id: "gene.b4170"
entity_type: "gene"
name: "mutL"
source_database: "NCBI RefSeq"
source_id: "gene-b4170"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4170"
  - "mutL"
---

# mutL

`gene.b4170`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4170`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutL (gene.b4170) is a gene entity. It encodes mutL (protein.P23367). Encoded protein function: FUNCTION: This protein is involved in the repair of mismatches in DNA. It is required for dam-dependent methyl-directed DNA mismatch repair. May act as a 'molecular matchmaker', a protein that promotes the formation of a stable complex between two or more DNA-binding proteins in an ATP-dependent manner without itself being part of the final effector complex. The ATPase activity of MutL is stimulated by DNA. EcoCyc product frame: EG11281-MONOMER. Genomic coordinates: 4397412-4399259.

## Biological Role

Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03430` Mismatch repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23367|protein.P23367]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mutL; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=mutL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013655,ECOCYC:EG11281,GeneID:948691`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4397412-4399259:+; feature_type=gene
