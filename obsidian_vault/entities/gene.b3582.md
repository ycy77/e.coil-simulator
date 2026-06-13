---
entity_id: "gene.b3582"
entity_type: "gene"
name: "sgbU"
source_database: "NCBI RefSeq"
source_id: "gene-b3582"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3582"
  - "sgbU"
---

# sgbU

`gene.b3582`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3582`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sgbU (gene.b3582) is a gene entity. It encodes sgbU (protein.P37679). Encoded protein function: FUNCTION: Catalyzes the isomerization of L-xylulose-5-phosphate to L-ribulose-5-phosphate (Potential). May be involved in the utilization of 2,3-diketo-L-gulonate. {ECO:0000305}. EcoCyc product frame: EG12286-MONOMER. EcoCyc synonyms: yiaR. Genomic coordinates: 3749232-3750092. EcoCyc protein note: SgbU appears to be required for the utilization of L-lyxose . Despite similarity to UlaE, no SgbU L-xylulose 5-phosphate 3-epimerase activity has yet been detected directly . Review:

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

- `encodes` --> [[protein.P37679|protein.P37679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sgbU; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sgbU; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=sgbU; function=+
- `represses` <-- [[protein.P37671|protein.P37671]] `RegulonDB` `C` - regulator=PlaR; target=sgbU; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011700,ECOCYC:EG12286,GeneID:948100`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3749232-3750092:+; feature_type=gene
