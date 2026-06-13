---
entity_id: "gene.b1739"
entity_type: "gene"
name: "osmE"
source_database: "NCBI RefSeq"
source_id: "gene-b1739"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1739"
  - "osmE"
---

# osmE

`gene.b1739`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1739`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

osmE (gene.b1739) is a gene entity. It encodes osmE (protein.P0ADB1). Encoded protein function: Osmotically-inducible putative lipoprotein OsmE (Activator of ntr-like gene protein) EcoCyc product frame: EG10044-MONOMER. EcoCyc synonyms: anr. Genomic coordinates: 1821918-1822256. EcoCyc protein note: OsmE has a lipoprotein-type signal sequence at the amino terminus and is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). OsmE is an osmotically inducible gene product in E. coli. Operon fusion experiments demonstrated that osmE osmotic regulation probably occurs at the transcriptional level . Under conditions of low osmolarity, osmE is induced at the onset of stationary phase . In the absence of σS, the stationary phase sigma factor encoded by rpoS, stationary phase induction does not occur, but the osmotic effect is still observed . An osmE nonsynonymous mutation (OsmES44N) contributes to colistin resistance in a laboratory evolved strain .

## Biological Role

Repressed by fis (protein.P0A6R3). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADB1|protein.P0ADB1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=osmE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=osmE; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=osmE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005799,ECOCYC:EG10044,GeneID:945305`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1821918-1822256:-; feature_type=gene
