---
entity_id: "gene.b0273"
entity_type: "gene"
name: "argF"
source_database: "NCBI RefSeq"
source_id: "gene-b0273"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0273"
  - "argF"
---

# argF

`gene.b0273`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0273`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argF (gene.b0273) is a gene entity. It encodes argF (protein.P06960). Encoded protein function: FUNCTION: Reversibly catalyzes the transfer of the carbamoyl group from carbamoyl phosphate (CP) to the N(epsilon) atom of ornithine (ORN) to produce L-citrulline, which is a substrate for argininosuccinate synthetase, the enzyme involved in the final step in arginine biosynthesis. {ECO:0000269|PubMed:789338}. EcoCyc product frame: CHAINF-MONOMER. Genomic coordinates: 289301-290305.

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06960|protein.P06960]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=argF; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=argF; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=argF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000939,ECOCYC:EG10067,GeneID:944844`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:289301-290305:-; feature_type=gene
