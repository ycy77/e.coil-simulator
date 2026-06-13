---
entity_id: "gene.b3581"
entity_type: "gene"
name: "sgbH"
source_database: "NCBI RefSeq"
source_id: "gene-b3581"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3581"
  - "sgbH"
---

# sgbH

`gene.b3581`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3581`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgbH (gene.b3581) is a gene entity. It encodes sgbH (protein.P37678). Encoded protein function: FUNCTION: Catalyzes the decarboxylation of 3-keto-L-gulonate-6-P into L-xylulose-5-P. May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000269|PubMed:11741871}. EcoCyc product frame: EG12285-MONOMER. EcoCyc synonyms: yiaQ. Genomic coordinates: 3748577-3749239. EcoCyc protein note: YiaQ/SgbH is one of two known 3-keto-L-gulonate-6-phosphate decarboxylases in E. coli . Expression from the yiaK promoter is moderately induced by fucose and ascorbate , and increased amounts of YiaQ protein are detected after aerobic growth on ascorbate . The presence of the amino acids proline, threonine, glutamate, glutamine or aspartate in the medium is required for yiaK promoter activity. Cells that overexpress the yiaK operon due to a mutation in the YiaJ repressor gain the ability to utilize L-ascorbate as the sole source of carbon . Review:

## Biological Role

Repressed by plaR (protein.P37671). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37678|protein.P37678]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sgbH; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgbH; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=sgbH; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=sgbH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011698,ECOCYC:EG12285,GeneID:948098`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3748577-3749239:+; feature_type=gene
