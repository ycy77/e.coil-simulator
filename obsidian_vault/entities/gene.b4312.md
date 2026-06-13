---
entity_id: "gene.b4312"
entity_type: "gene"
name: "fimB"
source_database: "NCBI RefSeq"
source_id: "gene-b4312"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4312"
  - "fimB"
---

# fimB

`gene.b4312`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4312`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimB (gene.b4312) is a gene entity. It encodes fimB (protein.P0ADH5). Encoded protein function: FUNCTION: FimB is one of the 2 regulatory proteins which control the phase variation of type 1 fimbriae in E.coli. These proteins mediate the periodic inversion of a 300bp DNA segment that harbors the promoter for the fimbrial structural gene, FimA. FimB switches FimA on. EcoCyc product frame: EG10309-MONOMER. EcoCyc synonyms: pil. Genomic coordinates: 4540957-4541559. EcoCyc protein note: FimB, along with FimE, is a recombinase in Escherichia coli which catalyzes the site-specific recombination required for inversion of a 314-bp invertible DNA element, the fim switch (fimS), to control transcription of the type I fimbrial structural genes--a process known as phase-variation switching. fimS contains the promoter for expression of the fimbrial structural genes. The promoter is positioned to allow expression of fimAICDFGH when fimS is in the ON orientation, but not when it is in the OFF orientation. FimB is responsible for both OFF-to-ON and ON-to-OFF switching at equal rates. FimE is responsible for primarily ON-to-OFF switching. FimB and FimE share significant homology with the lambda integrase family of site-specific recombinases...

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rseX (gene.b4603), hns (protein.P0ACF8). Activated by nanR (protein.P0A8W0), nagC (protein.P0AF20), basR (protein.P30843).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADH5|protein.P0ADH5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=fimB; function=+
- `activates` <-- [[protein.P0AF20|protein.P0AF20]] `RegulonDB` `C` - regulator=NagC; target=fimB; function=+
- `activates` <-- [[protein.P30843|protein.P30843]] `RegulonDB` `S` - regulator=BasR; target=fimB; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4603|gene.b4603]] `RegulonDB` `S` - regulator=RseX; target=fimB; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014141,ECOCYC:EG10309,GeneID:948832`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4540957-4541559:+; feature_type=gene
