---
entity_id: "gene.b4124"
entity_type: "gene"
name: "dcuR"
source_database: "NCBI RefSeq"
source_id: "gene-b4124"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4124"
  - "dcuR"
---

# dcuR

`gene.b4124`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4124`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dcuR (gene.b4124) is a gene entity. It encodes dcuR (protein.P0AD01). Encoded protein function: FUNCTION: Member of the two-component regulatory system DcuR/DcuS. Involved in the C4-dicarboxylate-stimulated regulation of the genes encoding the anaerobic fumarate respiratory system (frdABCD; nuoAN; dcuB; dcuC; sdhCDAB; etc.). Weakly regulates the aerobic C4-dicarboxylate transporter dctA. EcoCyc product frame: PHOSPHO-DCUR-MONOMER. EcoCyc synonyms: yjdG. Genomic coordinates: 4349315-4350034.

## Biological Role

Repressed by narL (protein.P0AF28). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD01|protein.P0AD01]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dcuR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=dcuR; function=+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=dcuR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013507,ECOCYC:G7826,GeneID:948640`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4349315-4350034:-; feature_type=gene
