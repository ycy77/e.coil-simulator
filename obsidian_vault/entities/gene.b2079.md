---
entity_id: "gene.b2079"
entity_type: "gene"
name: "baeR"
source_database: "NCBI RefSeq"
source_id: "gene-b2079"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2079"
  - "baeR"
---

# baeR

`gene.b2079`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2079`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

baeR (gene.b2079) is a gene entity. It encodes baeR (protein.P69228). Encoded protein function: FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates the mdtABCD (PubMed:12107133, PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operon (PubMed:21255106). {ECO:0000269|PubMed:12107133, ECO:0000269|PubMed:12107134, ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:21255106}. EcoCyc product frame: PHOSPHO-BAER. Genomic coordinates: 2164276-2164998. EcoCyc protein note: BaeR (bacterial adaptive response, response-regulator ) has been shown to regulate directly genes involved in drug resistance and indirectly appears to regulate genes involved in several cellular processes, such as flagellum biosynthesis, chemotaxis, and maltose transport . BaeR belongs to the BaeS/BaeR two-component system . Both genes, baeR, encoding the response regulator, and baeS, encoding the sensor kinase, are located at the end of the operon (mdtABCD-baeSR) regulated by BaeR . It has been suggested that BaeS senses envelope disorder . Indole and zinc have been used as inducers of this disorder. BaeR is the primary regulator of the ethanol stress response . Leblanc et al...

## Biological Role

Activated by cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69228|protein.P69228]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=baeR; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=baeR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006884,ECOCYC:EG11618,GeneID:946605`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2164276-2164998:+; feature_type=gene
