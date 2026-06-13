---
entity_id: "gene.b4313"
entity_type: "gene"
name: "fimE"
source_database: "NCBI RefSeq"
source_id: "gene-b4313"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4313"
  - "fimE"
---

# fimE

`gene.b4313`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4313`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimE (gene.b4313) is a gene entity. It encodes fimE (protein.P0ADH7). Encoded protein function: FUNCTION: FimE is one of the 2 regulatory proteins which control the phase variation of type 1 fimbriae in E.coli. These proteins mediate the periodic inversion of a 300bp DNA segment that harbors the promoter for the fimbrial structural gene, fimA. FimE switches fimA off. EcoCyc product frame: EG10312-MONOMER. EcoCyc synonyms: hyp, pilH. Genomic coordinates: 4542037-4542633. EcoCyc protein note: FimE, along with FimB, is a recombinase in Escherichia coli which catalyzes the site-specific recombination required for inversion of a 314-bp invertible DNA element, the fim switch (fimS), to control transcription of the type I fimbrial structural genes--a process known as phase-variation switching. fimS contains the promoter for expression of the fimbrial structural genes. The promoter is positioned to allow expression of fimAICDFGH when fimS is in the ON orientation, but not when it is in the OFF orientation. FimB is responsible for both OFF-to-ON and ON-to-OFF switching at equal rates. FimE is responsible for primarily ON-to-OFF switching. FimB and FimE share significant homology with the lambda integrase family of site-specific recombinases...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), lrhA (protein.P36771).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADH7|protein.P0ADH7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fimE; function=+
- `activates` <-- [[protein.P36771|protein.P36771]] `RegulonDB` `S` - regulator=LrhA; target=fimE; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fimE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014143,ECOCYC:EG10312,GeneID:948836`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4542037-4542633:+; feature_type=gene
