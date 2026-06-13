---
entity_id: "gene.b1501"
entity_type: "gene"
name: "ydeP"
source_database: "NCBI RefSeq"
source_id: "gene-b1501"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1501"
  - "ydeP"
---

# ydeP

`gene.b1501`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1501`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeP (gene.b1501) is a gene entity. It encodes ydeP (protein.P77561). Encoded protein function: FUNCTION: Probably involved in acid resistance. {ECO:0000269|PubMed:12399493, ECO:0000269|PubMed:12694615}. EcoCyc product frame: G6791-MONOMER. Genomic coordinates: 1584207-1586486. EcoCyc protein note: Overexpression of the response regulator evgA confers acid resistance to exponentially growing cells and induces the expression of many genes including ydeP. Deletion of ydeP decreases the acid resistance of exponential phase cells overexpressing evgA . Overexpression of ydeP results in acid resistance and a reduced growth rate in exponential phase cells Transcription is activated by EvgA, which binds to inverted repeat sequences located upstream. Mutation of these inverted repeat sequences causes a defect in acid resistance . ydeP has sequence similarity with FDNG-MONOMER "fdnG", FORMATEDEHYDROGH-MONOMER "fdhF" and FDOG-MONOMER "fdoG" - encoding subunits from formate dehydrogenases .

## Biological Role

Repressed by hns (protein.P0ACF8), narP (protein.P31802), nac (protein.Q47005). Activated by evgA (protein.P0ACZ4), uvrY (protein.P0AED5), narL (protein.P0AF28), rcsB (protein.P0DMC7).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77561|protein.P77561]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=ydeP; function=+
- `activates` <-- [[protein.P0AED5|protein.P0AED5]] `RegulonDB` `S` - regulator=UvrY; target=ydeP; function=+
- `activates` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ydeP; function=+
- `activates` <-- [[protein.P0DMC7|protein.P0DMC7]] `RegulonDB` `S` - regulator=RcsB; target=ydeP; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=ydeP; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ydeP; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ydeP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005001,ECOCYC:G6791,GeneID:946055`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1584207-1586486:-; feature_type=gene
