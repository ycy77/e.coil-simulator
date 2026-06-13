---
entity_id: "gene.b2009"
entity_type: "gene"
name: "sbmC"
source_database: "NCBI RefSeq"
source_id: "gene-b2009"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2009"
  - "sbmC"
---

# sbmC

`gene.b2009`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2009`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sbmC (gene.b2009) is a gene entity. It encodes sbmC (protein.P33012). Encoded protein function: FUNCTION: Inhibits the supercoiling activity of DNA gyrase. Acts by inhibiting DNA gyrase at an early step, prior to (or at the step of) binding of DNA by the gyrase. It protects cells against toxins that target DNA gyrase, by inhibiting activity of these toxins and reducing the formation of lethal double-strand breaks in the cell. Protects cells against the natural plasmid-encoded toxins microcin B17 (MccB17) and CcdB, and synthetic quinolones. Can also protect cells against alkylating agents that act independently of DNA gyrase, suggesting a more general role in protecting cells against DNA damage. {ECO:0000269|PubMed:11850398, ECO:0000269|PubMed:13680098, ECO:0000269|PubMed:8709849, ECO:0000269|PubMed:9442027}. EcoCyc product frame: EG11892-MONOMER. EcoCyc synonyms: dgi, gyrI, yeeB. Genomic coordinates: 2080789-2081262. EcoCyc protein note: SbmC is an inhibitor of DNA gyrase-mediated DNA supercoiling that inhibits the enzyme activity at an early step . Because this inhibitor interferes with DNA binding by gyrase, it also protects the cell from toxins that act via DNA damage caused by DNA-bound gyrase (e.g. the extrachromosomal CcdB and microcin B17 toxins and quinoline drugs)...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33012|protein.P33012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sbmC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006670,ECOCYC:EG11892,GeneID:946546`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2080789-2081262:-; feature_type=gene
